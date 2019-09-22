[TOC]



# 완전 검색 & 그리디

## 반복(Iteration)과 재귀(Recursion)

**반복과 재귀는 유사한 작업을 수행할 수 있다.**

**반복은 수행하는 작업이 완료될 때까지 계속 반복**

**재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법**

- 하나의 큰 문제를 해결할 수 있는 (해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합한다.
- 재귀 함수로 구현

### 반복 구조

- 초기화(loop initialization)
  - 반복되는 명령문을 실행하기 전에 (한 번만) 조건 검사에 사용할 변수의 초기값 설정
- 조건 검사(check control expression)
- 반복할 명령문 실행(action)
- 업데이트(loop update)
  - 무한 루프(infinite loop)가 되지 않게 조건이 거짓(False)이 되게 한다.

```python
def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp
```



### 재귀적 알고리즘

- 재귀적 정의는 두 부분으로 나뉜다.
- 하나 또는 그 이상의 기본 경우(basis case or rule)
  - 집합에 포함되어 있는 원소는 induction을  생성하기 위한 시드(seed)역할
- 하나 또는 그 이상의 유도된 경우(inductive case or rule)
  - 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법



### 재귀 함수(recursive function)

- 함수 내부에서 직접 혹은 간접적으로 자기 자신을 호출하는 함수
- 일반적으로 재귀적 정의를 이용해서 재귀함수를 구현한다.
- 따라서, 기본부분(basis part)와 유도 파트(inductive part)로 구성된다.
- 재귀적 프로그램을 작성하는 것은 반복 구조에 비해 간결하고 이해하기 쉽다.
  - 그러나, 재귀에 대해 익숙하지 않은 개발자들은 재귀적 프로그램이 어렵다고 느낀다.
- 함수 호출은 프로그램 메모리 구조에서 스택을 사용한다. 따라서 재귀 호출은 반복적인 스택의 사용을 의미하며 메모리 및 속도에서 성능 저하가 발생한다.



### 팩토리얼 재귀 함수

- 재귀적 정의

```python
Basis rule:
    N <= 1 경우, n = 1
Inductive rule:
    N > 1, n! = n X (n - 1)!
```

- n!에 대한 재귀함수

```python
def fact(n):
    if n <= 1:  # Basis part
        return 1
    else:  # Inductive part
        return n * fact(n-1)
```



## 반복 또는 재귀?

**해결할 문제를 고려해서 반복이나 재귀의 방법을 선택**

**재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스럽다.**

- 추상 자료형(List, Tree 등)의 알고리즘은 재귀적 구현이 간단하고 자연스러운 경우가 많다.

**일반적으로, 재귀적 알고리즘은 반복(Iterative) 알고리즘보다 더 많은 메모리와 연산을 필요로 한다.**

**<u>입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있다.</u>**



### 반복과 재귀의 비교

|                |                        재귀                        |         반복          |
| -------------- | :------------------------------------------------: | :-------------------: |
| 종료           | 재귀 함수 호출이 종료되는 베이스 케이스(Base case) |  반복문의 종료 조건   |
| 수행 시간      |                   (상대적) 느림                    |         빠름          |
| 메모리 공간    |                 (상대적) 많이 사용                 |       적게 사용       |
| 소스 코드 길이 |                     짧고 간결                      |         길다          |
| 소스 코드 형태 |                선택 구조(if...else)                | 반복 구조(for, while) |
| 무한 반복시    |                  스택 오버플로우                   |  CPU를 반복해서 점유  |

### 2**k 연산에 대한 재귀와 반복

재귀 Recursion

```python
Power_of_2( k )
	if k == 0
    	return 1
    else
    	return 2 * Power_of_2( k - 1 )
```

반복 Iteration

```python
Power_of_2( k )
	i <- 0
    power <- 1
    while i < k
    	power <- power * 2
        i++
        
    return power
```



## 완전 검색 기법

### Baby-gin game



### 고지식한 방법(brute-force)

**brute-force는 문제를 해결하기 위한 간단하고 쉬운 접근법이다.**

- 'Just do it'
- force의 의미는 사람(지능)보다는 컴퓨터의 force를 의미한다.

**brute-force 방법은 대부분의 문제에 적용 가능하다.**

**상대적으로 빠른 시간에 문제 해결(알고리즘 설계)을 할 수 있다.**

**문제에 포함된 자료(요소, 인스턴스)의 크기가 작다면 유용하다.**

**학술적 또는 교육적 목적을 위해 알고리즘의 효율성을 판단하기 위한 척도로 사용된다.**



### 완전 검색으로 시작하라

**모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작다.**

- 완전검색은 입력의 크기를 작게 해서 간편하고 빠르게 답을 수하는 프로그램을 작성한다.

**이를 기반으로 그리디 기법이나 동적 계획법을 이용해서 효율적인 알고리즘을 찾을 수 있다.**

**검정 등에서 주어진 문제를 풀 때, <u>우선 완전 검색을 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직</u>하다.**



### 완전 검색

- 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것이다.
- 또한, 이들은 전현적으로 순열(permutation), 조합(combination), 그리고 부분집합(subsets)과 같은 조합적 문제들(Combinational Problems)과 연관된다.
- 완전 검색은 조합적 문제에 대한 brute-force 방법이다.



## 조합적 문제

### 문제 제시 : 여행사 BIG sale!



### 순열(Permutation)

**서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것**

**서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현한다.**

nPr

**그리고 nPr은 다음과 같은 식이 성립한다.**

nPr = n * (n-1) * (n-2)* ... *(n-r+1)

**nPn = n!이라고 표기하면 Factorial이라 부른다.**

n! = n * (n-1) * (n-2)* ... * 2 * 1 



**다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있다.**

- 예 > TSP

**N개의 요소들에 대해서 n!개의 순열들이 존재한다.**

- 12! = 479,001,600
- n > 12인 경우, 시간 복잡도 폭발적으로 증가



#### 단순하게 순열을 생성하는 방법

- 예) {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수
  - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop을 이용해 아래와 같이 구현할 수 있다.

```python
for i1 in 1 -> 3
	for i2 in 1 -> 3
    	if i2 != i1
        	for i3 in 1 -> 3
            	if i3 != i1 and i3 != i2
                	print(i1, i2, i3)
```



### 순열 생성 방법

#### 사전적 순서(Lexicographic-Order)

- {1, 2, 3}, n = 3 인 경우 다음과 같이 생성된다.
- [1 2 3] [1 3 2] [2 1 3] [2 3 1] [3 1 2] [3 2 1]

#### 최소 변경을 통한 방법(Minimum-exchange requirement)

- 각각의 순열들은 이전의 상태에서 단지 두 개의 요소들 교환을 통해 생성
- [**1** 2 **3**] [**3 2** 1] [2 **3 1**] [**2** 1 **3**] [**3 1** 2] [1 3 2]

#### 최소한의 변경(Minimum-change requirement)을 통해 다음 순열을 생성하는 방법

- 1950년대의 교회의 종소리 패턴하고 유사
- Johnson-Trotter 알고리즘



#### 재귀 호출을 통한 순열 생성

```c
// arr[] : 데이터가 저장된 배열
// swap(i, j): arr[i] <-- 교환 --> arr[j]
// n: 원소의 개수, k: 현재까지 교환된 원소의 개수
perm(n, k)
	if k == n
    	print array // 원하는 작업 수행
    else
    	for i in k -> n-1
        	swap(k, i);
            perm(n, k + 1);
            swap(k, i);
```



### 부분집합

#### 집합에 포함된 원소들을 선택하는 것이다.

#### 다수의 중요 알고리즘들이 원소들의 그룹에서 최적의 부분집합을 찾는 것이다.

- 예 > 배낭 짐싸기(knapsack)

#### N개의 원소를 포함한 집합

- 자기 자신과 공집합 포함한 모든 부분집합(power set)의 개수는 2**n개
- 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가



#### 단순하게 모든 부분집합 생성하는 방법

- 4개 원소를 포함한 집합에 대한 power set 구하기

```c
for i1 in 0 -> 1
    bit[0] <- i1              // 0번째 원소
    for i2 in 0 -> 1
        bit[1] <- i2          // 1번째 원소
        for i2 in 0 -> 1
            bit[2] <- i3      // 2번째 원소
            for i2 in 0 -> 1
                bit[3] <- i4  // 3번째 원소
                print_array() // 생성된 부분집합 출력
```



#### 바이너리 카운팅을 통한 사전적 순서(Lexicographical Order)

- 부분집합을 생성하기 위한 가장 자연스러운 방법이다.
- 바이너리 카운팅(Binary Counting)은 사전적 순서로 생성하기 위한 가장 간단한 방법이다.

#### 바이너리 카운팅(Binary Counting)

- 원소 수에 해당하는 N개의 비트열을 이용한다.
- n번째 비트값이 1이면, n번째 원소가 포함되었음을 의미한다.

#### 바이너리 카운팅을 통한 부분집합 생성 코드 예

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(0, (1 << n)):
    # 1 << n : 부분집합의 개수
    for j in range(0, n):
        #원소의 수 만큼 비트를 비교함
        if i & (i << j):
                # i의 j번째 비트가 1이 j번째 원소 출력
            print('%d, ' % arr[j], end='')
    print()
```



### swea 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3

```python
def Safe(y, x):
    return 0 <= y < N and 0 <= x < N

def DFS(y, x):
    global sub_result, result

    if result < sub_result:
        return

    if y == N - 1 and x == N - 1:
        result = sub_result
        return

    for dir in range(2):
        NewY = y + dy[dir]
        NewX = x + dx[dir]
        if Safe(NewY, NewX) and (NewY, NewX) not in visited:
            visited.append((NewY, NewX))
            sub_result += Data[NewY][NewX]
            DFS(NewY, NewX)
            visited.remove((NewY, NewX))
            sub_result -= Data[NewY][NewX]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]

    visited = []

    # 오른쪽 아래
    dy = [0, 1]
    dx = [1, 0]

    sub_result, result = Data[0][0], 987654321
    DFS(0, 0)
    print('#{} {}'.format(tc, result))
