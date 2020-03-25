import pafy
import logging
from os import path
from env import SAMPLE_JSON_ROOT_PATH, VIDEO_ROOT_PATH, LOG_ROOT_PATH

from db_handler import SqliteHandler

VIDEO_LOG_FILE_PATH = path.join(LOG_ROOT_PATH, 'video_error.log')

class VideoHandler(object):
    def __init__(self, url):
        self.url = url
        self.initLogger()
        self.initSqliteHandler()

    def initLogger(self):
        fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
        logging.basicConfig(level=logging.DEBUG, format=fmt)
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler(VIDEO_LOG_FILE_PATH)
        self.logger.addHandler(fh)

    def dumpError(self, err, logger):
        logger.exception(f'Exception during downloading and registering videos: {err}')

    def initSqliteHandler(self):
        self.db_handler = SqliteHandler()

    def execute(self):
        self.video = pafy.new(self.url)
        self.stream = self.video.getbest(preftype='mp4')
        self.video_name = self.stream.filename

        if self.isAlreadyRegistered(self.db_handler, self.url):
            pass
        try:
            self.downloadVideo(self.stream, VIDEO_ROOT_PATH)
            self.registerVideo(self.db_handler, self.url, self.video_name)
            print('Video was registered')
        except Exception as e:
            self.dumpError(e, self.logger)
            return
        finally:
            self.db_handler.close()

    def downloadVideo(self, stream, url):
        stream.download(filepath=url)

    def getVideoName(self):
        return self.video_name

    def isAlreadyRegistered(self, db_handler, url):
        return db_handler.isAlreadyRegistered(url=url)

    def registerVideo(self, db_handler, url, video_name):
        db_handler.registerVideo(url, video_name)


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=0E00Zuayv9Q'
    url = 'https://www.youtube.com/watch?v=le1NvGzDWDk&feature=youtu.be&t=1168'
    vh = VideoHandler(url=url)
