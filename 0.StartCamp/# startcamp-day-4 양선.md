### Flask 모듈 활용 파이썬 코드 작성

```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "안녕하세요!!!"

@app.route("/html_tag")
def html_tag():
    return "<hl>안녕하세요</h1>"

@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1>
    <h2>반갑습니다</h2>
    """

#학기 종료까지 남은 날 수 알려주기
import datetime
@app.route("/dday")
def dday():
    today = datetime.datetime.now()
    endday = datetime.datetime(2019,11,29)
    d = endday-today
    return f"1학기 종료까지 {d.days}일 남음"

#render 탬플릿을 활용, html파일에서 가져올 수 있음

@app.route("/html_file")
def html_file():
    return render_template('index.html')

@app.route("/greeting/<string:name>")
def greeting(name):
    return f"안녕하세요 {name}님!!"

@app.route("/cube/<int:num>")
def cube(num):
    cube_num = num**3
    return f"{num}의 세제곱은 {cube_num}입니다"

# 제곱을 표현할 때 **뒤에 숫자를 붙이면 지수를 표현함(**2:제곱, **3:세제곱)

@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)

@app.route("/greeting_html/<string:name>")
def greeting_html(name):
    return render_template("greeting.html", name=name)

import random

@app.route("/lunch")
def lunch():
    menu = {
        "짜장면":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/240px-Jajangmyeon_by_stu_spivack.jpg",
        "오므라이스":"http://mblogthumb2.phinf.naver.net/20160610_9/sallysto_1465485225315gh1xq_JPEG/DSC_0023.JPG?type=w800",
        "삼겹살":"https://pds.joins.com/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg"
    }

    menu_list = list(menu.keys()) # ["짜장면", "오므라이스", "삼겹살"]
    pick = random.choice(menu_list)
    img = menu[pick]

    return render_template("lunch.html", pick=pick, img=img)

# 영화 고르기
@app.route('/movies')
def movies():
    movie_list = ['롱리브더킹', '알라딘', '존윅', '맨인블랙']
    return render_template("movies.html", movie_list=movie_list)

@app.route("/ping")
def ping():
    return render_template("ping.html")

@app.route("/pong")
def pong():
    user_input = request.args.get("test")
    return render_template("pong.html", user_input=user_input)

#내 검색창에서 네이버 검색하기
@app.route("/naver")
def naver():
    return render_template("naver.html")

#내 검색창에서 구글 검색하기
@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/text")
def text():
    return render_template("text.html")

# 문자 입력 시 그림문양으로 바꾸기
import requests
@app.route("/result")
def result():
    raw_text = request.args.get('raw')
    url = "http://artii.herokuapp.com/make?text="
    res = requests.get(url + raw_text).text
    return render_template("result.html", res=res)

# @app.route('/random')

# 로또번호 추출하기
@app.route('/lotto')
def lotto():
    return render_template("lotto.html")

@app.route('/lotto_result')
def lotto_result():
    # 사용자가 입력한 정보를 가져오기
    numbers = request.args.get('numbers').split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n))
    
    # 로또 홈페이지에서 정보 가져오기
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    lotto_numbers = res.json()

    winning_numbers = []
    for i in range(1,7):
        winning_numbers.append(lotto_numbers[f'drwtNo{i}'])
    bonus_number = lotto_numbers['bnusNo']

    result = "1등"

    matched = len(set(user_numbers) & set(winning_numbers))
    if matched == 6:
        result = "1등"
    elif matched == 5:
        if bonus_number in user_numbers:
            result = "2등"
        else :
            result = "3등"
    elif matched == 4:
        result = "4등"
    elif matched == 3:
        result = "5등"
    else:
        result = "꽝"

    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, b=bonus_number, r=result)

if __name__ == '__main__':
    app.run(debug=True)
```
127.0.0.1 : 본인의 ip주소



템플렛 만들어 html 파일 따로 사용하기



***index.html***



문서명 : 안녕하세요 

내용: 여기는 나의 첫번째 웹페이지

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>안녕하세요</title>
</head>
<body>
    <h1>여기는 나의 첫번째 웹페이지</h1>
</body>
</html>

```

****

**greeting.html**



입력창에 다른 이름을 입력하면 @@님 안녕하세요!!

​				"선"을 입력하면 선야 안녕!!

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% if name == "선" %}
        <p style="color:blueviolet">{{name}}</p>야 안녕!!
    {% else %}   
        <p style="color:blueviolet">{{name}}</p>님 안녕하세요!!
    {% endif %}
</body>
</html>
```

****

**cube.html**





```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <strong>{{num_html}}</strong>의 세제곱은 <i>{{cube_num_html}}</i>입니다.
    <!-- 중괄호 두개 사이에 파이썬 변수를 담을 수 있다. -->
</body>
</html>
```



**lunch.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h3>오늘의 점심은 {{pick}} 어떠세요?</h3>
    <img src="{{img}}" alt="">
</body>
</html>
```



**movies.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ol>
    {% for movie in movie_list %}
        <li>{{movie}}</li>
    {% endfor %}
    </ol>
</body>
</html>
```



**ping.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 핑입니다.</h1>
    <form action="/pong">
        <input type="text" name="test">
        <input type="submit">
    </form>
</body>
</html>
```



**pong.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 퐁입니다.</h1>
    사용자가 방금 입력한 데이터는
    <p>{{user_input}}</p>
    입니다.
</body>
</html>
```



**naver.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="https://search.naver.com/search.naver">
        <input type="text" name="query">
        <input type="text" name="hihi">
        <input type="submit">
    </form>
</body>
</html>
```



**google.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 구글 페이크 검색창입니다.</h1>
    <form action="https://www.google.com/search">
        <input type="text" name="q">
        <input type="submit">
    </form>    
</body>
</html>
```



**text.hml**



입력한 글자를 아스키코드로 나타내기!!

```html
!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>입력한 글자를 아스키 코드로 바꿔줍니다.</h1>
    <form action="/result">
        <input type="text" name="raw">
        <input type="submit" value="변경">
    </form>
</body>
</html>
```



**result.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>결과는 다음과 같습니다!</h1>
        <pre>{{res}}</pre>
</body>
</html>
```



**lotto.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/lotto_result">
        <input type="text" name="numbers">
        <input type="submit">
    </form>
</body>
</html>
```



**lotto_result.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {{u}}
    {{w}}
    {{b}}
    {{r}}
</body>
</html>
```

