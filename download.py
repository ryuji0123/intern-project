from pytube import YouTube

EXT = 'mp4'

def download(url):
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download('./videos')

if __name__ == '__main__':
    url = input('url >> ')
    download(url)
