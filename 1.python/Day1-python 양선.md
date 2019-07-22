# 상승장? 하락장?

> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

|      Key Name |                    Description |
| ------------: | -----------------------------: |
| opening_price |   최근 24시간 내 시작 거래금액 |
| closing_price | 최근 24시간 내 마지막 거래금액 |
|     min_price |   최근 24시간 내 최저 거래금액 |
|     max_price |   최근 24시간 내 최고 거래금액 |

```python
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']


start_price = int(data['opening_price']) # 구하고자 하는 항목의 변수 값 지정 및 정수화
maximum = int(data['max_price'])
minimum = int(data['min_price'])

coin_range = maximum - minimum

if maximum < start_price + coin_range:
    print("상승장")
else:
    print("하락장")


#list

#if 'opening_price'+'max_price'-'min_price' > 'max_price'
    #print("상승장")
#else
    #print("하락장")
```

# 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.



```python
my_str = "Life is too short, you need python"
result = ""

vowels = {'a', 'i', 'o', 'u', 'e'}

for char in my_str:
    if char not in vowels:
        result += char
print(result)
```

# 개인정보보호

> 사용자의 핸드폰번호를 입력 받으려고한다. 개인정보 보호를 위하여 뒷자리 4자리를 제외하고는 마스킹 처리를 하려고한다.
>
> 핸드폰번호는 010으로 시작해야하고 11자리여야한다. 핸드폰번호를 입력하지 않았다면 "핸드폰번호를 입력하세요"를 출력한다

```python
phone = input()

if len(phone) == 11 and phone[0:3] == "010":
    print('*'*7 + phone[-4:])
else:
    print("핸드폰 번호를 입력하세요")
```

# 정중앙

> 사용자가 입력한 문자열중 가운데 글자를 출력하라. 문자열이 짝수라면 가운데 두글자를 출력하라

```python
text = input()
# 안녕하세요
# 안녕하신가요

num = len(text) // 2


if len(text) % 2 == 1:
    middle = text[num]
else:
    middle = text[num-1:num+1]
    
print(middle)    
```