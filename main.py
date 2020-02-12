import pyglet

VIDEO_PATH = './videos/sample.mp4'

class VideoHandler(object):
    def __init__(self):
        self.window = pyglet.window.Window()
        self.player = pyglet.media.Player()
        self.source = pyglet.media.StreamingSource()
    
    def mediaLoadAndStart(self):
        self.media_load = pyglet.media.load(VIDEO_PATH)
        self.player.queue(self.media_load)
        self.player.play()
        
        @self.window.event
        def on_draw():
            if self.player.source and self.player.source.video_format:
                self.player.get_texture().blit(100, 100)

        pyglet.app.run()

if __name__ == '__main__':
    vh = VideoHandler()
    vh.mediaLoadAndStart()
