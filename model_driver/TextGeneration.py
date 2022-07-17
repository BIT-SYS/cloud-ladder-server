import torch
from PIL import Image
from min_dalle import MinDalle

model = MinDalle(
    models_root='./data/min_dalle',
    dtype=torch.float32,
    device='cpu',
    is_mega=False,
    is_reusable=True
)

def inference(text):
    image = model.generate_image(
        text=text,
        seed=-1,
        grid_size=1,
        temperature=1,
        top_k=256,
        supercondition_factor=32,
        is_verbose=False
    )
    return image