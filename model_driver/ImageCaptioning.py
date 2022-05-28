from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
sys.path.append("models/ImageCaptioning.pytorch")
import uuid
import json
import os
import torch
import captioning.models as models
import captioning.utils.opts as opts
from captioning.data.dataloader import *
from captioning.data.dataloaderraw import *
import captioning.utils.eval_utils as eval_utils
import argparse
import captioning.utils.misc as utils
import captioning.modules.losses as losses

# Input arguments and options
parser = argparse.ArgumentParser()
# Input paths
parser.add_argument('--model', type=str, default='data/model-best.pth',
                    help='path to model to evaluate')
parser.add_argument('--cnn_model', type=str,  default='resnet101',
                    help='resnet101, resnet152')
parser.add_argument('--infos_path', type=str, default='data/infos_trans_nscl-best.pkl',
                    help='path to infos to evaluate')
parser.add_argument('--only_lang_eval', type=int, default=0,
                    help='lang eval on saved results')
parser.add_argument('--force', type=int, default=0,
                    help='force to evaluate no matter if there are results available')
parser.add_argument('--device', type=str, default='cuda',
                    help='cpu or cuda')
opts.add_eval_options(parser)
opts.add_diversity_opts(parser)
opt = parser.parse_args()
opt.dump_images = 0

basedir = 'data/tmp'
if not os.path.exists(basedir):
    os.mkdir(basedir)
opt.image_folder = basedir

# Load infos
with open(opt.infos_path, 'rb') as f:
    infos = utils.pickle_load(f)

# override and collect parameters
replace = ['input_fc_dir', 'input_att_dir', 'input_box_dir',
            'input_label_h5', 'input_json', 'batch_size', 'id']
ignore = ['start_from']

for k in vars(infos['opt']).keys():
    if k in replace:
        setattr(opt, k, getattr(opt, k) or getattr(infos['opt'], k, ''))
    elif k not in ignore:
        if k not in vars(opt):
            vars(opt).update({k: vars(infos['opt'])[k]})  # copy over options from model

vocab = infos['vocab']  # ix -> word mapping
# Setup the model
opt.vocab = vocab
model = models.setup(opt)
del opt.vocab
model.load_state_dict(torch.load(opt.model, map_location='cpu'))
model.to(opt.device)
model.eval()
crit = losses.LanguageModelCriterion()

def inference(img):
    id = str(uuid.uuid1())
    dirname = basedir + "/" + id + "/"
    os.mkdir(dirname)
    img.save(dirname + "image.png")
    opt.image_folder = dirname

    loader = DataLoaderRaw({'folder_path': opt.image_folder, 'coco_json': opt.coco_json,
                            'batch_size': opt.batch_size, 'cnn_model': opt.cnn_model})
    loader.dataset.ix_to_word = infos['vocab']
    # Set sample options
    opt.dataset = opt.input_json
    loss, split_predictions, lang_stats = eval_utils.eval_split(model, crit, loader, vars(opt))
    print(split_predictions[0]['caption'])
    return split_predictions[0]['caption']
