# -*- coding: utf-8 -*-
import requests
from tools.res import selector

sess = requests.session()

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
# }
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=1684b12fe380-06769999a6e177-58422116-1fa400-1684b12fe3a354; __jsluid=188a9a24e8bc207aa04cd9ca81b2edfd; __jsl_clearance=1551231428.844|0|lEOPePavEAI0qAuGBTpH7YRwzvM%3D; SECTOKEN=7153432849794467152; CNZZDATA1261033118=655066317-1551227493-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1551227493; gsxtBrowseHistory1=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219EEDDDD%15E%15E%15E%15DFB%16BG%16CLDEFCFE%11B%15EE%16DEB%10SXS%11%1A%00%1A%15%19%11SNS%E5%B1%BB%E7%B0%87%E7%A6%A5%E6%8B%B4%E6%9D%BD%E9%98%A4%E8%B5%97%E4%BA%8F%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEGDXS%02%1D%07%1D%00%00%1D%19%11SNEAAEFGFGMDLLE%09; tlb_cookie=S172.16.12.68; JSESSIONID=454AC082F02C09B0ADF08A928E4DB110-n2:11',
    'Host': 'www.gsxt.gov.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',

}
gene = 'SMN1'
data = {'tab': 'ent_tab',
        'province': '',
        'geetest_challenge': 'e5ffef05af1d0ac4dc6ef90c79eb8732',
        'geetest_validate': '1d16c3a99d5c080600c1b4e08564d73a',
        'geetest_seccode': '1d16c3a99d5c080600c1b4e08564d73a|jordan',
        'token': '82988162',
        'searchword': '阿里巴巴',
        }
url = 'http://sh.gsxt.gov.cn/SearchItemCaptcha?t=1551319795212'
# res = requests.post(url, data=data, headers=headers)
res = requests.get(url)

resp = selector(res)

webname = resp.xpath('//head/title/text()').extract_first()
keyword = resp.xpath('//head/meta[@name="keywords"]/@content').extract_first()
description = resp.xpath('//head/meta[@name="description"]/@content').extract_first()

aa = res.content
print(aa)
