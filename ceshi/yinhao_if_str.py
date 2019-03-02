import pymysql

host = '47.95.249.180'
user = 'yangfei'
password = 'Elements123'
db = 'spider'

conn = pymysql.connect(host='{}'.format(host), port=3306, user='{}'.format(user),
                       password='{}'.format(password), db='{}'.format(db), charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
