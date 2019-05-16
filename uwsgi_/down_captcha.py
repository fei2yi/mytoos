import random, requests, time
from io import BytesIO
from PIL import Image, ImageEnhance
from uwsgi_ import aliyunOss
iplist = [
    '134.175.187.209:8089',
    '118.89.44.219:8089',
    '140.143.140.196:8089',
    '140.143.33.121:8089',
    '129.28.68.157:8089',
    '132.232.45.158:8089',
    '94.191.9.189:8089',
    '94.191.4.160:8089',
    '115.159.209.40:8089',
    '118.89.156.161:8089',
]
s = requests.session()
num = 102
image_url = 'http://neris.csrc.gov.cn/shixinchaxun/login/ycode.do'
path = 'E:\data\zqsx'


def get_name():
    global num
    num += 1
    print(num)
    return num


for ii in range(5):
    ip = iplist[random.randint(0, len(iplist)) - 1]
    proxies = {'http': "http://" + ip, "https": "http://" + ip}
    headers = {'Host': 'neris.csrc.gov.cn',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    try:
        image = s.get(image_url, headers=headers, proxies=proxies, timeout=3)

        bucket = aliyunOss.get_bucket()

        bucket.put_object('report/201903/out5.png', image.content)

        im = Image.open(BytesIO(image.content))

        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        for x in range(width):
            for y in range(height):
                r, g, b = pix[x, y]
                r0, r1, r2 = r, g, b
                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))
                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))
                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))

        name = get_name()
        im.save('{}\{}_{}.png'.format(path, name, name))

    except Exception as e:
        time.sleep(0.5)
        print(111)
        continue
