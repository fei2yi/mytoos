from io import BytesIO
import numpy as np
from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt

image = ImageCaptcha(width=360, height=100, fonts=['C:\Windows\Fonts\simsun.ttc'], font_sizes=(65, 65))



captcha_text = 'MHSBU'
data = image.generate_image(captcha_text)

im = data
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        if r + g + b >= 749 :
            im.putpixel((x, y), (255, 255, 255))
        else:
            im.putpixel((x, y), (0, 0, 0))

# assert isinstance(data, BytesIO)
f = plt.figure()
ax = f.add_subplot(111)
ax.text(0.1, 0.9, '', ha='center', va='center', transform=ax.transAxes)
plt.imshow(im)
plt.show()
