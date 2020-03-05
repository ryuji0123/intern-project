import imagehash

class HashedDistHandler(object):
    def calcHammingDist(self, target, img):
        return abs(self.selectedHash(target) - self.selectedHash(img))

    def calcHammingDistBetweenImageAndHash(self, target, img):
        return imagehash.hex_to_hash(target) - self.selectedHash(img)

    def setFrame(self, frame):
        self.frame = frame

    def getEncodedHash(self):
        return str(self.selectedHash(self.frame))

    def isSameFrame(self, frame):
        return abs(self.selectedHash(frame) - self.selectedHash(self.frame)) < 2

    def selectedHash(self, img):
        return imagehash.average_hash(img)
