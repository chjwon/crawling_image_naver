from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어 입력: ')
crawl_num = int(input('몇개나 크롤링 하실것입니까? (최대 50개):'))

url = baseUrl+quote_plus(plusUrl) #한글 검색 자동 변환
html = urlopen(url)
soup = bs(html,"html.parser")
img = soup.find_all(class_='_img')

n=1
for i in img:
    print(n)
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        #plz fix the path of the image
        with open('path of the image'+str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)

    n+=1
    if(n>crawl_num):
       break

print('Image Crawling is done. ')
