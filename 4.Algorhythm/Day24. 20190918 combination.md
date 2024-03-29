[TOC]

## 조합

**서로 다른 n개의 원소 중 r개를 순서없이 골라낸 것을 조합(Combination)이라고 부른다.**

**조합의 수식**

```python
nPr = n*(n-1)*...*(n-r+1)
	= n!/(n-r)!
'''
n개에서 r개를 고를 때,
어떤 1개를 포함하는 경우와 포함하지 않는 경우로 나눠서 생각한다.

'''
```

### 재귀 호출을 이용한 조합 생성 알고리즘

```python
an[] : n개의 원소를 가지고 있는 배열
tr[] : r개의 크기의 배열, 조합이 임시 저장될 배열
  
comb(n, r)
	if r == 0 : print_array_t
    elif n < r : return
    else
    	tr[r - 1] <- an[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)
```



# 탐욕 알고리즘

## 문제 제시 : 거스름돈 줄이기

**손님이 지불한 금액에서 물건값을 제한 차액(거스름돈)을 지불하는 문제를 생각해보자**

**"어떻게 하면 손님에게 거스름돈으로 주는 지폐와 동전의 개수를 최소한으로 줄일 수 있을까?"**

#### 탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법

#### 일반적으로, 머리 속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.



#### 여러 경우 중 하나를 선택할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.

#### 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, <u>그것이 최적이라는 보장은 없다.</u> 



#### 일단, 한 번 선택된 것은 번복하지 않는다. 이런 특성 때문에 대부분의 탐욕 알고리즘들은 단순하며, 또한 제한적인 문제들에 적용된다.

#### 최적화 문제(optimization)란 가능한 해들 중에서 가장 좋은(최대 또는 최소) 해를 찾는 문제이다.



### 탐욕 알고리즘의 동작 과정



#### 1) 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가한다.

#### 2) 실행 가능성 검사 : 새로운 부분 해 집합이 실행가능한 지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는 지를 검사한다.

#### 3) 해 검사 : 새로운 부분 해 집합이 문제의 해가 되는 지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1의 해 선택부터 다시 시작한다.



#### 탐욕 기법을 적용한 거스름돈 줄이기

1. 해 선택 : 여기에서는 멀리 내다볼 것 없이 가장 좋은 해를 선택한다. 단위가 큰 동전으로만 거스름돈을 만들면 동전의 개수가 줄어듦으로 현재 고를 수 있는 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가한다.
2. 실행 가능성 검사 : 거스름돈이 손님에게 내드려야 할 액수를 초과하는 지 확인한다. 초과한다면 마지막에 추가한 동전을 거스름돈에서 빼고, 1로 돌아가서 현재보다 한 단계 작은 단위의 동전을 추가한다.
3. 해 검사 : 거스름돈 문제의 해는 당연히 거스름돈이 손님에게 내드려야 하는 액수와 일치하는 셈이다. 더 드려도, 덜 드려도 안되기 때문에 거스름돈을 확인해서 액수에 모자라면 다시 1로 돌아가서 거스름돈에 추가할 돈전을 고른다.



### 배낭 짐싸기(knapsack)

#### 도둑은 부자들의 값진 물건들을 훔치기 위해 보관 창고에 침입하였다.

#### 도둑은 훔친 물건을 배낭에 담아 올 계획이다. 배낭은 담을 수 있는 물건의 총 무게(W)가 정해져 있다.

#### 창고에는 여러 개(n개)의 물건들이 있고 각각의 물건에는 무게와 값이 정해져 있다.

#### 경비원들에게 발각되기 전에 배낭이 수용할 수 있는 무게를 초과하지 않으면서, 값이 최대가 되는 물건들을 담아야 한다.



### Knapsack 문제 유형

- 0-1 Knapsack
  - 배낭에 물건을 통째로 담아야 하는 문제
  - 물건을 쪼갤 수 없는 경우
- Fractional Knapsack
  - 물건을 부분적으로 담는 것이 허용되는 문제
  - 물건을 쪼갤 수 있는 경우

#### 0-1 Knapsack에 대한 완전 검색 방법

