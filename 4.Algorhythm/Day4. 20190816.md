### 1209. [S/W 문제해결 기본] 2일차 - Sum

슈더 코드

```python
maxV = 0

#행의 합

for i : 0 -> 99
	s = 0 #행의 합, 행이 바뀔 때 초기화
	for j : 0 -> 99
		s = s + arr[i][j]
    if maxV < s:
        maxV = s
#열의 합
for i : 0 -> 99 # 열
    s = 0 # 열의 합, 열이 바뀔 때 초기화
    for j : 0 -> 99 # 행
        s = s + arr[i][j]
    if maxV < s # 열의 합과 비교
    	maxV = s
        
# 두 대각선의 합
s = 0 # 오른쪽 아래 방향
for i : 0 -> 99
    s = s + arr[i][j]
if maxV < s
	maxV = s
s = 0 # 왼쪽 아래 방향
for i : 0 -> 99
    s = s + arr[i][99-i] # N X N인 경우 arr[i][N-1-i]
    

```



```python
maxV = 0
s3 = 0 # 오른쪽 아래
s4 = 0 # 왼쪽 아래
for i : 0 -> 99
    s1 = 0 # 행의 합, 행이 바뀔 때 초기화
    s2 = 0 # 열의 합
    s3 = s3 + arr[i][i]
    s4 = s4 + arr[99-i]
    for j : 0 -> 99
        s1 = s1 + arr[i][j]
        s2 = s2 + arr[j][i]
    if maxV < s1: # 행의 합의 비교
    	maxV = s1
    if maxV < s2:
        maxV = s2
    if maxV < s3:
        maxV = s3
    if maxv < s4:
        maxV = s4
```



# 인덱스

인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다. Database 분야가 아닌 곳에서는 Look up table 등의 용어를 사용하기도 한다.



## 셀렉션 알고리즘(Selection Algorithm)

저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.



## 선택 정렬

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

시간복잡도 O(n**2)

```python
# N개의 원소
# 최소값을 찾는 구간의 시작 인덱스

for i : 0 -> N-2
    minidx = i # 각 구간의 시작인덱스
	for j : i+1 -> N-1 # 최소값을 찾는 구간 
        if arr[minidx] > arr[i]
        	minidx = j
    arr[i], arr[minidx] = arr[minidx], arr[i]
    
    
```

```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, lan(a)):
            if a[min] > a[j]:
            	min = j
        a[i], a[min] = a[min], a[j]
```

## 연습문제 3



# 문자열(String)

1967년 미국에서 ASCII(American Standard Code for Information Interchange)라는 문자 인코딩 표준이 제정

7bit 인코딩으로 128문자를 표현하면 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있다.

다국어 처리를 위해 표준을 마련 -> 유니코드

```markdown
10진수 153 = 100*1 + 10*5 + 1*3 = 10**2 * 1 + 10**1 * 5 + 10**0 *3
2진수 101 = 2**2*1 + 2**1*0 + 2**0*1 => 10진수로 나타내면 4*1 + 2*0 + 1*1 = 5
10진수 2진수 16진수
0 000  0
1 001  1
2 010  2
3 011	3
4 100  4 
5 101	5
6 110 	6	
7 111   7

8 1000    8
9 1001	  9
10 1010   A
11 1011	  B
12 1100   C
13 1101   D
14 1110   E

```



## 파이썬에서 문자열 처리

- char 타입 없음
- 텍스트 데이터의 취급법이 



### 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있다.
- 자기 문자열을 이용할 경우는 swap을 위한 임시 변수가 필요하면 반복 수행을 문자열 길이의 반만을 수행해야 한다.

### 문자열 교체하기

다음 예에서 문자열 내에서 "1, 2"라는 문자열을 "one, two" 로 변경해 보자.[교체될 문자열의 저장 공간은 충분히 크다고 가정]

```python
s1 = 'abc 1, 2, ABC'

s = ''
for i in range(0, len(s1)):
    if s1[i] == '1':
        s = s+'one'
    elif s1[i] == '2':
        s = s+'two'
    else:
        s = s+s1[i]
print(s)
```



