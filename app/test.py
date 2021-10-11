import base64
import requests


def get_as_base64(url):

    return base64.b64encode(requests.get(url).content)

if __name__ == '__main__':
    urls="https://s.isanook.com/ca/0/ui/279/1396205/download20190701165129_1562561119.jpg"
    imageTobase64=get_as_base64(url=urls)
    print(imageTobase64)