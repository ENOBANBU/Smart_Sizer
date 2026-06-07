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

def extract_contours(seg_img):
    alpha_channel = seg_img[:, :, 3]
    _, binary_mask = cv2.threshold(alpha_channel, 10, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest = max(contours, key=cv2.contourArea)
    return largest.reshape(-1, 2)

def smooth_cons(contour, n_pts = 200):
    deltas = np.diff(contour, axis=0)
    dists = np.sqrt((deltas ** 2).sum(axis=1))
    cumulative = np.concatenate([[0], np.cumsum(dists)])
    tot_len = cumulative[-1]
    sample_pos = np.linspace(0, tot_len, n_pts)

    smooth_x = np.interp(sample_pos, cumulative, contour[:, 0])
    smooth_y = np.interp(sample_pos, cumulative, contour[:, 1])

    return np.column_stack((smooth_x, smooth_y))