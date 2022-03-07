import random
import urllib.request

url = "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg"


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = "download_an_image/" + str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image(url)