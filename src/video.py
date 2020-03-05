import cv2
import pafy
from os import path
from env import YOUTUBE_BASE_PATH

SAMPLE_VIDEO_PATH = path.join(YOUTUBE_BASE_PATH, 'ZMcD_4w3Wyw')

if __name__ == '__main__':
    vPafy = pafy.new(SAMPLE_VIDEO_PATH)
    play = vPafy.getbest(preftype='mp4')

    cap = cv2.VideoCapture(play.url)
    while True:
        ret, frame = cap.read()
        if not ret: break

    cap.release()
    cv2.destroyAllWindows()