import re
from bs4 import BeautifulSoup, Comment
import requests
from parsel import selector

authorset = {'责任编辑', '作者'}


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


def getcontent(lst):
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
    content = [x.strip() for x in lst[startindex:endindex + maxindex] if len(x.strip()) > 0]
    return content


def run(url):
    text = ''
    title, content = filter_tags(text)
    newcontent = getcontent(content)
    ctt = '\n'.join(newcontent)
    return title, ctt


title, ctt = run(
    'http://hb.yinchuan.gov.cn/hjjc/hjzf/201812/t20181226_1231487.htm')
print(title, ctt)
