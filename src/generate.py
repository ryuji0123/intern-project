import json
from hashed_dist import HashedDistHandler
from env import IMG_ROOT_PATH, VIDEO_ROOT_PATH, YOUTUBE_BASE_PATH, SAMPLE_IMG_ROOT_PATH
from PIL import Image
from os import path
import cv2
import pafy
import numpy as np

ref = {}
SAMPLE_VIDEO_PATH = path.join(YOUTUBE_BASE_PATH, 'ZMcD_4w3Wyw')
IMG_PATH = path.join(SAMPLE_IMG_ROOT_PATH, 'sample{}.png')

if __name__ == '__main__':
    vPafy = pafy.new(SAMPLE_VIDEO_PATH)
    play = vPafy.getbest(preftype='mp4')
    hdh = HashedDistHandler()
    vidcap = cv2.VideoCapture(play.url)

    while True:
        success, cur_frame = vidcap.read()
        if not success: break
        
        frame = Image.fromarray(np.uint8(cur_frame))
        if vidcap.get(cv2.CAP_PROP_POS_FRAMES) == 1:
            hdh.setFrame(frame)
            ref[vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS)] = hdh.getEncodedHash()
            cv2.imwrite(IMG_PATH.format(len(ref) - 1), cur_frame)
            continue
        
        if not hdh.isSameFrame(frame):
            print(vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS))
            hdh.setFrame(frame)
            ref[vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS)] = hdh.getEncodedHash()
            cv2.imwrite(IMG_PATH.format(len(ref) - 1), cur_frame)

    print(ref)
    print(len(ref))
    with open('../public/json/nnsample.json', 'w') as f:
        json.dump(ref, f)

    with open('../public/json/length.json', 'w') as f:
        json.dump({'length': len(ref)}, f)