- 완전 검색으로 물건들의 집합 S에 대한 모든 부분집합을 구한다.
- 부분집합의 총 무게가 W를 초과하는 집합들은 버리고, 나머지 집합에서 총 값이 가장 큰 집합을 선택할 수 있다.
- 물건의 개수가 증가하면 시간 복잡도가 지수적으로 증가한다.
  - 크기 n인 부분합의수 2**n



#### 0-1 Knapsack에 대한 탐욕적 방법1

- 값이 비싼 물건부터 채운다.
- W = 30kg



- 탐욕적 방법의 결과
  - (물건1), 25kg, 10만원
- 최적해
  - (물건2, 물건3), 20kg, 14만원
- 최적이 아니다



#### 0-1 Knapsack에 대한 탐욕적 방법2

- 무게가 가벼운 물건부터 채운다.
- W = 30kg



- 탐욕적 방법의 결과
  - (물건2 + 물건3), 14만원
- 최적해
  - (물건1), 15만원
- 역시 최적해를 구할 수 없다.



#### 0-1 Knapsack에 대한 탐욕적 방법3

- 무게 당 (예 > kg당) 값이 높은 순서로 물건을 채운다.
- W = 30kg



- 탐욕적 방법
  - (물건1, 물건3), 190만원
- 최적해
  - (물건2, 물건3), 200만원
- 역시, 탐욕적 방법으로 최적해를 구하기 어렵다.



#### Fractional Knapsack 문제

- 물건의 일부를 잘라서 담을 수 있다.
- 탐욕적인 방법
  - (물건1 + 물건3 + 물건2의 절반), 30kg, 220만원



### 회의실 배정하기

#### 김대리는 소프트웨어 개발팀들의 회의실 사용 신청을 처리하는 업무를 한다. 이번 주 금요일에 사용 가능한 회의실은 하나만 존재하고 다수의 회의가 신청된 상태이다.

#### 회의는 시작 시간과 종료 시간이 있으며, 회의 시간이 겹치는 회의들은 동시에 열릴 수 없다.

#### 가능한 많은 회의가 열리기 위해서는 어떻게 배정해야 될까?

#### 입력 예

- 회의 개수
- (시작시간, 종료시간)



### 활동 선택(Activity-selection problem) 문제

#### 시작시간과 종료시간(Si, Fi)이 있는 n개의 활동들의 집합 A = {A1, A2, ... , An}, 1 <= i <= n에서 서로 겹치지 않는(non-overlapping) 최대갯수의 활동들의 집합 S를 구하는 문제

#### 양립 가능한 활동들의 크기가 최대가 되는 S0,n+1 의 부분집합을 선택하는 문제

- 종료 시간 순으로 활동들을 정렬한다.
- S0,n+1 는 a0의 종료 시간부터 a n+1의 시작 시간 사이에 포함된 활동 들
- S0,n+1 = {a1, a2, a3, a4, a5, a6, a7, a8, a9, a10} = S



#### 탐욕 기법을 적용한 반복 알고리즘

```python
A : 활동들의 집합, S : 선택된 활동(회의)들의 집합
Si: 시작시간, Fi: 종료시간, 1 <= i <= n
Sort A by finish time
S <- {A1}
j <- 1
for i in 2 -> n
	if Si >= Fj
    	S <- S U {Ai}
		j <- i
```

#### 종료 시간이 빠른 순서로 활동들을 정렬한다.

#### 첫 번쨰 활동을 선택한다.

#### 선택한 활동의 종료시간보다 빠른 시작 시간을 가지는 활동을 모두 제거한다.

#### 남은 활동들에 대해 앞의 과정을 반복한다.



#### 탐욕적 선택 속성(greedy choice property)

- 탐욕적 선택은 최적해로 갈 수 있음을 보여라.
  - 즐, 탐욕적 선택은 항상 안전하다.



#### 최적 부분 구조(optimal substructure property)

- 최적화 문제를 정형화하라
  - 하나의 선택을 하면 풀어야 할 하나의 하위 문제가 남는다.



#### [원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해] 임을 증명하라.



 # 3. 분할 정복 & 백트래킹

## 학습목표

#### 문제를 분할해서 해결하는 분할 정복(Divide and Conquer) 기법을 이해하고 대표적인 알고리즘인 퀵 정렬과 병합 정렬에 대해 학습한다.

