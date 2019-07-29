# 웹 서비스

post 보내다

get 받다

클라이언트가 요청을 보내면 서버가 응답한다.

클라이언트가 요청을 보내는 프로그램 : **크롬**, 사파리, 인터넷익스플로러 등등

url : Uniform Resource Locator

​		자료에 도달하기 위해 만든 경로

도메인

등등



static web <-> dynamic web

HTML : Hyper Text Markup Language

웹 페이지를 작성하기 위한 역할 표시 언어

모든 문서가 서로 링크를 통해 연결된 문서

하이퍼텍스트를 주고 받는 규칙 : HTTP(S)

-> Hyper Text Transfer Protocol



문서를 구조화하는 방법 : Markup

CSS : Cascading Style Sheet -> 색깔이나 폰트 부여

Javascript :  동작을 부여



```html
<!-- 여기는 주석입니다. -->

<h1>element</h1>

<img src="url"/>
<!-닫는 태그가 없는 태그도 존재한다-->


<!--속성-->
<a href="google.com"></a>
<!--태그에는 속성이 지정될 수 있다.-->

<!--속성명광 속성값은 띄어쓰기 X, 속성값은 ""안에 사용-->

<!--id, class, style-->

<!--2.4,  돔트리-->

<!--시맨틱 태그 -->

<!--SEO-->
<!--검색 엔진 최적화-->

<!--header, nav, aside, section, article, footer-->

<h1>1111</h1>
<h2>2222</h2>
<h3>3333</h3>

<!--의미를 가지는 마크업이기 때문에 글자 크기를 키우기 위해 사용해선 안됨-->

<h1>여기는 중요한 제목입니다.</h1>
<p>상세한 내용은 <b>아래</b> 기사를 참조하세요</p>

<!--b는 그냥, strong은 시맨틱 태그-->

<ol>
    <li>순서없음</li>
    <li>두번째</li>
    <li>세번째</li>
</ol>

<ul>
    <li>야</li>
    <li>뭐</li>
    <li>왜</li>
</ul>

<nav>이건 내비게이션 바입니다</nav>
<div>의미가 없어요</div>
<span>의미가 없었죠</span>

<a href="https://naver.com">
<img src="https://s.pstatic.net/shopping.phinf/20190723_13/54b16279-f688-4117-8e3e-557df1e28800.jpg" >
</a>
```



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
    <h1>프로그래밍 교육</h1>
    <a href="#python">파이썬</a>
    <a href="#web">웹</a>
    <a href="intro.html">참고사이트</a>
    <hr>
    <h2 id="python">
        <a href="https://docs.python.org/ko/3/tutorial/index.html"target="_blank">
        <img src="https://www.python.org/static/img/python-logo.png"></a>
    </h2>
    <h3>Number type</h3>
    <p>파이썬에서 숫자형은 아래와 같이 있다.</p>
    <ol>
        <li>int</li>
        <li>float</li>
        <li>complex</li>
        <li><del>str</del></li>
    </ol>
    <h3>Sequence</h3>
    <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>
    <p><b>시퀀스는 for문을 돌릴 수 있다.</b></p>

    <ol>
        <li>str</li>
        <li>list</li>
        <li>tuple</li>
        <li>range</li>
    </ol>

    <hr>

    <h2 id="web"><a href="https://developer.mozilla.org/en-US/">
    <img width = "50 pixel" height = "50 pixel" src="images/html.png"></a></h2>
    <h3>기초</h3>
    <ul>
        <li style="list-style-type: Circle">HTML</li>
        <li style="list-style-type: Circle">CSS</li>
    </ul>

    <iframe width="560" height="315" src="https://www.youtube.com/embed/GuAjwnfGDFA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    <!-- <table border="1">
        <tr>
            <td></td>
            <td>월</td>
            <td>화</td>
            <td>수</td>
        </tr>
        <tr>
            <td>A코스</td>
            <td rowspan="2">짬뽕<br></td>
            <td colspan="2">초밥</td>
            <!-- <td>dd</td> -->
        <!-- </tr>
        <tr>
            <td>B코스</td>
            <td>김치찌개</td>
            <td>삼계탕</td>
        </tr>
    </table> --> -->

    <!-- 선생님 버전 -->
    <table>
        <thead>
            <td></td>
            <td>월</td>
            <td>화</td>
            <td>수</td>
        </thead>

        <tbody>
            <tr>    
                <th>1</th>
                <th rowspan="2">2</th>
                <th colspan="2">3</th>

            </tr>
            <tr>    
                <th>1</th>
                <th>2</th>
                <th>3</th>

            </tr>
        </tbody>
    </table>

    <table border="1">
        <tr>
            <td></td>
            <td>월</td>
            <td>화</td>
            <td>수</td>
        </tr>
        <tr>
            <td>A코스</td>
            <td rowspan="2">짬뽕<br></td>
            <td colspan="2">초밥</td>
        
        </tr>
        <tr>
            <td>B코스</td>
            <td>김치찌개</td>
            <td>삼계탕</td>
        </tr>

    <!-- <table border="1">
        <tr>
            <td></td>
            <td>소극장</td>
            <td>잔디마당</td>
            <td>대공연장</td>
        </tr>
        <tr>
            <td>10:00</td>
            <td rowspan="2">안녕하신가영</td>
            <td></td>
            <td>10CM</td>
        </tr>
        <tr>
            <td>13:00</td>
            <td rowspan="2">선우정아</td>
            <td></td>
        </tr>
        <tr>
            <td>15:00</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>17:00</td>
            <td>크러쉬</td>
            <td></td>
            <td>폴킴</td>
        </tr>
    </table>  -->

    <table>
        <thead>
            <th>TIME</th>
            <th>IN</th>
            <th colspan="2">OUT</th>
        </thead>
        <tbody>
            <tr>
                <td></td>
                <td style="border: 2px solid red">소극장</td>
                <td style="border: 2px solid limegreen">잔디마당</td>
                <td style="border: 2px solid cornflowerblue">대공연장</td>
            </tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>



