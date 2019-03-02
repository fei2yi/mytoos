from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype
import random

text = '7QY29'
imgsize = (90, 25)
background = (255, 255, 255)
color = (0, 0, 0)
font = "C:\Windows\Fonts\simsun.ttc"
font_size = 18
imgmode = 'RGB'

table = []
for i in range(256):
    table.append(i * 256)

ttfont = truetype(font, font_size)  # 这里我之前使用Arial.ttf时不能打出中文，用华文细黑就可以
image = Image.new(imgmode, imgsize, background)
draw = Draw(image)


def _draw_character(c):
    w, h = draw.textsize(c, font=ttfont)

    dx = 0
    dy = 0
    im = Image.new(imgmode, (w + dx, h + dy),background)
    Draw(im).text((dx, dy), c, font=ttfont, fill=color)

    # rotate
    im = im.crop(im.getbbox())
    im = im.rotate(random.uniform(-30, 30), Image.BILINEAR, expand=1)

    return im


images = []
for c in text:
    images.append(_draw_character(c))
#
text_width = sum([im.size[0] for im in images])

width = max(text_width, imgsize[0])
# image = image.resize((width, imgsize[1]))

average = int(text_width / len(text))
rand = int(0.25 * average)
offset = int(average * 0.1)
#
for im in images:
    w, h = im.size
    if offset < 10:
        offset = 10
    image.paste(im, (offset, int((imgsize[1] - h) / 2)))
    offset = offset + w + random.randint(-rand, 0)

# draw.text((10, 2), text, fill=color, font=ttfont)

image.save('out5.png')