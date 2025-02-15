import os
import glob
import sys
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import rembg

class BLIP2():
    def __init__(self, device='cuda'):
        self.device = device
        from transformers import AutoProcessor, Blip2ForConditionalGeneration
        self.processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
        self.model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16).to(device)

    @torch.no_grad()
    def __call__(self, image):
        image = Image.fromarray(image)
        inputs = self.processor(image, return_tensors="pt").to(self.device, torch.float16)

        generated_ids = self.model.generate(**inputs, max_new_tokens=20)
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

        return generated_text

def rgb2gray(rgb):
    intensities = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    img_copy = rgb.copy()
    img_copy[..., :3] = np.stack((intensities, intensities, intensities), axis=-1)
    return img_copy

def to_rgba(path, size=256):
    file = path
    out_dir = os.path.dirname(path)

    out_base = os.path.basename(file).split('.')[0]
    out_rgba = os.path.join(out_dir, out_base + '_rgba.png')

    # load image
    print(f'[INFO] loading image {file}...')
    image = cv2.imread(file, cv2.IMREAD_UNCHANGED)

    final_rgba = 255 * np.ones((size, size, 4), dtype=np.uint8)
    final_rgba[:, :, :3] = image

    # write image
    cv2.imwrite(out_rgba, final_rgba)
    return out_rgba

def remove_background(path, size=256, border_ratio=0.2):
    session = rembg.new_session(model_name='u2net')

    file = path
    out_dir = os.path.dirname(path)

    out_base = os.path.basename(file).split('.')[0]
    out_rgba = os.path.join(out_dir, out_base + '_rgba.png')

    # load image
    print(f'[INFO] loading image {file}...')
    image = cv2.imread(file, cv2.IMREAD_UNCHANGED)

    # carve background
    print(f'[INFO] background removal...')
    # First find the background and the mask
    carved_image = rembg.remove(image, session=session)
    mask = carved_image[..., -1] > 0  # The values that were not made transparent
    flip_mask = carved_image[..., -1] <= 0

    # recenter
    print(f'[INFO] recenter...')
    final_rgba = np.zeros((size, size, 4), dtype=np.uint8)

    coords = np.nonzero(mask)
    x_min, x_max = coords[0].min(), coords[0].max()
    y_min, y_max = coords[1].min(), coords[1].max()
    h = x_max - x_min
    w = y_max - y_min
    desired_size = int(size * (1 - border_ratio))
    scale = desired_size / max(h, w)
    h2 = int(h * scale)
    w2 = int(w * scale)
    x2_min = (size - h2) // 2
    x2_max = x2_min + h2
    y2_min = (size - w2) // 2
    y2_max = y2_min + w2
    final_rgba[x2_min:x2_max, y2_min:y2_max] = cv2.resize(carved_image[x_min:x_max, y_min:y_max], (w2, h2),
                                                          interpolation=cv2.INTER_AREA)

    # write image
    cv2.imwrite(out_rgba, final_rgba)
    return out_rgba

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help="path to image (png, jpeg, etc.)")
    parser.add_argument('--model', default='u2net', type=str, help="rembg model, see https://github.com/danielgatis/rembg#models")
    parser.add_argument('--size', default=256, type=int, help="output resolution")
    parser.add_argument('--border_ratio', default=0.2, type=float, help="output border ratio")
    parser.add_argument('--recenter', type=bool, default=True, help="recenter, potentially not helpful for multiview zero123")
    parser.add_argument('--white_bg', type=bool, default=False, help="make the bg white")
    parser.add_argument('--grayscale', type=bool, default=False, help="make the image grayscale")

    opt = parser.parse_args()

    session = rembg.new_session(model_name=opt.model)

    if os.path.isdir(opt.path):
        print(f'[INFO] processing directory {opt.path}...')
        files = glob.glob(f'{opt.path}/*')
        out_dir = opt.path
    else: # isfile
        files = [opt.path]
        out_dir = os.path.dirname(opt.path)
    
    for file in files:

        out_base = os.path.basename(file).split('.')[0]
        out_rgba = os.path.join(out_dir, out_base + '_rgba.png')

        # load image
        print(f'[INFO] loading image {file}...')
        image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        
        # carve background
        print(f'[INFO] background removal...')
        # First find the background and the mask
        carved_image = rembg.remove(image, session=session)
        mask = carved_image[..., -1] > 0 # The values that were not made transparent
        flip_mask = carved_image[..., -1] <= 0

        # Then change the bg color if appropriate
        if opt.white_bg:
            # carved_image = rembg.bg.apply_background_color(carved_image, (255, 255, 255, 255))
            carved_image = rembg.remove(image, session=session, bgcolor=(255, 255, 255, 255)) # [H, W, 4]

        if opt.grayscale:
            carved_image = rgb2gray(carved_image)

        # recenter
        if opt.recenter:
            print(f'[INFO] recenter...')
            final_rgba = np.zeros((opt.size, opt.size, 4), dtype=np.uint8)

            coords = np.nonzero(mask)
            x_min, x_max = coords[0].min(), coords[0].max()
            y_min, y_max = coords[1].min(), coords[1].max()
            h = x_max - x_min
            w = y_max - y_min
            desired_size = int(opt.size * (1 - opt.border_ratio))
            scale = desired_size / max(h, w)
            h2 = int(h * scale)
            w2 = int(w * scale)
            x2_min = (opt.size - h2) // 2
            x2_max = x2_min + h2
            y2_min = (opt.size - w2) // 2
            y2_max = y2_min + w2
            final_rgba[x2_min:x2_max, y2_min:y2_max] = cv2.resize(carved_image[x_min:x_max, y_min:y_max], (w2, h2), interpolation=cv2.INTER_AREA)
            
        else:
            final_rgba = carved_image
        
        # write image
        cv2.imwrite(out_rgba, final_rgba)