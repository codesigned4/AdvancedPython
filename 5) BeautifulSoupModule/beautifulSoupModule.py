from bs4 import BeautifulSoup

html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1>
        Python KURSU
    </h1>

    <div class="grup1">

        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">

        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
<li>Menü 3</li>
        </ul>
    </div>

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>
     <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>
</body>
</html>
"""
soup=BeautifulSoup(html_doc,"html.parser")

result=soup.prettify()#html kaynağını düzenler
result=soup.title#tüm title getirir
result=soup.head#tüm head i getirir
result=soup.body#tüm body i getirir
result=soup.title.name#title name ini getirir
result=soup.title.string#title de yazan stringi getirir
result=soup.h1#h1 i getirir
result=soup.h2#ilk h2 yi getirir
result=soup.h2.string#h2 de yazan stringi getirir
result=soup.find_all("h2")#find_all in içerisine aldığı tüm etiketleri liste şeklinde getirir
reuslt=soup.find_all("h2")[0]#şeklinde ilk etikete ulaşabilirsin
result=soup.find_all("div")[1].ul.find_all("li")#[<li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]
result=soup.find_all("a")
for link in result:
    print(link.get("href"))
    #http://example1.com/elsie
    #http://example2.com/lacie 
    #http://example3.com/tillie