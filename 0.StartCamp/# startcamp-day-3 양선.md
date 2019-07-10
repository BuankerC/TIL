비주얼 코드에서 텍스트 파일 작성하기

1.

```python
# open 함수의 경우 파일 명과 어떤 방식으로 열 것인지 선언해야 함
# 두번째 변수의 값을
# r : 읽기
# w : 쓰기
# a : 추가

f = open("student.txt", 'w')

f.write("안녕하세요")

f.close()
```





하면 폴더에 student. txt 라는 파일이 "안녕하세요"라는 내용으로 만들어진다.



"ctrl + /"  : 주석처리



파일을 열때는 이름이 필요

어떤 방식으로 열지 정해주기



csv

```python
import csv
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

tr = soup.select("tbody > tr")
with open("naver_exchange.csv",'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    
    for r in tr:    
        print(r.select_one('.tit').text.strip())
        print(r.select_one('.sale').text) 
        row = [r.select_one('.tit').text.strip(), (r.select_one('.sale').text)]
        csv_writer.writerow(row)
```





### HTML&CSS

하이퍼텍스트 : 문서와 문서가 연결되어 있음

마크업 : 

```html
<hl>HTML</hl>
<h2>HyperText Markup language</h2>
<a href="https://naver.com">네이버</a>
<태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름>

<!DOCTYPE html>
<html>
    <head>
        <style>
            h1{
               background-color:red; 
            }
            a {
               color:brown; 
            }
            .blue{
               background-color:blue; 
            }
            #git {
                background-color:black;
            }
        </style>
    </head>
    <body>
        <h1>HTML</hl>
        <h1 class="blue">CSS</h1>    
        <h2>HyperText Markup language</h2>
        <a href="https://naver.com">네이버</a>
        
        <!-- <태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름>     -->
        
        <h3>우리가 공부한것</h3>
        <ol>
            <li><strong><i>파이썬</i>></strong>></li>
            <li class="blue">HTML</li>
            <li id="git" class="blue">Git</li>
        </ol>
        
    </body>
</html>
```

***a href*** 문서에 링크 걸어주는 역할

***id*** - 중복되면 안됨, 지정해서 사용

***class*** - 동시에 적용 가능

***h*** - h1~h6까지 사용가능

***<html></html>*** html 문서의 시작과 끝

<head></head> 머리와

<body></body> 몸통

***ol*** Ordered List 주문받은 리스트? 라는 뜻

## css파일

```css
/* 여기는 CSS파일입니다!!! */
h1{
    background-color:red; 
}
a {
    color:brown; 
}
.blue{
        background-color:blue; 
}
#git {
        background-color:black;
}
```

- 위의 문서에서 head 부분을 잘라내어 CSS파일 작성

- html과 분리하여 작업의 효율성 극대화

  

html 용어 참고 사이트

https://www.w3schools.com/tags/tag_main.asp



### HTML, CSS, Javascript의 구분

html 구조를 잡음

CSS 표현하고 꾸미는 방법

Javascript 동작을 부여함

codecademy 참조

html의 h1~h6은 박스형 구조로 되어있다.

CSS

.XXX : 클래스



CSS selector



### 빗썸을 크롤링해보기!!

```python
import requests

import csv

from bs4 import BeautifulSoup



url = "https://www.bithumb.com/"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")



tr = soup.select("tbody > tr")

with open("btc_exchange.csv",'w', encoding="utf-8", newline="") as f:

​    csv_writer = csv.writer(f)

​    

​    for r in tr:    

​        print(r.select_one('.blind').text.strip())

​        print(r.select_one('.sort_real').text) 

​        row = [r.select_one('.blind').text.strip(), (r.select_one('.sort_real').text)]

​        csv_writer.writerow(row)


훌륭하다















```





### 메뉴와 번호판 나오게 하기

```python
import csv

lunch = {
    "BBQ":"123123",
    "중국집":"456456",
    "한식":"456789"
}

with open("lunch.csv", 'w', encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)

    for item in lunch.items():
        csv_writer.writerow(item)
        
        
```



