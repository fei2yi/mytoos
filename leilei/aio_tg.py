import asyncio
from aiohttp import web
import json
from io import BytesIO
from PIL import Image, ImageEnhance
import base64

async def zqsx(request):
    info = await request.text()
    info = json.loads(info)
    img = info['img']
    img_byte = base64.b64decode(img)
    print(img_byte)
    return web.Response(body='{}'.format(fileName))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('POST', '/zqsx', zqsx)
    await loop.create_server(app.make_handler(), '127.0.0.1', 8001)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
