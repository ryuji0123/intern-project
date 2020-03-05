from pdf2image import convert_from_path
from os import path
from hashed_dist import HashedDistHandler
from env import SAMPLE_IMG_ROOT_PATH, SAMPLE_PDF_ROOT_PATH
import cv2
from PIL import Image
import numpy as np

SAMPLE_IMG_PATH = path.join(SAMPLE_IMG_ROOT_PATH, 'sample{}.png')

if __name__ == '__main__':
    hdh = HashedDistHandler()
    pages = convert_from_path(path.join(SAMPLE_PDF_ROOT_PATH, 'sample.pdf'))
    for idx, p in enumerate(pages):
        p.save(SAMPLE_IMG_PATH.format(idx), 'PNG')
