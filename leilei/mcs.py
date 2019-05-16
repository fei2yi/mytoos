import requests, json
from io import BytesIO
from PIL import Image, ImageEnhance
import base64

image_url = 'http://neris.csrc.gov.cn/shixinchaxun/login/ycode.do'
headers = {'Host': 'neris.csrc.gov.cn',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
image = requests.get(image_url, headers=headers, timeout=3)


def getByte(img):
    img_byte = base64.b64encode(img)
    img_str = img_byte.decode('ascii')
    return img_str


img_str = getByte(image.content)
print(img_str)
data = {'img': img_str}
json_mod = json.dumps(data)
res = requests.post('http://127.0.0.1:8001/zqsx', data=json_mod)
print(1)
