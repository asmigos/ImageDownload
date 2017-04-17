import random
import urllib


def web_image_download(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".png"
    urllib.urlretrieve(url, fullname)

web_image_download("https://ee5817f8e2e9a2e34042-3365e7f0719651e5b8d0979bce83c558.ssl.cf5.rackcdn.com/python.png")