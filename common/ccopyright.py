import requests

url = 'http://weixin.ccopyright.com/mobile/index.php?com=com_vcredentialQuery&method=wlist&name=&obligee=杨飞&registernumber=&page=4'
headers = {
    'Host': 'weixin.ccopyright.com',
    'Cookie': 'Hm_lpvt_f8ab12fa48356e856df03f3367877b16=1548137748; Hm_lvt_f8ab12fa48356e856df03f3367877b16=1548063421,1548137615; PHPSESSID=m809mhmcnr31n18turv91kfjv6; PHPSESSID_NS_Sig=oenCV6mfxDYg5xO8',
    'Connectioo': 'keep-alive',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/4.9 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.12 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.2(0x17000222) NetType/WIFI Language/zh_CN',
    'Referer': 'http://weixin.ccopyright.com/mobile/index.php?com=com_vcredentialQuery&method=selectBulletin',
    'Accept-Language': 'zh-cn',
    'Accept-Encodinh': 'gzip, deflate',
}
res = requests.get(url, headers=headers)
text = res.text
if '内查询次数已达6次' in text:
    print('内查询次数已达6次')
else:
    print(1)
