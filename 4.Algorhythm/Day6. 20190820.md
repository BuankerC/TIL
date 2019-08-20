## 1859. 백만 장자 프로젝트

```python
T = int(input())
for tc in range(1, T+1):
    days = int(input())
    prices = list(map(int, input().split()))
    
    max_price = prices[-1]
    temp = 0
    gain = 0
    
    for i in range(len(prices)-1, -1, -1):
        if prices[i] > max_price:
            mac_price = prices[i]
        else:
            gain += (max_price - prices[i])
	print("#{} {}".format(tc, gain))    
    
#gain = 0
#for i in range(days):
#    max_price = prices[i]
#    for j in range(i, days):
#        if prices[j] > max_price:
#            max_price = prices[j]
#    if prices:
    
#    else:
```

슈더 코드

7 2 4 6 3 2 5

​			 3 2 5 : 6의 오른쪽 숫자들, 3과 5 중 큰 수(3과 3의 오른쪽 숫자 중 가장 큰 수)

​				2 5 : 3의 오른쪽 숫자들, 가장 큰 수 5



### 1926. 간단한 369게임

```python
N = int(input())

for i in range(1, N + 1):
    a = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if a:
        print('-'*a, end='')
    else:
        print('-', end='')
        
```

```python
n = int(input())
forbid = ['3', '6', '9']
for i in range(1, n+1):
    forbid_count = 0
    for j in str(i):
        if j in forbid:
            forbid_count += 1
    if forbid_count == 0:
        print(i, end=" ")
    else:
        print('-'*forbid_count, end=" ")
```



## 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 D2

```python
T = int(input())
for tc in range(1, T+1):
    txt = input()
    s = list()
    s.append(txt[0])
    for i in range(1, len(txt)):
        # 스택의 맨 위 글자와 다르면 push(txt[i]), 다르면 pop()
        if len(s) == 0 or s[-1] != txt[i]:
            s.append(txt[i])
        else:
            s.pop()
    print('#{} {}'.format(tc, len(s)))
```



## 스택2

### 계산기

문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.

문자열 수식 계산의 일반적 방법

중위 표기법, 후위 표기법

중위표기식의 후위 표기식 변환 방법 



**연습문제1**

수식문자열을 읽어서 피연산자는 바로 출력하고 연산자는 스택에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오. 연산자는 4칙 연산만 사용하시오.

```python
def find():
    s = []
    for i in range(len(code)):
        if code[i] == '+' or code[i] == '-' or code[i] == '/' or code [i] == '*':
            if len(s) > 2:
            	
               	
        
```





**후위 표기법의 수식을 스택에 이용하여 계산**

피연산자를 만나면 스택에 push한다.



### 백트래킹

