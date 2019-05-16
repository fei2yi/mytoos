# coding:utf8
'''
icp 每天发送
'''
import datetime
import email
import smtplib
import os,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import xlwt
import MySQLdb


class MyEmail:
    def __init__(self):
        self.user = None
        self.passwd = None
        self.sql = None
        self.to_list = []
        self.cc_list = []
        self.tag = None
        self.doc = None
        self.content = None

    #下载附件
    def dowmysql(self):
        conn = MySQLdb.connect(host='47.95.249.180', user='yangfei', passwd='Elements123', db='spider_copy', charset='utf8')
        cursor = conn.cursor()
        count = cursor.execute(self.sql)
        print 'has %s record' % count
        if count >0:
            # 重置游标位置
            cursor.scroll(0, mode='absolute')
            # 搜取所有结果
            results = cursor.fetchall()
            # 测试代码，print results
            # 获取MYSQL里的数据字段
            fields = cursor.description
            # 将字段写入到EXCEL新表的第一行
            wbk = xlwt.Workbook()
            # 创建sheet页
            sheet = wbk.add_sheet('sheet1', cell_overwrite_ok=True)

            # 写入字段
            for ifs in range(0, len(fields)):
                sheet.write(0, ifs, unicode(fields[ifs][0], "utf-8"))

            ics = 1
            jcs = 0
            for ics in range(1, len(results) + 1):
                for jcs in range(0, len(fields)):
                    if ics <= 65535:
                        sheet.write(ics, jcs, results[ics - 1][jcs])

                print ics
            wbk.save('C:/Users/yf/Desktop/icp/'+str(int(time.strftime("%Y%m%d")) - 3)+'.xls')
            conn.close()
            return '1'
        else:
            return '0'

    def send(self):
        '''
        发送邮件
        '''
        try:
            server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
            server.login(self.user, self.passwd)
            print '1'
            server.sendmail("<%s>" % self.user, self.to_list + self.cc_list, self.get_attach())
            print '2'
            server.close()
            print "send email successful"
        except Exception, e:
            print "send email failed"

    def get_attach(self):
        '''
        构造邮件内容
        '''
        attach = MIMEMultipart()
        # 添加邮件内容
        txt = MIMEText(self.content)
        attach.attach(txt)
        if self.tag is not None:
            # 主题,最上面的一行
            attach["Subject"] = self.tag
        if self.user is not None:
            # 显示在发件人
            attach["From"] = "Data Team<%s>" % self.user
        if self.to_list:
            # 收件人列表
            attach["To"] = ";".join(self.to_list)
        if self.cc_list:
            # 抄送列表
            attach["Cc"] = ";".join(self.cc_list)
        if self.doc:
            # 估计任何文件都可以用base64，比如rar等
            # 文件名汉字用gbk编码代替
            name = os.path.basename(self.doc).encode("gbk")
            f = open(self.doc, "rb")
            doc = MIMEText(f.read(), "base64", "gb2312")
            doc["Content-Type"] = 'application/octet-stream'
            doc["Content-Disposition"] = 'attachment; filename="' + name + '"'
            attach.attach(doc)
            f.close()
        return attach.as_string()


if __name__ == "__main__":
    my = MyEmail()
    dates = str(int(time.strftime("%Y%m%d")) - 3)
    my.sql = """select distinct a.ENTNAME 开办者名称,case when a.etype = '1' then '企业' when a.etype = '2' then '个人' when a.etype = '3' then '事业单位'
            when a.etype = '4' then '政府' when a.etype = '5' then '军队' when a.etype = '6' then '司法鉴定所'
            when a.etype = '7' then '基金会' when a.etype = '8' then '境外驻华机构' when a.etype = '9' then '外国文化中心'
            when a.etype = '10' then '大中院校' when a.etype = '11' then '律师事务所' when a.etype = '12' then '民办非企业'
            when a.etype = '13' then '社会团体' when a.etype = '14' then '群团组织' when a.etype = '15' then '律师执业机构'
            when a.etype = '16' then '医疗机构' when a.etype = '17' then '宗教团体' when a.etype = '18' then '公正机构' end 开办主体 ,
            a.icpnum 公安备案号,a.webname 网站名称,a.hostname 网站域名,a.burl 官方验证地址,a.shdate '审核/备案日期',a.beiandi 备案地公安机关,
            a.TEL 电话,a.CONTACT 网站联系窗口,a.province 所在省份,a.city 所在城市
            from spider_copy.dataplus_icp a where a.shdate = '{0}' and a.etype != '2';""".format(dates)
    my.doc = r'C:/Users/yf/Desktop/icp/' + dates + '.xls'
    res = my.dowmysql()
    if res == '1':
        my.content = ' '
    else:
        my.content = '当天无数据!'
    print res
    print '附件下载成功'
    my.user = "qinwentao@elements.org.cn"
    my.passwd = "a94BX3prG39ueBkv"
    my.to_list = ["jingqikai@elements.org.cn", ]
    my.cc_list = ["yangfei@elements.org.cn",]
    my.tag = "icp数据测试-{0}".format(dates)

    print my.doc
    my.send()
