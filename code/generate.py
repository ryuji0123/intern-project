import json
from hashed_dist import HashedDistHandler
from env import IMG_ROOT_PATH, VIDEO_ROOT_PATH
from PIL import Image
from os import path
import cv2
import numpy as np

ref = {}

if __name__ == '__main__':
    hdh = HashedDistHandler()
    vidcap = cv2.VideoCapture(path.join(VIDEO_ROOT_PATH, 'sample1.mov'))

    while True:
        success, frame = vidcap.read()
        if not success: break
        
        frame = Image.fromarray(np.uint8(frame))
        if vidcap.get(cv2.CAP_PROP_POS_FRAMES) == 1:
            hdh.setFrame(frame)
            ref[vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS)] = hdh.getEncodedHash()
            continue
        
        if not hdh.isSameFrame(frame):
            print(vidcap.get(cv2.CAP_PROP_POS_FRAMES))
            hdh.setFrame(frame)
            ref[vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS)] = hdh.getEncodedHash()
        
    print(ref)
    with open('../public/json/nsample.json', 'w') as f:
        json.dump(ref, f)
