import re
from bs4 import BeautifulSoup, Comment
import requests

authorset = {'责任编辑', '作者'}


def getcontentfromweb(src):
    obj = requests.get(src)
    return obj.text


def filter_tags(html_str):
    soup = BeautifulSoup(html_str)
    title = soup.title.string.encode().decode('utf-8')
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    [comment.extract() for comment in comments]
    reg1 = re.compile("<[^>]*>")
    content = reg1.sub('', soup.prettify()).split('\n')
    return title, content


def getcontent(lst, title, authorset):
    lstlen = [len(x) for x in lst]
    threshold = 50
    startindex = 0
    maxindex = lstlen.index(max(lstlen))
    endindex = 0
    for i, v in enumerate(lstlen[:maxindex - 3]):
        if v > threshold and lstlen[i + 1] > 5 and lstlen[i + 2] > 5 and lstlen[i + 3] > 5:
            startindex = i
            break
    for i, v in enumerate(lstlen[maxindex:]):
        if v < threshold and lstlen[maxindex + i + 1] < 10 and lstlen[maxindex + i + 2] < 10 and lstlen[
            maxindex + i + 3] < 10:
            endindex = i
            break
    content = ['<p>' + x.strip() + '</p>' for x in lst[startindex:endindex + maxindex] if len(x.strip()) > 0]
    return content


def run(url):
    ctthtml = getcontentfromweb(url)
    title, content = filter_tags(ctthtml)
    newcontent = getcontent(content, title, authorset)
    ctt = ''.join(newcontent)
    return title, ctt


title, ctt = run(
    'http://www.cdepb.gov.cn/cdepbws/Web/Template/GovDefaultInfo.aspx?cid=850&aid=7ABE4B94FD084958A0D413AD91DA99F2')
print(title, ctt)
