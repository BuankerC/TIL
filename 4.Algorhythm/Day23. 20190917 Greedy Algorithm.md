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


