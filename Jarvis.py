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