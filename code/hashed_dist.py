import imagehash

class HashedDistHandler(object):
    def calcHammingDist(self, target, img):
        return imagehash.average_hash(target) - imagehash.average_hash(img)
