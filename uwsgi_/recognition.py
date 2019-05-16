# -*- coding: utf-8 -*-
import time
import requests
import random
from parsel import Selector
import json, base64

s = requests.session()
image_url = 'http://neris.csrc.gov.cn/shixinchaxun/login/ycode.do'
url = 'http://neris.csrc.gov.cn/shixinchaxun/honestyObj/query.do'
headers = {'Host': 'neris.csrc.gov.cn',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def getByte(img):
    img_byte = base64.b64encode(img)
    img_str = img_byte.decode('ascii')
    return img_str


class inquiry(object):
    def csrc(self, name, cardnum):
        form_data = {'randSesion': 'f08f0786362c43f1aa257cdfd99fdb35',
                     'realCardNumber': ''}
        form_data['objName'] = name
        form_data['realCardNumber'] = cardnum

        while True:
            ipurl = 'http://172.16.203.203:8080/ippool'
            res = requests.get(ipurl)
            iplist = json.loads(res.text)['ippool']
            ip = iplist[random.randint(0, len(iplist)) - 1]
            proxies = {'http': ip, "https": ip}
            try:
                image = s.get(image_url, headers=headers, proxies=proxies, timeout=3)
            except:
                time.sleep(0.5)
                continue

            img_str = getByte(image.content)
            data = {'img': img_str}
            json_mod = json.dumps(data)
            res = requests.post('http://172.16.203.78:8000/zqsx', data=json_mod)

            form_data['ycode'] = res.text
            # print auth
            try:
                html = s.post(url, data=form_data, headers=headers, proxies=proxies, timeout=3)
            except:
                time.sleep(0.5)
                continue
            if html.status_code == 200:
                resp = Selector(html.text)
                judge = resp.xpath(".//form[@id='list_form']/table/tr[1]/td/table/tr[3]/td[4]/text()")
                if judge:
                    time.sleep(0.15)
                    continue
                else:
                    if resp.xpath("//*[@id='sorttab2']/tbody/tr/td/font"):
                        return []
                    cods = resp.xpath("//*[@id='sorttab2']/tbody/tr")
                    fishing_net = []
                    for cod in cods:
                        fish = cod.xpath(".//td/text()").extract()
                        fish = [i.strip() for i in fish]
                        fish.append('http://neris.csrc.gov.cn' + cod.xpath(".//td/a/@href").extract_first())
                        fishing_net.append(fish)
                    return fishing_net
            else:
                time.sleep(0.3)


quiry = inquiry()
data = quiry.csrc('李强', '')