</body>
</html>
```



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
    <h1>서브웨이 주문하기</h1>
    <p>주문서를 작성해주세요.</p>
    
    <form action="">
        <label for="name">이름:</label>
        <input id="name" type="text" name="name">

        <label for="when">날짜:</label>
        <input id= "when" type="date" name="when">
    
        <h2>1. 샌드위치 선택</h2>
        <input id="option1" type="radio" name="main" value="1"><label for="option1">에그마요</label>
        <input id="option2" type="radio" name="main" value="2"><label for="option2">비엘티</label>
        <input id="option3" type="radio" name="main" value="3"><label for="option3">터키</label>

        <input type="submit">
    
        <hr>

        <h2>2. 사이즈 선택</h2>
        <input type="text">

        <hr>

        <h2>3. 빵</h2>
        <select>
            <option value="honeyoat">허니오트</option>
            <option value="flatbread">플랫브레드</option>
            <option value="parmesanoregano">파마산 오레가노</option>
        </select>

        <hr>

        <h2>4. 야채/소스</h2>
        <input id="source1" type="checkbox" name="etc" value="s1"><label for="s1">토마토</label>
        <input id="source2" type="checkbox" name="etc" value="s2"><label for="s2">오이</label>
        <input id="source3" type="checkbox" name="etc" value="s3"><label for="s3">할라피뇨</label>
        <input id="source4" type="checkbox" name="etc" value="s4"><label for="s4">핫 칠리</label>
        <input id="source5" type="checkbox" name="etc" value="s5"><label for="s5">바베큐</label>

        <input type="submit">

        <hr>

        <h2>5. 오늘의 추천 메뉴</h2>
        <select>
            <option value="shrimp avocado">쉬림프 아보카도</option>
            <option value="pulled pork">풀드 포크</option>
            <option value="steak&cheeze">스테이크&치즈</option>
            <option value="turkey bacon avocado">터키 베이컨 아보카도</option>
            <option value="spicy Italian">스파이시 이탈리안</option>
        </select>

        
    </form>
</body>
</html>
```











