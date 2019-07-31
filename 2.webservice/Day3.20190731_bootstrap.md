## selector

태그

클래스

아이디 셀렉터 등등



# Bootstrap

CDN 활용을 통해 Bootstrap에 작성된 CSS, JS를 활용하자!



## 1. spacing



### 1-2 color

primary 파랑

secondary 회색

success 녹색

info 청록

warning 노랑

danger 빨강

light 하양

dark 검정



배경 색깔 변경

.bg-info



문자 색깔 변경

.text-success



버튼 만들기

.btn-success



### 1-3 border

.border .border-primary : 경계 색깔 설정

.rounded-circle: 보더 둥글게 만들기



### 1-4 Display

.d-block: 한 블록(줄)을 차지함

.d-inline: 같은 줄에 합침

.d-none: 가리기

.d-sm-none : sm사이즈일때는 none, 그 외에는 클래스를 적용시킴



사이즈 : Extra small, small, Medium, Large, Extra Large



### 1-5 position

.position-static

.position-relative

.position-absolute

.position-none

.fixed-top



### 1.6 Text

text-align: center ->

.text-center : 문자를 가운데 정렬

.font-weight-bold : 글씨체를 진하게



색깔이랑 breakpoint는  component에서 많이 쓰이니 참고!



## 2. Grid System

어떤 크기를 12등분해서 칸으로 구분

12등분 이유: 인수가 많아서 등분하기 편함



**Flexbox Foggy로 flex연습하기**



**자세한건 Bootstrap의 Utility 참조**



## Flask

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">MySite</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-item nav-link active" href="/lotto">Lotto<span class="sr-only">(current)</span></a>
          <a class="nav-item nav-link" href="/lunch">Lunch</a>
          <a class="nav-item nav-link" href="/opgg">opgg</a>
        </div>
      </div>
    </nav>
  <div class="container">
    {% block body %}
    {% endblock %}
  </div>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```



### index.html

```html
{% extends 'base.html' %}

{% block body %}
<h1>여기는 저의 사이트입니다.</h1>
{% endblock %}
```



### lotto.html

```html
{% extends 'base.html' %}

{% block body %}
{{numbers}}
{% endblock %}
```



### lunch.html

```html
{% extends 'base.html' %}

{% block body %}
    <h1>{{pick}}</h1>
{% endblock %}}
```



### opgg.html

```html
{% extends 'base.html' %}

{% block body %}
<form action="/search">
  <div class="form-group col-8">
    <img src="https://attach.s.op.gg/logo/20190730135214.bb87673d92d8dff6a5de5c104187e4b4.png" alt="">
    <input type="text" class="form-control d-inline" id="summoner" name="summoner">
  </div>
  <button type="submit" class="btn btn-primary d-inline">제출</button>
  <div class="spinner-border" role="status">
    <span class="sr-only">Loading...</span>
  </div>
  <div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      Dropdown button
    </button>
    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
      <a class="dropdown-item" href="#">소환사여 일어나라</a>
      <a class="dropdown-item" href="#">언랭사절</a>
      <a class="dropdown-item" href="#">화이팅</a>
    </div>
  </div>
  <div class="jumbotron">
    <h1 class="display-4">소환사 여러분, 안녕하세요!</h1>
    <p class="lead">이 곳은 소환사님들이 그 동안 쌓아온 전적과 수고를 돌아보는 자리입니다.</p>
    <hr class="my-4">
    <p>소환사님의 플레이 시간을 보고 싶다면</p>
    <a class="btn btn-primary btn-lg" href="#" role="button">게임 시간 확인</a>
  </div>
</form>
{% endblock %}
```



### search.html

```html
{% extends 'base.html' %}

{% block body %}
  <h1>여기는 결과창입니다.</h1>
  <p>{{summoner}}님의 등급은 {{user_tier}}입니다.</p>
{% endblock %}
```



### app.py

```python
{% extends 'base.html' %}

{% block body %}
  <h1>여기는 결과창입니다.</h1>
  <p>{{summoner}}님의 등급은 {{user_tier}}입니다.</p>
{% endblock %}
```

