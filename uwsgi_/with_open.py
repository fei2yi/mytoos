from urllib import parse

with open('C:\\Users\yf\Documents\WeChat Files\wxid_jw91l5z2musr22\Files\\元素征信数据中标_2019-02-19.data', 'r',
          encoding='utf8') as f:
    bbb = f.readlines()

urls = []
url_dict = {}
for bid, b in enumerate(bbb):
    url = b.split()[-1]
    # url解码
    urldata = parse.unquote(url)
    # url结果
    result = parse.urlparse(urldata)
    # 获取我需要的信息
    netloc = result.netloc
    scheme = result.scheme
    u = '{}://{}'.format(scheme, netloc)

    url_dict.setdefault(netloc, u)
    urls.append(netloc)

urls2 = set(urls)
for netloc in urls2:
    u_c = urls.count(netloc)
    print(url_dict.get(netloc), ',', u_c)
