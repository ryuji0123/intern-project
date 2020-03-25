import requests

class YoutubePing(object):
    def __init__(self, url):
        self.url = url
        self.doRequest(self.url)

    def isValidUrl(self):
        return self.response.status_code == 200

    def doRequest(self, url):
        self.response = requests.get(url)