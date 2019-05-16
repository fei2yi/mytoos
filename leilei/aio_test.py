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

rst = select('spider_record.conmom_record', cursor=cursor)

bianliang1 = int(rst[0]['pid'])
bianliang2 = int(rst[1]['pid'])
bianliang3 = int(rst[2]['pid'])
bianliang4 = int(rst[3]['pid'])
bianliang5 = int(rst[4]['pid'])
bianliang6 = int(rst[5]['pid'])
bianliang7 = int(rst[6]['pid'])
bianliang8 = int(rst[7]['pid'])
bianliang9 = int(rst[8]['pid'])
bianliang10 = int(rst[9]['pid'])
bianliang11 = int(rst[10]['pid'])
bianliang12 = int(rst[11]['pid'])
bianliang13 = int(rst[12]['pid'])
bianliang14 = int(rst[13]['pid'])
bianliang15 = int(rst[14]['pid'])
bianliang16 = int(rst[15]['pid'])
bianliang17 = int(rst[16]['pid'])
bianliang18 = int(rst[17]['pid'])
bianliang19 = int(rst[18]['pid'])
bianliang20 = int(rst[19]['pid'])
bianliang21 = int(rst[20]['pid'])
bianliang22 = int(rst[21]['pid'])
bianliang23 = int(rst[22]['pid'])
bianliang24 = int(rst[23]['pid'])
bianliang25 = int(rst[24]['pid'])
bianliang26 = int(rst[25]['pid'])
bianliang27 = int(rst[26]['pid'])
bianliang28 = int(rst[27]['pid'])
bianliang29 = int(rst[28]['pid'])
bianliang30 = int(rst[29]['pid'])
bianliang31 = int(rst[30]['pid'])
bianliang32 = int(rst[31]['pid'])
bianliang33 = int(rst[32]['pid'])
bianliang34 = int(rst[33]['pid'])
bianliang35 = int(rst[34]['pid'])
bianliang36 = int(rst[35]['pid'])
bianliang37 = int(rst[36]['pid'])
bianliang38 = int(rst[37]['pid'])
bianliang39 = int(rst[38]['pid'])
bianliang40 = int(rst[39]['pid'])
bianliang41 = int(rst[40]['pid'])
bianliang42 = int(rst[41]['pid'])
bianliang43 = int(rst[42]['pid'])
bianliang44 = int(rst[43]['pid'])
bianliang45 = int(rst[44]['pid'])
bianliang46 = int(rst[45]['pid'])
bianliang47 = int(rst[46]['pid'])
bianliang48 = int(rst[47]['pid'])
bianliang49 = int(rst[48]['pid'])
bianliang50 = int(rst[49]['pid'])
bianliang51 = int(rst[50]['pid'])
bianliang52 = int(rst[51]['pid'])
bianliang53 = int(rst[52]['pid'])
bianliang54 = int(rst[53]['pid'])
bianliang55 = int(rst[54]['pid'])
bianliang56 = int(rst[55]['pid'])
bianliang57 = int(rst[56]['pid'])
bianliang58 = int(rst[57]['pid'])
bianliang59 = int(rst[58]['pid'])
bianliang60 = int(rst[59]['pid'])
bianliang61 = int(rst[60]['pid'])
bianliang62 = int(rst[61]['pid'])
bianliang63 = int(rst[62]['pid'])
bianliang64 = int(rst[63]['pid'])
bianliang65 = int(rst[64]['pid'])
bianliang66 = int(rst[65]['pid'])
bianliang67 = int(rst[66]['pid'])
bianliang68 = int(rst[67]['pid'])
bianliang69 = int(rst[68]['pid'])
bianliang70 = int(rst[69]['pid'])
bianliang71 = int(rst[70]['pid'])
bianliang72 = int(rst[71]['pid'])
bianliang73 = int(rst[72]['pid'])
bianliang74 = int(rst[73]['pid'])
bianliang75 = int(rst[74]['pid'])
bianliang76 = int(rst[75]['pid'])
bianliang77 = int(rst[76]['pid'])
bianliang78 = int(rst[77]['pid'])
bianliang79 = int(rst[78]['pid'])
bianliang80 = int(rst[79]['pid'])
bianliang81 = int(rst[80]['pid'])
bianliang82 = int(rst[81]['pid'])
bianliang83 = int(rst[82]['pid'])
bianliang84 = int(rst[83]['pid'])
bianliang85 = int(rst[84]['pid'])
bianliang86 = int(rst[85]['pid'])
bianliang87 = int(rst[86]['pid'])
bianliang88 = int(rst[87]['pid'])
bianliang89 = int(rst[88]['pid'])
bianliang90 = int(rst[89]['pid'])
bianliang91 = int(rst[90]['pid'])
bianliang92 = int(rst[91]['pid'])
bianliang93 = int(rst[92]['pid'])
bianliang94 = int(rst[93]['pid'])
bianliang95 = int(rst[94]['pid'])
bianliang96 = int(rst[95]['pid'])
bianliang97 = int(rst[96]['pid'])
bianliang98 = int(rst[97]['pid'])
bianliang99 = int(rst[98]['pid'])
bianliang100 = int(rst[99]['pid'])

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
    query_string = request.query_string
    if not query_string:
        global mlr_land_supply_lid
        mlr_land_supply_lid += 1
        print('mlr_land_supply', mlr_land_supply_lid)
        return web.Response(body='{}'.format(mlr_land_supply_lid))
    else:
        query_str = query_string.split('=')[-1]
        if query_str.isdigit():
            query_str = int(query_str)
            if query_str == 1:
                global bianliang1
                bianliang1 += 1
                print('bianliang1', bianliang1)
                return web.Response(body='{}'.format(bianliang1))
            elif query_str == 2:
                global bianliang2
                bianliang2 += 1
                print('bianliang2', bianliang2)
                return web.Response(body='{}'.format(bianliang2))
            elif query_str == 3:
                global bianliang3
                bianliang3 += 1
                print('bianliang3', bianliang3)
                return web.Response(body=str(bianliang3))
            elif query_str == 4:
                global bianliang4
                bianliang4 += 1
                print('bianliang4', bianliang4)
                return web.Response(body=str(bianliang4))
            elif query_str == 5:
                global bianliang5
                bianliang5 += 1
                print('bianliang5', bianliang5)
                return web.Response(body=str(bianliang5))
            elif query_str == 6:
                global bianliang6
                bianliang6 += 1
                print('bianliang6', bianliang6)
                return web.Response(body=str(bianliang6))
            elif query_str == 7:
                global bianliang7
                bianliang7 += 1
                print('bianliang7', bianliang7)
                return web.Response(body=str(bianliang7))
            elif query_str == 8:
                global bianliang8
                bianliang8 += 1
                print('bianliang8', bianliang8)
                return web.Response(body=str(bianliang8))
            elif query_str == 9:
                global bianliang9
                bianliang9 += 1
                print('bianliang9', bianliang9)
                return web.Response(body=str(bianliang9))
            elif query_str == 10:
                global bianliang10
                bianliang10 += 1
                print('bianliang10', bianliang10)
                return web.Response(body=str(bianliang10))
            elif query_str == 11:
                global bianliang11
                bianliang11 += 1
                print('bianliang11', bianliang11)
                return web.Response(body=str(bianliang11))
            elif query_str == 12:
                global bianliang12
                bianliang12 += 1
                print('bianliang12', bianliang12)
                return web.Response(body=str(bianliang12))
            elif query_str == 13:
                global bianliang13
                bianliang13 += 1
                print('bianliang13', bianliang13)
                return web.Response(body=str(bianliang13))
            elif query_str == 14:
                global bianliang14
                bianliang14 += 1
                print('bianliang14', bianliang14)
                return web.Response(body=str(bianliang14))
            elif query_str == 15:
                global bianliang15
                bianliang15 += 1
                print('bianliang15', bianliang15)
                return web.Response(body=str(bianliang15))
            elif query_str == 16:
                global bianliang16
                bianliang16 += 1
                print('bianliang16', bianliang16)
                return web.Response(body=str(bianliang16))
            elif query_str == 17:
                global bianliang17
                bianliang17 += 1
                print('bianliang17', bianliang17)
                return web.Response(body=str(bianliang17))
            elif query_str == 18:
                global bianliang18
                bianliang18 += 1
                print('bianliang18', bianliang18)
                return web.Response(body=str(bianliang18))
            elif query_str == 19:
                global bianliang19
                bianliang19 += 1
                print('bianliang19', bianliang19)
                return web.Response(body=str(bianliang19))
            elif query_str == 20:
                global bianliang20
                bianliang20 += 1
                print('bianliang20', bianliang20)
                return web.Response(body=str(bianliang20))
            elif query_str == 21:
                global bianliang21
                bianliang21 += 1
                print('bianliang21', bianliang21)
                return web.Response(body=str(bianliang21))
            elif query_str == 22:
                global bianliang22
                bianliang22 += 1
                print('bianliang22', bianliang22)
                return web.Response(body=str(bianliang22))
            elif query_str == 23:
                global bianliang23
                bianliang23 += 1
                print('bianliang23', bianliang23)
                return web.Response(body=str(bianliang23))
            elif query_str == 24:
                global bianliang24
                bianliang24 += 1
                print('bianliang24', bianliang24)
                return web.Response(body=str(bianliang24))
            elif query_str == 25:
                global bianliang25
                bianliang25 += 1
                print('bianliang25', bianliang25)
                return web.Response(body=str(bianliang25))
            elif query_str == 26:
                global bianliang26
                bianliang26 += 1
                print('bianliang26', bianliang26)
                return web.Response(body=str(bianliang26))
            elif query_str == 27:
                global bianliang27
                bianliang27 += 1
                print('bianliang27', bianliang27)
                return web.Response(body=str(bianliang27))
            elif query_str == 28:
                global bianliang28
                bianliang28 += 1
                print('bianliang28', bianliang28)
                return web.Response(body=str(bianliang28))
            elif query_str == 29:
                global bianliang29
                bianliang29 += 1
                print('bianliang29', bianliang29)
                return web.Response(body=str(bianliang29))
            elif query_str == 30:
                global bianliang30
                bianliang30 += 1
                print('bianliang30', bianliang30)
                return web.Response(body=str(bianliang30))
            elif query_str == 31:
                global bianliang31
                bianliang31 += 1
                print('bianliang31', bianliang31)
                return web.Response(body=str(bianliang31))
            elif query_str == 32:
                global bianliang32
                bianliang32 += 1
                print('bianliang32', bianliang32)
                return web.Response(body=str(bianliang32))
            elif query_str == 33:
                global bianliang33
                bianliang33 += 1
                print('bianliang33', bianliang33)
                return web.Response(body=str(bianliang33))
            elif query_str == 34:
                global bianliang34
                bianliang34 += 1
                print('bianliang34', bianliang34)
                return web.Response(body=str(bianliang34))
            elif query_str == 35:
                global bianliang35
                bianliang35 += 1
                print('bianliang35', bianliang35)
                return web.Response(body=str(bianliang35))
            elif query_str == 36:
                global bianliang36
                bianliang36 += 1
                print('bianliang36', bianliang36)
                return web.Response(body=str(bianliang36))
            elif query_str == 37:
                global bianliang37
                bianliang37 += 1
                print('bianliang37', bianliang37)
                return web.Response(body=str(bianliang37))
            elif query_str == 38:
                global bianliang38
                bianliang38 += 1
                print('bianliang38', bianliang38)
                return web.Response(body=str(bianliang38))
            elif query_str == 39:
                global bianliang39
                bianliang39 += 1
                print('bianliang39', bianliang39)
                return web.Response(body=str(bianliang39))
            elif query_str == 40:
                global bianliang40
                bianliang40 += 1
                print('bianliang40', bianliang40)
                return web.Response(body=str(bianliang40))
            elif query_str == 41:
                global bianliang41
                bianliang41 += 1
                print('bianliang41', bianliang41)
                return web.Response(body=str(bianliang41))
            elif query_str == 42:
                global bianliang42
                bianliang42 += 1
                print('bianliang42', bianliang42)
                return web.Response(body=str(bianliang42))
            elif query_str == 43:
                global bianliang43
                bianliang43 += 1
                print('bianliang43', bianliang43)
                return web.Response(body=str(bianliang43))
            elif query_str == 44:
                global bianliang44
                bianliang44 += 1
                print('bianliang44', bianliang44)
                return web.Response(body=str(bianliang44))
            elif query_str == 45:
                global bianliang45
                bianliang45 += 1
                print('bianliang45', bianliang45)
                return web.Response(body=str(bianliang45))
            elif query_str == 46:
                global bianliang46
                bianliang46 += 1
                print('bianliang46', bianliang46)
                return web.Response(body=str(bianliang46))
            elif query_str == 47:
                global bianliang47
                bianliang47 += 1
                print('bianliang47', bianliang47)
                return web.Response(body=str(bianliang47))
            elif query_str == 48:
                global bianliang48
                bianliang48 += 1
                print('bianliang48', bianliang48)
                return web.Response(body=str(bianliang48))
            elif query_str == 49:
                global bianliang49
                bianliang49 += 1
                print('bianliang49', bianliang49)
                return web.Response(body=str(bianliang49))
            elif query_str == 50:
                global bianliang50
                bianliang50 += 1
                print('bianliang50', bianliang50)
                return web.Response(body=str(bianliang50))
            elif query_str == 51:
                global bianliang51
                bianliang51 += 1
                print('bianliang51', bianliang51)
                return web.Response(body=str(bianliang51))
            elif query_str == 52:
                global bianliang52
                bianliang52 += 1
                print('bianliang52', bianliang52)
                return web.Response(body=str(bianliang52))
            elif query_str == 53:
                global bianliang53
                bianliang53 += 1
                print('bianliang53', bianliang53)
                return web.Response(body=str(bianliang53))
            elif query_str == 54:
                global bianliang54
                bianliang54 += 1
                print('bianliang54', bianliang54)
                return web.Response(body=str(bianliang54))
            elif query_str == 55:
                global bianliang55
                bianliang55 += 1
                print('bianliang55', bianliang55)
                return web.Response(body=str(bianliang55))
            elif query_str == 56:
                global bianliang56
                bianliang56 += 1
                print('bianliang56', bianliang56)
                return web.Response(body=str(bianliang56))
            elif query_str == 57:
                global bianliang57
                bianliang57 += 1
                print('bianliang57', bianliang57)
                return web.Response(body=str(bianliang57))
            elif query_str == 58:
                global bianliang58
                bianliang58 += 1
                print('bianliang58', bianliang58)
                return web.Response(body=str(bianliang58))
            elif query_str == 59:
                global bianliang59
                bianliang59 += 1
                print('bianliang59', bianliang59)
                return web.Response(body=str(bianliang59))
            elif query_str == 60:
                global bianliang60
                bianliang60 += 1
                print('bianliang60', bianliang60)
                return web.Response(body=str(bianliang60))
            elif query_str == 61:
                global bianliang61
                bianliang61 += 1
                print('bianliang61', bianliang61)
                return web.Response(body=str(bianliang61))
            elif query_str == 62:
                global bianliang62
                bianliang62 += 1
                print('bianliang62', bianliang62)
                return web.Response(body=str(bianliang62))
            elif query_str == 63:
                global bianliang63
                bianliang63 += 1
                print('bianliang63', bianliang63)
                return web.Response(body=str(bianliang63))
            elif query_str == 64:
                global bianliang64
                bianliang64 += 1
                print('bianliang64', bianliang64)
                return web.Response(body=str(bianliang64))
            elif query_str == 65:
                global bianliang65
                bianliang65 += 1
                print('bianliang65', bianliang65)
                return web.Response(body=str(bianliang65))
            elif query_str == 66:
                global bianliang66
                bianliang66 += 1
                print('bianliang66', bianliang66)
                return web.Response(body=str(bianliang66))
            elif query_str == 67:
                global bianliang67
                bianliang67 += 1
                print('bianliang67', bianliang67)
                return web.Response(body=str(bianliang67))
            elif query_str == 68:
                global bianliang68
                bianliang68 += 1
                print('bianliang68', bianliang68)
                return web.Response(body=str(bianliang68))
            elif query_str == 69:
                global bianliang69
                bianliang69 += 1
                print('bianliang69', bianliang69)
                return web.Response(body=str(bianliang69))
            elif query_str == 70:
                global bianliang70
                bianliang70 += 1
                print('bianliang70', bianliang70)
                return web.Response(body=str(bianliang70))
            elif query_str == 71:
                global bianliang71
                bianliang71 += 1
                print('bianliang71', bianliang71)
                return web.Response(body=str(bianliang71))
            elif query_str == 72:
                global bianliang72
                bianliang72 += 1
                print('bianliang72', bianliang72)
                return web.Response(body=str(bianliang72))
            elif query_str == 73:
                global bianliang73
                bianliang73 += 1
                print('bianliang73', bianliang73)
                return web.Response(body=str(bianliang73))
            elif query_str == 74:
                global bianliang74
                bianliang74 += 1
                print('bianliang74', bianliang74)
                return web.Response(body=str(bianliang74))
            elif query_str == 75:
                global bianliang75
                bianliang75 += 1
                print('bianliang75', bianliang75)
                return web.Response(body=str(bianliang75))
            elif query_str == 76:
                global bianliang76
                bianliang76 += 1
                print('bianliang76', bianliang76)
                return web.Response(body=str(bianliang76))
            elif query_str == 77:
                global bianliang77
                bianliang77 += 1
                print('bianliang77', bianliang77)
                return web.Response(body=str(bianliang77))
            elif query_str == 78:
                global bianliang78
                bianliang78 += 1
                print('bianliang78', bianliang78)
                return web.Response(body=str(bianliang78))
            elif query_str == 79:
                global bianliang79
                bianliang79 += 1
                print('bianliang79', bianliang79)
                return web.Response(body=str(bianliang79))
            elif query_str == 80:
                global bianliang80
                bianliang80 += 1
                print('bianliang80', bianliang80)
                return web.Response(body=str(bianliang80))
            elif query_str == 81:
                global bianliang81
                bianliang81 += 1
                print('bianliang81', bianliang81)
                return web.Response(body=str(bianliang81))
            elif query_str == 82:
                global bianliang82
                bianliang82 += 1
                print('bianliang82', bianliang82)
                return web.Response(body=str(bianliang82))
            elif query_str == 83:
                global bianliang83
                bianliang83 += 1
                print('bianliang83', bianliang83)
                return web.Response(body=str(bianliang83))
            elif query_str == 84:
                global bianliang84
                bianliang84 += 1
                print('bianliang84', bianliang84)
                return web.Response(body=str(bianliang84))
            elif query_str == 85:
                global bianliang85
                bianliang85 += 1
                print('bianliang85', bianliang85)
                return web.Response(body=str(bianliang85))
            elif query_str == 86:
                global bianliang86
                bianliang86 += 1
                print('bianliang86', bianliang86)
                return web.Response(body=str(bianliang86))
            elif query_str == 87:
                global bianliang87
                bianliang87 += 1
                print('bianliang87', bianliang87)
                return web.Response(body=str(bianliang87))
            elif query_str == 88:
                global bianliang88
                bianliang88 += 1
                print('bianliang88', bianliang88)
                return web.Response(body=str(bianliang88))
            elif query_str == 89:
                global bianliang89
                bianliang89 += 1
                print('bianliang89', bianliang89)
                return web.Response(body=str(bianliang89))
            elif query_str == 90:
                global bianliang90
                bianliang90 += 1
                print('bianliang90', bianliang90)
                return web.Response(body=str(bianliang90))
            elif query_str == 91:
                global bianliang91
                bianliang91 += 1
                print('bianliang91', bianliang91)
                return web.Response(body=str(bianliang91))
            elif query_str == 92:
                global bianliang92
                bianliang92 += 1
                print('bianliang92', bianliang92)
                return web.Response(body=str(bianliang92))
            elif query_str == 93:
                global bianliang93
                bianliang93 += 1
                print('bianliang93', bianliang93)
                return web.Response(body=str(bianliang93))
            elif query_str == 94:
                global bianliang94
                bianliang94 += 1
                print('bianliang94', bianliang94)
                return web.Response(body=str(bianliang94))
            elif query_str == 95:
                global bianliang95
                bianliang95 += 1
                print('bianliang95', bianliang95)
                return web.Response(body=str(bianliang95))
            elif query_str == 96:
                global bianliang96
                bianliang96 += 1
                print('bianliang96', bianliang96)
                return web.Response(body=str(bianliang96))
            elif query_str == 97:
                global bianliang97
                bianliang97 += 1
                print('bianliang97', bianliang97)
                return web.Response(body=str(bianliang97))
            elif query_str == 98:
                global bianliang98
                bianliang98 += 1
                print('bianliang98', bianliang98)
                return web.Response(body=str(bianliang98))
            elif query_str == 99:
                global bianliang99
                bianliang99 += 1
                print('bianliang99', bianliang99)
                return web.Response(body=str(bianliang99))
            else:
                return web.Response(body='query_string error!')
        else:
            return web.Response(body='query_string error!')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/wanfang', wanfang)
    app.router.add_route('GET', '/mohurd', mohurd)
    app.router.add_route('GET', '/tudijieguo', tudijieguo)
    await loop.create_server(app.make_handler(), '127.0.0.1', 9000)


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
