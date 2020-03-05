import scipy.spatial.distance as dist
import cv2
from os import path
from env import IMG_ROOT_PATH

class SimilarityHandler(object):
    def __init__(self, im1_filename='', im2_filename=''):
        self.im1 = cv2.imread(path.join(IMG_ROOT_PATH, im1_filename))
        self.im2 = cv2.imread(path.join(IMG_ROOT_PATH, im2_filename))

    def calcEuclidDistance(self, im1, im2):
        return dist.euclidean(im1.flatten(), im2.flatten())
