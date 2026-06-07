import cv2
import numpy as np
from rembg import remove
from PIL import Image
import io

def load_img(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Could not load image from path: {path}")
    return img

def seg_obj(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    output = remove(pil_img)

    return np.array(output)
