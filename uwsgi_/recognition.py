# -*- coding: utf-8 -*-
import re
import time
import requests
import pytesseract
import random
from lxml import etree
from io import BytesIO
from PIL import Image, ImageEnhance

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


class inquiry(object):
    table = []
    threshold = 85
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    def sum_9_region(self, img, x, y):  # 去除图片中孤点
        cur_pixel = img.getpixel((x, y))  # 当前像素点的值
        width = img.width
        height = img.height

        if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
            return 0

        if y == 0:  # 第一行
            if x == 0:  # 左上顶点,4邻域
                # 中心点旁边3个点
                sum = cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))
                return 4 - sum
            elif x == width - 1:  # 右上顶点
                sum = cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1))

                return 4 - sum
            else:  # 最上非顶点,6邻域
                sum = img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))
                return 6 - sum
        elif y == height - 1:  # 最下面一行
            if x == 0:  # 左下顶点
                # 中心点旁边3个点
                sum = cur_pixel \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y - 1)) \
                      + img.getpixel((x, y - 1))
                return 4 - sum
            elif x == width - 1:  # 右下顶点
                sum = cur_pixel \
                      + img.getpixel((x, y - 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y - 1))

                return 4 - sum
            else:  # 最下非顶点,6邻域
                sum = cur_pixel \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x, y - 1)) \
                      + img.getpixel((x - 1, y - 1)) \
                      + img.getpixel((x + 1, y - 1))
                return 6 - sum
        else:  # y不在边界
            if x == 0:  # 左边非顶点
                sum = img.getpixel((x, y - 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y - 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))

                return 6 - sum
            elif x == width - 1:  # 右边非顶点
                # print('%s,%s' % (x, y))
                sum = img.getpixel((x, y - 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x - 1, y - 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1))

                return 6 - sum
            else:  # 具备9领域条件的
                sum = img.getpixel((x - 1, y - 1)) \
                      + img.getpixel((x - 1, y)) \
                      + img.getpixel((x - 1, y + 1)) \
                      + img.getpixel((x, y - 1)) \
                      + cur_pixel \
                      + img.getpixel((x, y + 1)) \
                      + img.getpixel((x + 1, y - 1)) \
                      + img.getpixel((x + 1, y)) \
                      + img.getpixel((x + 1, y + 1))
                return 9 - sum

    def parse_image(self, image):
        try:
            im = Image.open(BytesIO(image.content))
        except:
            return ''
        # im.save('tuna.jpg', 'jpeg')
        # im = Image.open('tuna.jpg')
        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        for x in range(width):
            for y in range(height):
                r, g, b = pix[x, y]
                if r + g + b >= 300 or r >= 150 or g >= 150 or b >= 150:
                    im.putpixel((x, y), (255, 255, 255))
        im = ImageEnhance.Sharpness(im).enhance(2.5)  # 图像锐化处理
        imgry = im.convert('L')  # 图像灰化

        im=im.crop((12, 3, 78, 22))

        im.save('out.jpg')
        # imgry.save('gtuna.jpg')
        imgbz = imgry.point(self.table, '1')  # 转二值图
        # imgbz.save('btuna.jpg')
        for x in range(width):
            for y in range(height):
                insula = self.sum_9_region(imgbz, x, y)
                if insula <= 2:
                    imgbz.putpixel((x, y), 1)

        # imgbz.save('out.jpg')
        auth = pytesseract.image_to_string(imgbz, config="-psm 7").replace(' ', '')
        m = re.compile(r'\W*', re.L)
        auth = m.sub('', auth)
        return auth

    def csrc(self, name, cardnum):

        image_url = 'http://neris.csrc.gov.cn/shixinchaxun/login/ycode.do'
        url = 'http://neris.csrc.gov.cn/shixinchaxun/honestyObj/query.do'
        form_data = {'randSesion': 'f08f0786362c43f1aa257cdfd99fdb35',
                     'realCardNumber': ''}
        form_data['objName'] = name
        form_data['realCardNumber'] = cardnum
        s = requests.session()
        headers = {'Host': 'neris.csrc.gov.cn',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

        while True:
            ip = iplist[random.randint(0, len(iplist)) - 1]
            proxies = {'http': "http://" + ip, "https": "http://" + ip}
            try:
                image = s.get(image_url, headers=headers, proxies=proxies, timeout=3)
            except:
                time.sleep(0.5)
                continue
            auth = self.parse_image(image)
            form_data['ycode'] = auth
            # print auth
            try:
                html = s.post(url, data=form_data, headers=headers, proxies=proxies, timeout=3)
            except:
                time.sleep(0.5)
                continue
            if html.status_code == 200:
                selector = etree.HTML(html.content)
                judge = selector.xpath(".//form[@id='list_form']/table/tr[1]/td/table/tr[3]/td[4]/text()")
                if judge:
                    time.sleep(0.15)
                    continue
                else:
                    if selector.xpath("//*[@id='sorttab2']/tbody/tr/td/font"):
                        return []
                    cods = selector.xpath("//*[@id='sorttab2']/tbody/tr")
                    fishing_net = []
                    for cod in cods:
                        fish = cod.xpath(".//td/text()")
                        fish = map(lambda x: x.strip(), fish)
                        fish.append('http://neris.csrc.gov.cn' + cod.xpath(".//td/a/@href")[0])
                        fishing_net.append(fish)
                    return fishing_net
            else:
                time.sleep(0.3)


quiry = inquiry()
data = quiry.csrc('张磊', '')