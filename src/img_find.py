import cv2
import numpy as np

class ImgFindHandler(object):
    def isDetected(self, frame, template, threshold):
        grayed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        return np.where(cv2.matchTemplate(grayed_frame, template, cv2.TM_CCOEFF_NORMED) >= threshold)
