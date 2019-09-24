[TOC]



# 리스트

## 리스트

### 리스트

- 순서를 가진 데이터의 집합을 가리키는 추상자료형(abstract data type)
- 동일한 데이터를 가지고 있어도 상관없다.



- 구현방법에 따라 크게 두 가지로 나뉜다.

   1) 순차 리스트 : 배열을 기반으로 구현된 리스트

   2) 연결 리스트 : 메모리의 동적할당을 기반으로 구현된 리스트

### 순차리스트 구현 방법

- 1차원 배열에 항목들을 순서대로 저장한다.
- 데이터의 종류와 구조에 따라 구조화된 자료구조를 만들어 배열로 만들 수도 있다.

#### 데이터 접근

- 배열의 인덱스를 이용해 원하는 위치의 데이터에 접근할 수 있다.



## 연결리스트의 기본구조

### 노드

- 연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료 단위

- 구성 요소

  1) 데이터 필드

  - 원소의 값을 저장하는 자료구조
  - 저장할 원소의 종류나 크기에 따라 구조를 정의하여 사용함

  2) 링크 필드

  - 다음 노드의 주소를 저장하는 자료구조

### 헤드

- 리스트의 처음 노드를 가리키는 레퍼런스



## 단순 연결 리스트(Singly Linked List)

### 연결 구조

- 노드가 하나의 링크 필드에 의해 다음 노드와 연결되는 구조를 가진다.
- 헤드가 가장 앞의 노드를 가리키고, 링크 필드가 연속적으로 다음 노드를 가리킨다.
- 최종적으로 NULL을 가리키는 노드가 가장 마지막 노드이다.



## 단순 연결 리스트의 삽입 연산

### 'A', 'C', 'D'를 원소로 갖고 있는 리스트의 두번째에 'B'노드를 삽입할 때

1) 메모리를 할당하여 새로운 노드 new 생성

2) 새로운 노드 new의 데이터 필드에 'B' 저장

3) 삽입될 위치의 바로 앞에 위치한 노드릐 링크 필드를 new에 복사

4) new의 주소를 앞 노드의 링크 필드에 저장

### 첫번째 노드로 삽입하는 알고리즘

```python
def addtoFirst(data):		# 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head) # 새로운 노드 생성
```

### 가운데 노드로 삽입하는 알고리즘

```python
def add(pre, data):  # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
```

### 마지막 노드로 삽입하는 알고리즘

```python
def addtoLast(Data):  # 마지막에 데이터 삽입
    globla Head
    if Head == None :  # 빈 리스트이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:  # 마지막 노드 찾을 때까지
            p = p.link
        p.link = node(data, None)
```

### 노드를 삭제하는 알고리즘

```python
def delete(pre):  # pre 다음 노드 삭제
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link
```







### 대략적인 알고리즘

```python
import sys

class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link
        
def addLast(data):  # 마지막 노드 추가
    global pHead
    if pHead == None:
        pHead = Node(data, None)
    else:
        p = pHead
        while p.link != None:
            p = p.link
        p.link = Node(data, None)
    return

def add(data, idx):  # idx 위치에 새 노드 추가
    global pHead
    p = pHead
    n = 0
    while n < idx - 1:
        p = p.link
        n += 1
    t = p.link
    p.link = Node(data, t)
    return

def get(idx):  # idx의 데이터 리턴
    
```



## 이중 연결 리스트(Doubly Linked List)

### 특성

- 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
- 두 개의 링크 필드와 한 개의 데이터 필드로 구성



## 이중 연결 리스트의 삽입 연산

### cur가 가리키는 노드 다음으로 D값을 가진 노드를 삽입하는 과정

1) 메모리를 할당하여 새로운 new를 생성하고 데이터 필드에 'D'를 저장한다.



2) cur의 next를 new의 next에 저장하여 cur의 오른쪽 노드를 삽입할 노드 new의 오른쪽 노드로 연결한다.



3) new의 주소를 cur의 next에 저장형 노드 new를  cur의 오른쪽 노드로 연결한다.



4) cur에 있는 링크 값을  new의 prev 에 저장형 cur를 new의 왼쪽 노드로 연결한다.



5)  new의 주소를 new의 오른쪽 노드의 next에 저장하여 노드 new의 오른쪽 노드의 왼쪽 노드로 new를 연결한다.



## 삽입 정렬(Insertion Sort)

- 자료 배열의 모든 원소들을 앞에서부터 차례대로 이미 정렬된 부분과 비교화여, 자신의 위치를 찾아냄으로써 정렬을 완성한다.

### 정렬과정

- 정렬할 자료를 두 개의 부분집합 S와 U로 가정
  - 부분집합 S : 정렬된 앞 부분의 원소들
  - 부분집합 U : 아직 정렬되지 않은 나머지 원소들
- 정렬되지 않은 부분집합 U의 원소를 하나씩 꺼내서 이미 정렬되어 있는 부분집합의 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입한다.
- 삽입 정렬를 반복하면서 부분집합   S의 원소는 하나씩 늘리고 부분집합 U의 원소는 하나씩 감소하게 된다. 부분집합 U가 공집합이 되면 삽입정렬이 완성된다.

### 시간 복잡도

O(n**2)



## 병합 정렬(Merge Sort)

**여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식**

**분할 정복 알고리즘 활용**

- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
- top-down 방식

**시간 복잡도**

- O(n log n)



### 분할 과정

```python
def merge_sort(m):
    if len(m) <= 1 :  # 사이즈가 0이거나 1인 경우, 바로 리턴
        return m
    
    # 1. DIVIDE 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 2. CONQUER 부분 : 분할된 리스트들 벼합
    return merge(left, right)
```

### 병합 과정

```python
def merge(left, right):
    result = [] # 두 개의 분할된 리스트를 병합하여 result를 만듦
    
    while len(left) > 0 and len(right) > 0: # 양쪽 리스트에 원소가 남아있는 경우
        # 두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    if len(left) > 0 :  # 왼쪽 리스트에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0 :  # 오른쪽 리스트에 원소가 남아있는 경우
        result.extend(right)
    return result
```



## 리스트를 이용한 스택

### 리스트를 이용해 스택을 구현할 수 있다.

### 스택의 원소 : 리스트의 노드

- 스택 내의 순서는 리스트의 링크를 통해 연결됨
  - push : 리스트의 마지막에 노드 삽입
  - pop : 리스트의 마지막 노드 반환/삭제

### 변수 top

- 리스트의 마지막 노드를 가리키는 변수
- 초기 상태 : top = null



## 리스트를 이용한 스택 연산

### 리스트를 이용해 Push와 Pop 연산 구현

1) null값을 가지는 노드를 만들어 스택 초기화

2) 원소 A 삽입: push(A)

3) 원소 B 삽입:  push(B)

4) 원소 C 삽입: push(C)

5) 원소 반환 : pop

### Push/Pop

```python
def push(i):		# 원소 i를 스택 top(맨 앞) 위치에 push
    global top
    top = Node(i, pop)  # 새로운 노드 생성
    
def pop():             # 스택의 top을 pop
    global top
    
    if top == None :  # 빈 리스트이면
        print("error")
    else : 
        data = top.data
        top = top.link  # top이 가리키는 노드를 바꿈
        return data
```

















