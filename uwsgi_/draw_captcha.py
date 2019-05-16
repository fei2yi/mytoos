from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype
import random

ALPHABET = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

imgsize = (90, 25)
background = (255, 255, 255)
background_RGBA = (255, 255, 255, 0)
color = (0, 0, 0)
font = "C:\Windows\Fonts\simsun.ttc"
font_size = 18
imgmode = 'RGB'
imgmode_RGBA = 'RGBA'


def create_noise_curve(image, color):
    w, h = image.size
    x1 = random.randint(0, int(w / 5))
    x2 = random.randint(w - int(w / 5), w)
    y1 = random.randint(int(h / 5), h - int(h / 5))
    y2 = random.randint(y1, h - int(h / 5))
    points = [x1, y1, x2, y2]
    end = random.randint(160, 200)
    start = random.randint(0, 20)
    Draw(image).arc(points, start, end, fill=color)
    return image


def _draw_character(c, draw, ttfont):
    w, h = draw.textsize(c, font=ttfont)

    dx = 0
    dy = 0
    im = Image.new(imgmode_RGBA, (w + dx, h + dy), background_RGBA)
    Draw(im).text((dx, dy), c, font=ttfont, fill=color)

    # rotate
    im = im.crop(im.getbbox())
    im = im.rotate(random.uniform(-30, 30), expand=1, fillcolor=background)

    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            r, g, b, a = pix[x, y]
            if a == 0:
                im.putpixel((x, y), (255, 255, 255, 255))
            # elif 200>a>0:
            #     im.putpixel((x, y), (r, g, b, a))
            else:
                # im.putpixel((x, y), (0, 0, 0, 0))
                r0, r1, r2 = r, g, b
                if r0 + r1 + r2 > 760:
                    pass
                else:
                    im.putpixel((x, y), (0, 0, 0, 255))
    return im


def make_pic(text):
    ttfont = truetype(font, font_size)  # 这里我之前使用Arial.ttf时不能打出中文，用华文细黑就可以
    image = Image.new(imgmode, imgsize, background)
    draw = Draw(image)

    images = []
    for c in text:
        images.append(_draw_character(c, draw, ttfont))
    #
    text_width = sum([im.size[0] for im in images])

    # width = max(text_width, imgsize[0])
    # image = image.resize((width, imgsize[1]))

    average = int(text_width / len(text))
    rand = int(0.25 * average)
    offset = int(average * 0.1)
    #

    for im in images:
        w, h = im.size
        if offset < 10:
            offset = 10

        offseth = int((imgsize[1] - h) / 2) + random.randint(-4, 4)

        image.paste(im, (offset, offseth))
        offset = offset + w + random.randint(-rand, 0)

    # create_noise_curve(image, color)
    # draw.text((10, 2), text, fill=color, font=ttfont)

    image.save('out5.png')


if __name__ == '__main__':
    ALPHABET_len = len(ALPHABET)
    text = ''
    for i in range(5):
        rd=random.randint(0, ALPHABET_len-1)
        print(rd)
        text += ALPHABET[rd]
    make_pic(text)
