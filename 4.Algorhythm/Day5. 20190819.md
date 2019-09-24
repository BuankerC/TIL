[TOC]



## 스택

스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 자료구조이다.
- 스택에 저장된 자료는 선형 구조를 갖는다.
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(LIFO)이라고 부른다.

### 연산

- 삽입 : push
- 삭제 :  pop
- 스택의 공백 여부 : isEmpty
- 스택의 top에 있는 item을 반환하는 연산 : peek

스택의 push 알고리즘

```python
def push(item):
    s.append(item)
```

스택의 pop 알고리즘

```python
def pop():
    if len(s) == 0:
        # underflow
        return
    else : 
        return s.pop(-1);
```



연습문제(스택 구현)

```python

#크기가 정해진 리스트를 이용한 스택 구현
stack = [0]*10
top = -1

#push(1)
top = top + 1
stack[top] = 1

#push(2)
top = top + 1
stack[top] = 2

#push(3)
top = top + 1
stack[top] = 3

#pop()
r = stack[top]
top = top - 1
print(r)
while(top != -1): # 스택이 비어있지 않으면 반복
    r = stack[top]
    top = top - 1
    print(r)

#append()를 사용한 스택
s = list()
s.append(10)
s.append(20)
s.append(30)
while(len(s) !=0):
    print(s.pop())
```

### 스택의 용용1: 괄호검사

**조건**

- 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
- 같은 괄호에서 왼쪽 괄호는 오른 쪽 괄호보다 먼저 나와야 한다.
- 괄호 사이에는 포함 관계만 존재한다.

**연습문제2**

```python
# 괄호의 짝이 맞으면 1 아니면 0 리턴
def f(txt):
    s = list() # 스택생성
    for i in range(len(txt)):
        if(txt[i]=='('): # 여는 괄호면 push()
            s.append(txt[i])
        elif(txt[i]==')'): # 닫는 괄호면 pop()해서 비교
            if (len(s)==0): # 스택이 비어있으면 오류
                return 0

            else: # 스택이 비어있지 않으면 여는 괄호 하나 꺼냄
                s.pop()
    # 스택에 여는 괄호가 남아있으면
    if(len(s)!=0):
        return 0
    else:
        return 1



T = int(input())
for tc in range(1, T+1):
    txt = input()
    print(f(txt))
```

### 스택의 응용 : Function call

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

### 재귀호출

특징

- 자기 자신을 호출하지만 사용하는 메모리 영역이 구분되므로 다른 함수를 호출하는 것과 같음.
- 정해진 횟수만큼, 혹은 조건을 만족할 때까지 호출을 반복함.

정해진 횟수만큼 호출하기

- 호출 횟수에 대한 정보는 인자로 전달
- 정해진 횟수에 다다르면 호출 중단

**피보나치**

```python
def fibo(n):
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)
```

중복 호출이 있음



### Memoization

```python
def fibo1(n):  
    return memo[n]

memo = [0, 1] 
```



### DP(Dynamic Programming)

동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.

동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.



**피보나치 수 DP 적용 알고리즘**

```python
def fibo2(n):
    f = [0, 1]
    
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
```



## SWEA 4869 종이붙이기

```python
def GetSome(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return GetSome(x+10) + GetSome(x+20) * 2

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print('#%d %s'%(tc, GetSome(0)))
```

**선생님 슈더코드**

```python
f(n) = f(n-1) +2*(n-2)

f = [1] # N = 0
f.append(1) # N = 1
f.append(3) # N = 2
for i in range(3, N+1):
    f.append(f[i-1] + 2*[i-2])
--------------------------------
f = [0]*(N+1)
f[0] = 1
f[1] = 1
f[2] = 3
for i in range(3, N+1):
    f[i] = f[i-1] + 2*[i-2]
    
---------------------------------
f(n)
	if n == 1
    	return 1
    elif n==2
    	return 3
    else
    	return f(n-1) + 2*(n-2) 
```



## SWEA 4866 괄호검사

```python
TC = int(input())
for tc in range(1, TC+1):
    Data = input()
    N = len(Data)
    stack = []
    for i in range(N):
        #여는 괄호가 올 경우 => stack에 저장
        if Data[i] == '(' or Data[i] == '{':
            stack.append(Data[i])
        elif Data[i] == ')' or Data[i] == '}':
            #닫는 괄호이며 stack이 빈 경우 => 처음부터 닫는 괄호가 오는 경우
            if len(stack) == 0:
                stack = [Data[i]]
                break
            #stack에 저장된 괄호와 일치하지 않는 경우
            elif (Data[i] == '}' and stack[-1] !='{') or (Data[i] == ')' and stack[-1] != '('):
                stack = [Data[i]]
                break
            #stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
            else:
                stack.pop()

    if not len(stack):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
```

슈더코드

#모든 글자에 대해

(1) 여는 괄호 '{' 또는 "(" 인경우 push()

(2) 닫는 괄호인 경우

(2-1) '}'인 경우

​	pop() 결과 짝이 맞으면, '{'인 경우 계속 아니면 중지

(2-2) ')'인 경우

​	pop() 결과 짝인 맞으면 계속, 아니면 중지

#모든 글자에 대한 검토 후

스택에 남은 괄호가 있으면 비정상,

남은 괄호가 없으면 정상



## SWEA 4873 반복문자 지우기

```python
TC = int(input())

for tc in range(1, TC+1):
    Data = list(input())
    N = len(Data)
    stack = []
    for i in range(N):
        # stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우
        # stack에 저장(append)
        if not stack or stack[-1] != Data[i]:
            stack.append(Data[i])
        #stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우
        # stcak에서 제거(pop)
        elif stack and stack[-1] == Data[i]:
            stack.pop()
    print(f'#{tc} {len(stack)}')
```

슈더 코드

#모든 글자에 대해

스택이 비어 있지 않으면

​	현재 글자를 마지막으로 저장된 글자와 비교

​	일치하면 pop()하고 버림

​	일치하지 않으면 push()



스택이 비어 있으면

​	push()



CAAABBA

C (C, Stack is Empty)

CA

C

CA

CAB

CA

C

## 비트 연산자

```markdown
& 비트 단위로 AND 연산을 한다.

| 비트 단위로 OR 연산을 한다.

<< 피연산자의 비트 열을 왼쪽으로 이동시킨다.

>> 피연산자의 비트열을 왼쪽으로 이동시킨다.

<< 연산자
- 1 << n: 2**n** 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
& 연산자
- i&(1<<j): i의 j번째 비트가 1인지 아닌지를 리턴한다.



```

**보다 간결하게 부분집합을 생성하는 방법**

```python
arr = [3,6,7,1,5,4]

n = len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분 집합의 개수
    for j in range(n+1): # 원소의 수만큼 비트를 교환함
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=', ')
    print()
print()
```



### 1859. 백만 장자 프로젝트

슈더 코드

#주어진 가격의 범위

0~N-1(N일)

#사는 것을 고려하는 범위

i : 0 ~ N-2

​	#파는 것을 고려하는 범위

​	j : i+1 ~ N+1

​		#i날에 사서 j날에 팔 때 최대 이익을 찾음

​		#이익이 없으면 사지 않음



```python
T = int(input())
for i in range:
	
    
    
    
```

