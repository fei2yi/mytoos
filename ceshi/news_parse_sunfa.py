from newspaper import Article

url = 'http://hb.yinchuan.gov.cn/hjjc/hjzf/201812/t20181226_1231487.htm'
news = Article(url, language='zh')
news.download()
news.parse()
print(news.text)
print(news.title)
print(news.html)
print(news.authors)
print(news.top_image)
print(news.movies)
print(news.keywords)
print(news.summary)
