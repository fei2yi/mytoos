import random, requests, time
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
s = requests.session()
num = 5250


def get_name():
    global num
    num += 1
    print(num)
    return num

def pic_to(im):
    shu = im.load()
    cl = True
    if cl:
        for x in range(0, 1):  # 从左边找到入口，从这个入口处向右边消，x=[0,1]
            for y in range(0, im.size[1] - 1):
                if shu[x, y] == 255:
                    pass
                elif shu[x, y] == 0 and im.load()[x, y + 1] == 255 and im.load()[x, y - 1] == 255:  # 入口黑，上下白

                    for z in range(x, im.size[0]):
                        if shu[z, y] == 255:
                            break
                        if shu[z, y] == 0 and im.load()[z, y + 1] == 255:  # 从入口进去，口黑and上黑and下黑
                            im.putpixel((z, y), 255)
                        if shu[z, y] == 0 and im.load()[z, y - 1] == 255:
                            im.putpixel((z, y), 255)
        for x in range(im.size[0] - 1, im.size[0]):  # 从右边找入口，从入口处向左边消 x=[最大，最大-1]
            for y in range(0, im.size[1] - 1):
                if shu[x, y] == 255:
                    pass
                elif shu[x, y] == 0:  # 入口黑， 向前走

                    for z in range(im.size[0] - 1, 0, -1):
                        if shu[z, y] == 255:
                            break
                        if shu[z, y] == 0 and shu[z, y + 1] == 255:  # 从入口进去，口黑and上黑and下黑
                            im.putpixel((z, y), 255)
                        if shu[z, y] == 0 and shu[z, y - 1] == 255:
                            im.putpixel((z, y), 255)
        for x in range(0, im.size[0]):  # 从左边开始向右边扫，x=[0,最大]
            for y in range(1, im.size[1] - 1):
                if shu[x, y] == 255:
                    pass
                elif shu[x, y] == 0 and shu[x, y + 1] == 255 and shu[x, y - 1] == 255 and shu[x - 1, y] == 255:
                    # 入口黑，上下白and前白

                    for z in range(x, im.size[0]):
                        if shu[z, y] == 255:
                            break
                        if shu[z, y] == 0 and shu[z, y + 1] == 255 and shu[z, y - 1] == 255:  # 入口黑，上下白
                            im.putpixel((z, y), 255)
        for x in range(im.size[0] - 1, 0, -1):  # 从右边向左边扫，x=[最大，0]
            for y in range(1, im.size[1] - 1):
                if shu[x, y] == 255:
                    pass
                elif shu[x, y] == 0 and shu[x, y + 1] == 255 and shu[x, y - 1] == 255 and shu[
                            x + 1, y] == 255:  # 入口黑，上下前白
                    for z in range(x, 0, -1):
                        if shu[z, y] == 255:
                            break
                        if shu[z, y] == 0 and shu[z, y + 1] == 255 and shu[z, y - 1] == 255:  # 入口黑，上下白
                            im.putpixel((z, y), 255)

    return im


while True:
    image_url = 'http://neris.csrc.gov.cn/shixinchaxun/login/ycode.do'
    ip = iplist[random.randint(0, len(iplist)) - 1]
    proxies = {'http': "http://" + ip, "https": "http://" + ip}
    headers = {'Host': 'neris.csrc.gov.cn',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    try:
        image = s.get(image_url, headers=headers, proxies=proxies, timeout=3)
        im = Image.open(BytesIO(image.content))


        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        for x in range(width):
            for y in range(height):
                r, g, b = pix[x, y]
                # if r + g + b >= 450:
                #     im.putpixel((x, y), (255, 255, 255))

                r0, r1, r2 = r, g, b
                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))

                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))
                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))
                # if pix[x, y] != 0:
                #     pix[x, y] = 255
                # elif r + g + b <= 150:
                #     im.putpixel((x, y), (0, 0, 0))
                # else:
                #     im.putpixel((x, y), (255, 255, 255))
        im.save('out.jpg')
        im.save('E:\chromedownload\\font1715\out0.jpg')
        # im.save('out.jpg')
        path = 'E:\data\pic'

        break
    except Exception as e:
        time.sleep(0.5)
        continue
