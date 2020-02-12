from pdf2image import convert_from_path
from os import path
from calc_sim import SimilarityHandler
from img_find import ImgFindHandler
from env import IMG_ROOT_PATH, PDF_ROOT_PATH, VIDEO_ROOT_PATH
import cv2
import numpy as np

TEMPLATE_PATH = path.join(IMG_ROOT_PATH, 'template.png')

if __name__ == '__main__':
    sh = SimilarityHandler()
    ifh = ImgFindHandler()
    pages = convert_from_path(path.join(PDF_ROOT_PATH, 'sample.pdf'))
    for idx, page in enumerate(pages):
        page.save(TEMPLATE_PATH, 'PNG')
        matched_ones = {}
        
        
        vidcap= cv2.VideoCapture(path.join(VIDEO_ROOT_PATH, 'sample2.mp4'))
        template = cv2.imread(TEMPLATE_PATH)
        print(f'frame rate: {vidcap.get(5)}')

        while True:
            success, frame = vidcap.read()
            if not success: 
                print(f'slide {idx} not found')
                break
            res = ifh.isDetected(frame, template, 0.7)
            #if not len(res[0]): 
            #    continue
            print(f'slide{idx}: {vidcap.get(cv2.CAP_PROP_POS_FRAMES)}')
            break
    #for i in range(len(pages)):
    #    best_score = float('inf')
    #    idx = 0
    #    for j in range(len(pages)):
    #        im1, im2 = np.asarray(pages[i]), np.asarray(pages[j])
    #        sim_score = sh.calcEuclidDistance(im1, im2)
    #        if sim_score < best_score:
    #            best_score = sim_score
    #            idx = j

    #    matched_ones[idx] = best_score

    #print(matched_ones)
