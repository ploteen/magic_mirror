import requests
from bs4 import BeautifulSoup
from datetime import datetime
def news_crawl():
    url = 'https://news.naver.com'
    html = requests.get(url,headers = {'User-Agent': 'Mozilla/5.0'})
    html = html.text
    bsObject = BeautifulSoup(html, 'html.parser')
    nnews = list()

    my_news = bsObject.select(
    'div#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit'
    )
    for news in my_news:
        nnews.append(news.text.strip())
    return nnews

if __name__=="__main__":
    news_crawl()