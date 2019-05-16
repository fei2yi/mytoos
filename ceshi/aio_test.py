import asyncio
from aiohttp import web
import pymysql

host = 'localhost'
user = 'root'
password = 'Elements123'
db = 'spider_record'
conn = pymysql.connect(host='{}'.format(host), port=3306, user='{}'.format(user),
                       password='{}'.format(password), db='{}'.format(db), charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


def select(tablename, key=None, value=None, term=None, v='*', one=False, cursor=None):
    if term:
        sql = 'select {} from {} where {}'.format(v, tablename, term)
    elif key and value:
        sql = 'select {} from {} where {}="{}"'.format(v, tablename, key, value)
    else:
        sql = 'select {} from {}'.format(v, tablename)
    cursor.execute(sql)
    if one:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    return result


rst = select('spider_record.dataplus_patent', one=True, cursor=cursor)
v = rst['pid']

rst = select('spider_record.mohurd_jzsc_person', one=True, cursor=cursor)
mo = rst['pid']

conn.close()
cursor.close()


async def index(request):
    global v
    v += 1
    print('wanfang', v)
    return web.Response(body='{}'.format(v))


async def mohurd(request):
    global mo
    mo += 1
    print('zhijianbu', mo)
    return web.Response(body='{}'.format(mo))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/index', index)
    app.router.add_route('GET', '/mohurd', mohurd)
    await loop.create_server(app.make_handler(), '127.0.0.1', 9000)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