```

슈더 코드

```python
f(i, j, s) # 방문하는 칸의 좌표 i, j 이전에 지나온 칸의 합 s
	if i == N-1 and j == N - 1:
        
    else:
        f(i+1, j, s+arr[i][j])
        
        f(i, j+1, s+arr[i][j])
        
# i, j 칸까지 도착하는 최소비용의 합
for i : j -> N
    for j : 1 - > N
        d[i][j] = min(d[i-1][j], d[i][j-1]) + arr[i][j]
```





### swea 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3

```python
def solve(i, cnt):
    global minsum
    if i == N:
        if cnt < minsum:
            minsum = cnt
        return
    for j in range(N):
        if not check[j] and cnt + mat[i][j] <= minsum:
            check[j] = 1
            solve(i+1, cnt + mat[i][j])
            check[j] = 0

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))
    check = [0] * N
    minsum = 1500
    solve(0, 0)
    print('#%d %d' % (t, minsum))
```



## A대비 보충수업

### 백준 1182. 부분수열의 합

```python
N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, 1 << N):
    subset = []
    for j in range(N):
        if i % 1 << j:
            subset.append(arr[j])
    if sum(subset) == S:
        cnt += 1
print(cnt)
```



**선생님 코드**

```python
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, 1 << N):
    t = 0
    for j in range(N):
        if i % (1 << j):
            t += num[j]
    if S == t:
        cnt += 1
print(cnt)
```

```python
# 재귀로 만드는 경우

```



**슈더 코드**

```python
a = [3, 6]

[] -> bit = [0, 0]
[6] -> bit = [0, 1]
[3] -> bit = [1, 0]
[3, 6]-> bit = [1, 1]

for j in range(2):
    if bit[j] == 1:
        print(a[j], end="")
```











다시 올것 같던 나 혼자만의 오랜 기대였던 그 날들이

내겐 필요했어요 많은 걸 깨닫게 했던

그 이별을 단 한 번 더 오늘 할게요