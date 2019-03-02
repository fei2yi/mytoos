import asyncio
from aiohttp import web
import pymysql

host = '47.95.249.180'
user = 'yangfei'
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

rst = select('spider_record.mlr_land_supply', one=True, cursor=cursor)
mlr_land_supply_lid = rst['lid']

conn.close()
cursor.close()


async def wanfang(request):
    global v
    v += 1
    print('wanfang', v)
    return web.Response(body='{}'.format(v))


async def mohurd(request):
    global mo
    mo += 1
    print('zhijianbu', mo)
    return web.Response(body='{}'.format(mo))

async def tudijieguo(request):
    global mlr_land_supply_lid
    mlr_land_supply_lid += 1
    print('mlr_land_supply', mlr_land_supply_lid)
    return web.Response(body='{}'.format(mlr_land_supply_lid))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/wanfang', wanfang)
    app.router.add_route('GET', '/mohurd', mohurd)
    app.router.add_route('GET', '/tudijieguo', tudijieguo)
    await loop.create_server(app.make_handler(), '127.0.0.1', 9000)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
