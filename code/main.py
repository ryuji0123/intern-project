from pdf2image import convert_from_path
from os import path
from hashed_dist import HashedDistHandler
from env import IMG_ROOT_PATH, PDF_ROOT_PATH, VIDEO_ROOT_PATH
from PIL import Image
import cv2
import numpy as np

CURRENT_TEMPLATE_PATH = path.join(IMG_ROOT_PATH, 'cur_template.png')
NEXT_TEMPLATE_PATH = path.join(IMG_ROOT_PATH, 'next_template.png')

if __name__ == '__main__':
    hdh = HashedDistHandler()
    pages = convert_from_path(path.join(PDF_ROOT_PATH, 'sample.pdf'))
    video_idx = [0]
    slide_idx = 0
    pages[slide_idx].save(CURRENT_TEMPLATE_PATH, 'PNG')
    pages[slide_idx + 1].save(NEXT_TEMPLATE_PATH, 'PNG')
    
    vidcap = cv2.VideoCapture(path.join(VIDEO_ROOT_PATH, 'sample1.mov'))
    print(f'fps: {vidcap.get(cv2.CAP_PROP_FPS)}')
    print(f'total frame: {vidcap.get(cv2.CAP_PROP_FRAME_COUNT)}')
    
    while slide_idx < len(pages):
        if len(video_idx) != slide_idx:
            slide_idx += 1
            pages[slide_idx].save(CURRENT_TEMPLATE_PATH, 'PNG')
            pages[slide_idx + 1].save(NEXT_TEMPLATE_PATH, 'PNG')
        
        success, frame = vidcap.read()
        print(vidcap.get(cv2.CAP_PROP_POS_FRAMES))
        if not success: break
        target = Image.fromarray(np.uint8(frame))
        cur_template = Image.fromarray(np.uint8(cv2.imread(CURRENT_TEMPLATE_PATH)))
        next_template = Image.fromarray(np.uint8(cv2.imread(NEXT_TEMPLATE_PATH)))
        if hdh.calcHammingDist(target, next_template) < hdh.calcHammingDist(target, cur_template):
            video_idx.append(vidcap.get(cv2.CAP_PROP_POS_FRAMES))
            print(f'idx is now {len(video_idx)}')
        print(f'Dist {len(video_idx) - 1}: {hdh.calcHammingDist(target, cur_template)}, {len(video_idx)}: {hdh.calcHammingDist(target, next_template)}')

    print(video_idx)
