from io import BytesIO
import numpy as np
from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt

image = ImageCaptcha(width=450, height=125, fonts=['C:\Windows\Fonts\simsun.ttc'], font_sizes=(85, 85))



captcha_text = '2QY29'
data = image.generate_image(captcha_text)

im = data
pix = im.load()
width = im.size[0]
height = im.size[1]
# for x in range(width):
#     for y in range(height):
#         r, g, b = pix[x, y]
#         if r + g + b >= 700 :
#             im.putpixel((x, y), (255, 255, 255))
#         else:
#             im.putpixel((x, y), (0, 0, 0))

# im=im.resize((90,25))
im.save('out4.png')
# # assert isinstance(data, BytesIO)
# f = plt.figure()
# ax = f.add_subplot(111)
# ax.text(0.1, 0.9, '', ha='center', va='center', transform=ax.transAxes)
# plt.imshow(im)
# plt.show()