### 고지식한 알고리즘(Brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일히 비교하는 방식으로 동작

```python
p = "is" # 찾을 패턴
t = "This is a book~!" # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N: 
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i - M # 검색 성공
    else: return -1 # 검색 실패

```

**슈더 코드**

```python
0123456
This is
	is
i    4
j    2


for i : 0 -> N-M # 패턴의 길이만큼 비교구간을 만들었을 때 시작 인덱스
    for j : 0 -> M-1 #패턴 내부의 비교 위치
        if t[i+j] != p[j]
        	break
     
    if j == M
    	return 1 # return i(패턴의 시작위치)
return -1 # 패턴이 존재하지 않음...    
```



### KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는 지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 시간 복잡도 O(M+N)



### 보이어-무어 알고리즘

- 오른 쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘



### 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

```python
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    result = []

    #가로줄 확인
    Garo_lst = []
    for i in range(N):
        Data = input()
        Garo_lst.append(Data)
        for i in range(len(Data)-M+1):
            if Data[i:M+i] == Data[i:M+i][::-1]:
                result.append(Data[i:M+i])

    #세로줄 확인
    Sero_lst = []
    Sero_sub_lst = ''
    for x in range(N):
        for y in Garo_lst:
            Sero_sub_lst += y[x]
        Sero_lst.append(Sero_sub_lst)
        Sero_sub_lst =''
    print(Sero_lst)

    for sero_data in Sero_lst:
        for j in range(len(sero_data)-M+1):
            if sero_data[j:M+j] == sero_data[j:M+j][::-1]:
                result.append(sero_data[j:M+j])

    # print(result)
    print("#%d %s"%(tc, result[0]))
```

### 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

```python
T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    result = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            result = 1

    print('#%d %s'%(t, result))
```

### 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수

```python
T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    sub_cnt, cnt = 0, 0

    for i in str1:
        for j in str2:
            if i == j:
                sub_cnt += 1
        if sub_cnt > cnt:
            cnt = sub_cnt
        sub_cnt = 0
    print("#%d %s"%(t, cnt))
```



### 1976. 시각 덧셈

```python
T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = list(map(int, input().split()))

    h = h1 + h2
    m = m1 + m2

    if m > 60:
        m -= 60
        h += 1

    if h > 12:
        h -= 12

    print('#{} {} {}'.format(tc, h, m))
```

### 1216. [S/W 문제해결 기본] 3일차 - 회문2

```python
for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1

    # 가로줄 확인
    Garo_lst = []
    for i in range(N):
        Data = input()
        Garo_lst.append(Data)
        #회문 길이
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if Data[k:M+K] == Data[k:M+K][::-1]:
                    if len(Data[k:M+k]) > result:
                        result = len(Data[k:M+k])

    # 세로줄 확인
    Sero_lst = []
    Sero_sub_lst = ''
    for x in range(N):
        for y in Garo_lst:
            Sero_lst.append(Sero_sub_lst)
            Sero_sub_lst = ''

    for sero_data in Sero_lst:
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if sero_data[k:M+k] == sero_data[k:M+k][::-1]:
                    if len(sero_data[k:M+k]) > result:
                        result = len(sero_data[k:M+k])

    print("#%d %s"%(tc, result))
```

**해결방법1**

```python
def find():
    for i in range(0, len(str2)-len(str1)+1): # str2에서 비교를 시작하는 위치
        j = 0
        while str1[j] == str2[i+j]:
            j += 1
            if j == len(str1):
                return 1
    return 0
            
```



**해결방법2**

```python
str1 = input()
str2 = input()
r = str2.find(str1)
if r == -1:			#str1과 같은 부분이 없는 경우
    r = 0
else:
    r = 1
print('#{}{}'.format(tc, r))
```



**글자판에서 세로 회문이 있는 경우**

```python
def find():
    for i in range(N):
        for j in range(N-M+1):
            k = 0
            h = M//2
            while k < h:
                if
```