해를 찾는 도중에 '막히면'(즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.

최적화 문제와 결정 문제를 해결할 수 있다.

**백트래킹과 깊이우선탐색과의 차이**

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임.



**백트래킹 기법**

- 어떤 노드의 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 모드로 감

- 어떤 노드를 방문하있을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.

- ###### 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로

**일반 백트래킹 알고리즘**

```python
def checknote(v) : #node
if promising(v):
    if there is a solution at v:
        write the solution
    else:
        for u in each child of v:
            checknode(u)
```



**부분집합 구하기**

연습문제2

{1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 구하시오.

```python
#합이 10인 부분집합의 개수
N = 10
K = 55
cnt = 0
arr = [i for i in range(1, N+1)]
for i in range(1, 1<<N):
    s = 0
    for j in range(N): #0에서 9번 비트까지 검사
        if i & (1<<j):
            s += arr[j] #j번이 부분집합에 포함되면..
            # s += j+1 # 인덱스를 직접 부분집합의 숫자로 활용
    if s == K:
        cnt += 1
print(cnt)
```



재귀를 사용한 부분집합

```python
#합이 10인 부분집합의 개수

def f(i, N, K):
    global cnt
    global bit
    if i==N: # bit의 모든 칸이 결정됨
        s = 0
        for j in range(N): # 0~N-1은 원집합의 원소 1~N을 가리킴
            if bit[j] == 1: # j+1이 부분집합에 포함된 경우
                s += j+1
        if s==K :
            cnt += 1
    else:
        bit[i] = 0
        f(i+1, N, K)
        bit[i] = 1
        f(i + 1, N, K)



N = 10 # 1부터 N까지가 집합의 원소
K = 10 # 부분집합의 합
cnt = 0
bit = [0] * N
f(0, N, K)
```

### 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

```python
TC = int(input())

for tc in range(1, TC + 1):
    Data = list(input().split())
    N = len(Data)
    stack = []
    flag = 0

    # 마침표는 제외하기 위해 N-1까지 반복
    for i in range(N - 1):

        # 숫자인 경우, stack에 append
        if Data[i].isdigit():
            stack.append(Data[i])

        else:
            try:  # 후위표기 계산
                num2, num1 = int(stack.pop()), int(stack.pop())

                if Data[i] == "+":
                    result = num1 + num2
                elif Data[i] == "-":
                    result = num1 - num2
                elif Data[i] == "/":
                    result = num1 // num2
                elif Data[i] == "*":
                    result = num1 * num2

                stack.append(str(result))

            except:  # 에러 발생 예외 처리 예) 숫자 + 연산자 + 연산자
                flag = 987654321

    # 예외처리 조건 (X) + Stack의 길이가 1인 경우(계산이 성공적인경우)
    if flag == 0 and len(stack) == 1:
        print(f'#{tc} {stack[0]}')

    # 예외처리 조건 (O) + stack의 길이가 2이상인 경우 ex) 숫자만 입력된 경우
    elif flag == 987654321 or len(stack) > 1:
        print(f'#{tc} error')

```



## 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 D2

```python
def IsSafe(y, x):
    return 0 <= y < N and 0 <= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def DFS(start_y, start_x):
    global result

    if Maze[start_y][start_x] == 3:
        result = 1
        return

    visited.append((start_y, start_x))
    for dir in range(4):
        New_Y = start_y + dy[dir]
        New_X = start_x + dx[dir]
        if IsSafe(New_Y, New_X) and (New_Y, New_X) not in visited:
            DFS(New_Y, New_X)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x
    #상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = []
    result = 0
    DFS(start_y, start_x)
    print('#%d %d'%(tc, result))
```

```python
def f(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global maze
    global N
    # if maze[i][j] == '1':
    #     return 0
    if maze[i][j] == '3': #목적지면
        return 1
    else:
        maze[i][j] = '1' # 방문 표시, 벽으로 바꿈
        #이동할 좌표 생성
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni > 0 and ni < N and nj >= 0 and nj < N:
                if maze[ni][nj] != 1: # 벽이 아니면 방문
                    if f(ni, nj) == 1: # 진행방향에서 목적지를 찾은 경우
                        return 1
        return 0 # 현재 위치에서 갈 수 있는 방향에서 목저지를 찾지 못함, 이전의 다른 방향 탐색




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Maze = [list(input()) for _ in range(N)]
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print('#{} {}'.format(tc, f(i, j)))
```



## 2001. 파리 퇴치

```python
testCase = int(input())

for testNum in range(1, testCase + 1):
    a = list(map(int, input().split()))
    N, M = a[0], a[1]
    mos = ''
    for i in range(N):
        mos += input()
        mos += ' '

    b = list(map(int, mos.split()))

    c = 0
    max = 0
    for i in range((N - M + 1)):
        for j in range((N - M + 1)):
            for k in range(M):
                c += sum(b[N * i + j + k * N: N * i + j + M + k * N])
            if max < c:
                max = c
            c = 0

    print('#{0} {1}'.format(testNum, max))
```



## 1989. 초심자의 회문 검사

```python
test_number = int(input())
for i in range(test_number):
    word = input()
    
    if word == word[::-1]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
```



## 2005. 파스칼의 삼각형

```python

```







## 분할 정복 알고리즘

**설계 전략**

- 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복 : 나눈 작은 문제를 각각 해결한다.
- 통합 : (필요하다면) 해결된 해답을 모은다.

**거듭 제곱(Exponentiation)**

```python
def Power(Base, Exponent):
    if Base == 0: return 1
    result = 1 # Base^0은 1이므로
    for i in range(Exponent):
        result *= Base
    return result
```

**분할 정복 기반의 알고리즘: O(log2n)**

```python
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    
    if Exponent % 2 == 0:
		NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base
```



## 퀵 정렬

**주어진 배열을 두 개로 분할하고, 각각을 정렬한다.**

**알고리즘**

```python
def quickSort(a, begin, end) : 
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
```



```python
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1
        while(a[R] < a[pivot] and L < R): R += 1
            if L < R:
                if L == pivot : pivot = R
                a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
```



