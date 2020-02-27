import imagehash

class HashedDistHandler(object):
    def calcHammingDist(self, target, img):
        return imagehash.average_hash(target) - imagehash.average_hash(img)

    def setFrame(self, frame):
        self.frame = frame

    def getEncodedHash(self):
        return str(imagehash.average_hash(self.frame))

    def isSameFrame(self, frame):
        return imagehash.average_hash(frame) == imagehash.average_hash(self.frame)
