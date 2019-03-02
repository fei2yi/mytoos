import requests, json

url ='http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/showSearchResult-startWa.shtml'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '484',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'WEE_SID=4X10juj8EiyEywP5xOETT1pSwXAYURyRzf9BUs4b4eCM3ZIxm9AV!624860171!-445085552!1548143749372; IS_LOGIN=true; wee_username=eWZ5ZjEyMzQ1Ng%3D%3D; wee_password=eWZ5ZjEyMzQ1Ng%3D%3D; avoid_declare=declare_pass; JSESSIONID=4X10juj8EiyEywP5xOETT1pSwXAYURyRzf9BUs4b4eCM3ZIxm9AV!624860171!-445085552',
    'Host': 'www.pss-system.gov.cn',
    'Origin': 'http://www.pss-system.gov.cn',
    'Referer': 'http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/tableSearch-showTableSearchIndex.shtml',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
data = {
    'resultPagination.limit': '24',
    'resultPagination.sumLimit': '10',
    'resultPagination.start': '60',
    'resultPagination.totalCount': '260786',
    'searchCondition.sortFields': '-APD,+PD',
    'searchCondition.searchType': 'Sino_foreign',
    'searchCondition.originalLanguage': '',
    "searchCondition.extendInfo['MODE']": 'MODE_TABLE',
    "searchCondition.extendInfo['STRATEGY']": 'STRATEGY_CALCULATE',
    'searchCondition.searchExp': '公开（公告）日<2019-01-22 AND  公开（公告）日>2019-01-01',
    'searchCondition.executableSearchExp': "VDB:((PD<'2019-01-22' AND PD>'2019-01-01'))",
    'searchCondition.dbId': '',
    'searchCondition.literatureSF': '公开（公告）日<2019-01-22 AND  公开（公告）日>2019-01-01',
    'searchCondition.targetLanguage': '',
    'searchCondition.resultMode': 'SEARCH_MODE',
    'searchCondition.strategy': '',
    'searchCondition.searchKeywords': '[2][ ]{0,}[0][ ]{0,}[1][ ]{0,}[9][ ]{0,}[.][ ]{0,}[0][ ]{0,}[1][ ]{0,}[.][ ]{0,}[2][ ]{0,}[2][ ]{0,},[2][ ]{0,}[0][ ]{0,}[1][ ]{0,}[9][ ]{0,}[.][ ]{0,}[0][ ]{0,}[1][ ]{0,}[.][ ]{0,}[0][ ]{0,}[1][ ]{0,}',

}
res = requests.post(url, headers=headers, data=data)
text = res.text

aaa = json.loads(text)
ccc = aaa['searchResultDTO']['searchResultRecord']
print(11)
if '内查询次数已达6次' in text:
    print('内查询次数已达6次')
else:
    print(1)