#### 상태 공간 트리의 모든 노드를 검색하는 백트래킹에 대해 학습한다.

#### 이진 트리(Binary Tree)의 특성을 이해하고 이진 트리의 중요한 연산인 탐색, 삽입, 삭제 알고리즘을 학습한다.



## 분할 정복 기법

#### Top-down approach



## 거듭 제곱

#### 반복(Iterative) 알고리즘 : O(n)

```python
Iterative_Power(x, n)
	result <- 1
    
    for i in 1 -> n
    	result <- result * x
    return result
```



#### 분할정복 기반의 알고리즘 : O(log2n)

```python
Recursive_Power(x, n)
	if n == 1 : return x
    if n is even
    	y <- Recursive_Power(x, n/2)
        return y * y
    else
    	y <- Recursive_Power(x, (n-1)/2)
        return y * y * x
```



## 병합 정렬(Merge Sort)

#### 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

#### 분할 정복 알고리즘 활용

- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
- top-down 방식

#### 시간 복잡도

- O(n log n)



#### 알고리즘 : 분할 과정

```python
merge_sort(list m)
	if length(m) == 1 : return m
    
    list left, right
    middle <- length(m) / 2
    for x in m before middle
    	add x to left
    for x in m after or equal middle
    	add x to right
        
    left <- merge_sort(left)
    right <- merge_sort(right)
    
    return merge(left, right)
```



#### 알고리즘 : 병합과정

```python
merge(list left, list right)
	list result
    
    while length(left) > 0 or length(right) > 0
    	if length(left) > 0 and length(right) > 0
        	if first(left) <= first(right)
            	append popfirst(left) to result
            else:
                append popfirst(right) to result
        elif length(left) > 0:
            append posfirst(left) to result
        elif length(right) > 0:
            append popfirst(right) to result
            
    return result
```



### 퀵 정렬

#### 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.

- 병합 정렬과 동일?



#### 다른 점1 : 병합 정렬은 그냥 두 부분을 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.



#### 다른 점 2 : 각 부분 정렬이 끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.



#### 알고리즘

```python
quickSort(A[], l, r)
	if l < r
    	s <- partition(a, l, r)
        quickSort(A[], l, s - 1)
        quickSort(A[], s + 1, r)
```



#### Hoare-Partition 알고리즘

```c
partition(A[], l, r)
    p <- A[l]
    i <- l, j <- r
    while i <= j
    	while A[i] <= p : i++
        while A[j] >= p : j--
        if i < j : swap(A[i], A[j])
        
    swap(A[l], A[j])
    return j
```



#### Lomuto partition 알고리즘

```c
partition(A[], p, r)
    x <- A[r]
    i <- p - 1
    
    for j in p -> r - 1
        if A[j] <= x
        	i++, swap(A[i], A[j])
        
    swap(A[i+1], A[r])
    return i + 1
```



## 이진 검색(Binary Search)

#### 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

#### 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

#### 검색과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

#### 알고리즘 : 반복구조

```python
binarySearch(n, s[], k)
low -> 0
high <- n - 1

while low <= high and location = 0
	mid <- low + (high - low) / 2
    
    if S[mid] == key
    	return mid
    elif S[mid] > key
    	high <- mid - 1
    else
    	low <- mid + 1
return -1
```



### 분할 정복의 활용

#### 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, 멀티코어 CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.



### swea 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Mat_Weight = list(map(int, input().split()))
    Truck_Weight = list(map(int, input().split()))
    visited = [0] * M

    ans = 0
    for i in range(M):
        result = 0
        for unit_Weight in Mat_Weight:
            if Truck_Weight[i] >= unit_Weight and unit_Weight >= result:
                result = unit_Weight
        if result != 0:
            Mat_Weight.remove(result)
        ans += result
    print('#{} {}'.format(tc, ans))
```

슈더코드

```python
'''
1 5 3 -> 컨테이너 무게
8 3 - > 트럭 용량

각각 정렬한다.

가장 무거운 컨테이너와 가장 큰 트럭을 
가리키는 인덱스를 준비한다.

인덱스가 가리키는 컨테이너를 인덱스 가리키는
트럭에 실을 수 있으면 두 인덱스를 다음으로 변경.
실을 수 없다면 컨테이너 인덱스만 다음으로 변경.
'''
```















