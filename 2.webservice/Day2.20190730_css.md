# CSS

- HTML없는 CSS는 무의미함

- 기본 사용법

  ```css
  hl{color:blue;font-size:15px}
  ```

  

## CSS 활용하기 1. Inline(인라인) -> 거의 안씀

```css
<h1 style="color:cyan">CSS intro</h1>
```

## 2. Embedding(내부참조)

```css
<style>
        h2 {
            color:gray
        }
    </style>
</head>
<body>
    <h2>CSS is awesome</h2>
</body>
</html>
```

## 3. link file(외부 참조)

```css
<link rel="stylesheet" href="00_intro.css">
</head>
<body>
    <h1 style="color:cyan">CSS intro</h1>
    <h2>CSS is awesome</h2>
    <p>Lorem ipsum dolor sit amet.</p>
</body>
</html>
```

컴포넌트화: 일반적으로 외부 파일로써 사용함

## CSS 단위

프로퍼티 값의 단위 : 키워드, 크기단위, 색깔

```css
p {
    font-size: 50px;
}
```





## 크기 단위

px : 디바이스별로 픽셀의 크기는 제각각임

% : 백분율 단위의 상대 단위 -> 요소에 지정된 사이즈에 상대적인 사이즈를 설정한다.  

```css
/* #으로 시작하는건 id이다 */
#hello {
    font-size: 50px;
}

#welcome {
    font-size: 200%;
}

div {
    width: 50%;
}

h1 {
    width: 50%;
}
```



## 배수 단위(rem, em)



```css
#lunch {
    font-size: 10em;
}
```



## viewport 단위

```css
/* 화면의 비율이 바뀌면 범위를 조절함 */
#menu {
    background-color: red;
    width: 50vw;
}
```

# 3. 색상 표현 단위

```markdown
HEX: 
RGB: 
RGBA:
```



## box model

```markdown
margin : 여백 주기

boarder

padding

div {
    width: 100px;
    height: 100px;
    background-color: darkgoldenrod;
    
}

.margin{
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 10px;
    margin-right: 10px;
}

.padding{
    padding-top: 20px;
    padding-bottom: 10px;
}

.border{
    /* border-width: 2px;
    border-color: magenta;
    border-style: dotted */
    border: 3px blue dotted;

```



## short hand

```css
/* 모든 방향 10 */
.margin-1 {
    margin: 10px;
}
/* 상하 10 좌우 20 */
.margin-2 {
    margin: 10px 20px;
}
/* 싱 10 좌우 20 하 30 */
.margin-3 {
    margin: 10px 20px 30px;
}
/* 상10 우20 하30 좌40 */
.margin-4 {
    margin: 10px 20px 30px 40px;
}
```

# Display

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="03_display.css">
</head>
<body>
    <div>
        <h1>div는 block입니다.</h1>
    </div>
    <h1>여기는 h1입니다.</h1>
    <div id="half">
        <h1>여기는 절반만!</h1>
    </div>
    <div id="half">
            <h1>여기는 절반만!</h1>
    </div>
</body>
</html>
```

## block

항상 새로운 라인에서 시작함.

기본적으로 너비의 100%

너비가 정해지면 나머지는 마진으로

레벨요소 예 : div, h1~h6, p, ol, ul, li hr, table, form

```css
div {
    background-color: greenyellow;
    margin-left: auto;
    margin-right: auto;
}

#half {
    width: 10%;
}
```



## inline

새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.

content의 너비만큼 가로폭을 차지한다.

width, height, matgin-top, margin-bottom 프로퍼티를 저장할 수 없다.

상, 하 여백은 line-height로 지정한다.

```html
    <span>여기는 span</span>
    <input type="text">
    <input type="date">
```



## inline-block

block과 inline 레벨 요소를 모두 갖는다.

```css
.bi {
    display: inline-block;
    margin-top: 20px;
}
```



## None

해당 요소를 화면에 표시하지 않는다.(공간조차 사라진다.)



# 3. Visibility 속성

## 3-1. visible

```css
visibility: hidden;
```

display:none 사라진다.

vs

visibility:hidden 숨겨진다.



## background-image



## font

font-size

font-family

letter-spacing



## Position

### 1. static

기본적인 위치

### 2. relative(상대적)

원래 위치에서 상대적인 위치

### 3.  absolute(절대적)

원본이 있던 위치를 기준으로 위치함.

방향 이동 시에는 가장 처음 만든 도형 기준으로 움직임.

```css
div {
    height: 100px;
    width: 100px;
}

.blue {
    background-color: blue;
    position: static;
}

.red {
    background-color: red;
    position: relative;
    left: 50px;
    bottom: 50px;
}

.green {
    background-color: green;
    position: absolute;
    left: 25px;
    top: 25px;
}
```



### 4. fixed (고정 위치)

