from bs4 import BeautifulSoup
import urllib.request as req

url = "https://quotes.toscrape.com/"

# urlopen()으로 데이터 가져오기 ---- (1)
res = req.urlopen(url)

# BeautifulSoup 으로 분석하기 ---- (2)
soup = BeautifulSoup(res, 'html.parser')

# 원하는 데이터 추출하기 ---- (3)
title = soup.find('title').string

# 제일 위에 것 하나만 가져오기
quote = soup.find('div', class_="quote")
text = quote.find('span', class_="text").string
author = quote.find('small', class_="author").string

print("페이지명:", title)
print("명언:", text)
print("작성자:", author)