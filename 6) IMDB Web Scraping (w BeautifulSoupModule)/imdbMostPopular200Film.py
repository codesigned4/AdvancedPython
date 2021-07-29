import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top?ref_=nv_mv250"

html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")
                       #class attributu olarak lister-list olanı seçiyoruz
list=soup.find("tbody",{"class":"lister-list"}).find_all("tr")
count=1
for tr in list:
    title =tr.find("td",{"class":"titleColumn"}).find("a").string
    year=tr.find("td",{"class":"titleColumn"}).find("span").string.strip("()")
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").string
    print(f"{str(count).ljust(3)}- film: {title.ljust(100)} yıl: {year} değerlendirme: {rating}")
    count+=1
