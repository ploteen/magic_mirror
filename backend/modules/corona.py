import requests
from bs4 import BeautifulSoup

def corona_scrap():
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do'
    html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    html = html.text
    bsObject = BeautifulSoup(html, 'html.parser')
    numbers = list()
    numbers.append(bsObject.select('ul.ca_body > li > dl >dd.ca_value')[0].text)
    numbers.append(bsObject.select('p.inner_value')[0].text.split()[1])
    return numbers


if __name__=="__main__":
    corona_scrap()