import sys
import librosa
import soundfile
import io
import uuid
import os
from flask import send_file

root = 'data/'
if not os.path.exists(root):
    os.mkdir(root)
subdirectory = root + 'tmp/'
if not os.path.exists(subdirectory):
    os.mkdir(subdirectory)
def inference(audio,type):
    id = str(uuid.uuid1())
    dirname = subdirectory + "/" + id + "/"
    os.mkdir(dirname)
    audio.save(dirname + "demo_audio.wav")
    audio_file = dirname + 'demo_audio.wav'
    y,sr = librosa.load(audio_file)
    #通过移动音调变声 ，20是上移20个半步， 如果是 -20 下移20个半步
    if type == 'high':
        b = librosa.effects.pitch_shift(y, sr, n_steps=20)
    else:
        b = librosa.effects.pitch_shift(y, sr, n_steps=-20)
    soundfile.write(audio_file,b,sr)
    return send_file(audio_file, mimetype="application/octet-stream", as_attachment=True)
        return send_file(audio_file, mimetype="application/octet-stream", as_attachment=True)
    #目前了解到的音频转换模型有两种：
    #CycleGAN-VC2和pytorch-StarGAN-VC
    #CycleGAN-VC2：
    #    用于将一种声音转变为某个特定对象的声音，Github上有转变为高晓松、凯特温切斯特、钉宫的项目，但没有数据集和对应的预训练模型。
    #pytorch-StarGAN-VC：
    #    用于将一类声音转变为另一类，例如男声转女声，女声转男声。github上对应项目的代码有严重问题，无法训练，需要修改。
    #由于模型训练困难，目前仅通过移动声调变声
        
