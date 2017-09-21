from bs4 import BeautifulSoup
import requests

webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=sat'
response = requests.get(webtoon_url)
source = response.text
soup = BeautifulSoup(source)
print(soup.prettify())

with open('sample.txt', 'wt') as f:
    f.write(soup.prettify())
