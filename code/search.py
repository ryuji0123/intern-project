import json
import cv2
import numpy as np
from os import path
from PIL import Image
from pdf2image import convert_from_path
from hashed_dist import HashedDistHandler
from env import PDF_ROOT_PATH, IMG_ROOT_PATH

CURRENT_TEMPLATE_PATH = path.join(IMG_ROOT_PATH, 'cur_template.png')

if __name__ == '__main__':
    with open('../public/json/nsample.json', 'r') as f:
        data = json.load(f)

    hdh = HashedDistHandler()
    pages = convert_from_path(path.join(PDF_ROOT_PATH, 'sample.pdf'))
    ref = []

    for p in pages:
        p.save(CURRENT_TEMPLATE_PATH, 'PNG')
        frame = Image.fromarray(np.uint8(cv2.imread(CURRENT_TEMPLATE_PATH)))
        dist = float('inf')
        for d in data:
            if hdh.calcHammingDistBetweenImageAndHash(data[d], frame) < dist:
                seconds = d
                dist = hdh.calcHammingDistBetweenImageAndHash(data[d], frame)
        
        ref.append(seconds)
        if len(ref) == len(data): break

    with open('../public/json/matched.json', 'w') as f:
        json.dump(ref, f)