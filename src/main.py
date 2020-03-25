import json
from hashed_dist import HashedDistHandler
from youtube_ping import YoutubePing
from download_video import VideoHandler
from env import IMG_ROOT_PATH, VIDEO_ROOT_PATH, SAMPLE_IMG_ROOT_PATH, SAMPLE_JSON_ROOT_PATH
from PIL import Image
from os import path
import cv2
import pafy
import numpy as np

ref = {}
IMG_PATH = path.join(SAMPLE_IMG_ROOT_PATH, '{}{}.png')

if __name__ == '__main__':
    youtube_url = input('Input youtube url which begins with https://www.youtube.com/ : ')
    #youtube_url = 'https://www.youtube.com/watch?v=le1NvGzDWDk&feature=youtu.be&t=1168'
    youtube_url = 'https://www.youtube.com/watch?v=0E00Zuayv9Q'
    yp = YoutubePing(youtube_url)
    if not yp.isValidUrl:
        print('Url you inputted is not valid.')
        exit()

    vh = VideoHandler(youtube_url)
    vh.execute()
    video_name = vh.getVideoName()
    video_path = path.join(VIDEO_ROOT_PATH, video_name)

    hdh = HashedDistHandler()
    vidcap = cv2.VideoCapture(video_path)

    while True:
        success, cur_frame = vidcap.read()
        if not success:
            break
        
        frame = Image.fromarray(np.uint8(cur_frame))
        if vidcap.get(cv2.CAP_PROP_POS_FRAMES) == 1:
            hdh.setFrame(frame)
            ref[vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS)] = hdh.getEncodedHash()
            cv2.imwrite(IMG_PATH.format(video_name, len(ref) - 1), cur_frame)
            continue
        
        if not hdh.isSameFrame(frame):
            #print(vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS))
            hdh.setFrame(frame)
            ref[vidcap.get(cv2.CAP_PROP_POS_FRAMES) / vidcap.get(cv2.CAP_PROP_FPS)] = hdh.getEncodedHash()
            cv2.imwrite(IMG_PATH.format(video_name, len(ref) - 1), cur_frame)

    with open(path.join(SAMPLE_JSON_ROOT_PATH, f'{video_name}.json'), 'w') as f:
        json.dump(ref, f)

    with open(path.join(SAMPLE_JSON_ROOT_PATH, f'{video_name}_length.json'), 'w') as f:
        json.dump({'length': len(ref)}, f)
