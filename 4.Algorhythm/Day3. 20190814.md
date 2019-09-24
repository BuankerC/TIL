[TOC]



# 1206. [S/W 문제해결 기본] 1일차 - View

슈더코드

#조망권 확인 구간 (가로 길이 N)

for i : 2 -> N - 3

​				if (h[i] > h[i-1] && h[i] > h[i-2] && h[i] > h[i+1] && h[i] > h[i+2])

​						diff = h[i] - h[i-1]

​						if(diff>h[i]-h[i-2])

​										diff = h[i] - h[i-2]

​						if(diff>h[i]-h[i+1])

​										diff = h[i] - h[i+1]

​						if(diff>h[i]-h[i+2])

​										diff = h[i] - h[i+2]

​						s = s + diff

```python
def GetMax(i):
    max_floor = floor[i-2]
    if max_floor < floor[i-1]:
        max_floor = floor[i-1]
    if max_floor < floor[i+1]:
        max_floor = floor[i+1]
    if max_floor < floor[i+2]:
        max_floor = floor[i+2]

    return max_floor

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    floor = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        side = GetMax(i)
        if side < floor[i]:
            result += floor[i] - side

    print(f'#{tc} {result}')
```



# 1208. [S/W 문제해결 기본] 1일차 - Flatten

슈더코드

덤프 횟수가 남아있는 동안,

최고점과 최저점의 차이가 1 이내면 중단,

아니면 최고점에서 1을 빼고 최저점에 1을 더함.



연습) 평탄화 하는데 필요한 최소 덤프 횟수는? 평탄화는 최고점과 최저점의 차이가 1 이내인 경우를 말함.

연습) 주어진 덤프횟수 안에 평탄화가 이뤄지면 1, 아니면 0을 출력하시오.

```python
for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    while(dump > 0):
        maxIdx = 0;
        minIdx = 0;
        for i in range(1, 100):
            if(box[maxIdx] < box[i]):
                maxIdx = i
            if(box[minIdx] < box[i]):
                minIdx = i
            diff = box[maxIdx] - box[minIdx]
            if (diff <= 1):
                break
            else:
                box[maxIdx] = box[maxIdx] - 1
                box[minIdx] = box[minIdx] + 1
        dump = dump -1
    print()
```



## 2차원 배열

**2차원 배열의 선언**

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화 통해 변수 선언과 초기화가 가능함

**배열 순회**

- n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

**행 우선 순회**

```python
# i행의 좌표
# j열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[i])):
        Array[i][j] # 필요한 연산 수행
```

**열 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j] # 필요한 연산 수행
```

**지그재그 순회**

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[0]))
    	Array[i][j + (m-1-2*j) * (i % 2)]
        # 필요한 연산 수행
```





**전치 행렬**

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3], [4,5,6], [7,8,9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```





**가로의 합, 세로의 합**

정사각형

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 가로의 합
for i in range(len(arr)):
    s = 0
    for j in range(len(arr[i])):
        s = s + arr[i][j]
    print(s)

# 세로의 합
for i in range(len(arr[i])): # 칸 변경
    s = 0
    for j in range(len(arr)): # 칸 고정, 줄 변경
        s = s + arr[j][i]
    print(s)
```



정사각형이 아닌 사각형

```python
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 가로의 합
N = 3 # row 줄 수
M = 4 # column 칸 수

for i in range(N):
    s = 0
    for j in range(M):
        s = s + arr[i][j]
    print(s)
# 세로의 합
for i in range(M): # 칸 변경
    s = 0
    for j in range(N): # 칸 고정, 줄 변경
        s = s + arr[j][i]
    print(s)
```



```python
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
# 가로의 합
for i in range(N):
    s = 0
    for j in range(M):
        s = s + arr[i][j]
    print(s)
# 세로의 합
for i in range(M): # 칸 변경
    s = 0
    for j in range(N): # 칸 고정, 줄 변경
        s = s + arr[j][i]
    print(s)
```



# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 D2



```python
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    red_1st = []
    blue_1st = []
    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if color == 1:
                    red_1st.append((y, x))
                elif color == 2:
                    blue_1st.append((y, x))

    result = []
    if len(red_1st) > len(blue_1st):
        for i in blue_1st:
            if i in red_1st:
                result.append(i)

    if len(red_1st) < len(blue_1st):
        for i in red_1st:
            if i in blue_1st:
                result.append(i)

    print('#%s %d'%(tc, len(result)))
```



# 연습문제 1

5X5 2차 배열에 무작위로 25개의 숫자로 초기화 한후

25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.

25개의 요소에 대해서 모두 조사하여 총합을 구하시오.

벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.

**델타를 이용한 2차 배열 탐색**

```python
ary[0...n-1][0...n-1]
dx[] <- [0, 0, -1, 1] # 상하좌우
dy[] <- [-1, 1, 0, 0]

for x in range(len(ary)):
    for y in range(len(ary[x])):
        for I in range(4):
            testX <- x + dx[mode]
            testY <- y + dy[mode]
            test(ary[testX][testY])
```



**문제풀이**

슈더코드

#모든 칸의 이웃에 대해 조사하는 경우

#모든 칸의 범위는

for i : 0 -> 4

​			for j : 0 -> 4

​						if ( j+1 <= 4) #오른쪽 칸이 존재하면

​						if( i+1 <= 4) #아래 칸이 존재하면

​						if( j-1 >= 0) #왼쪽 칸이 존재하면

​						if(  i-1 >= 0) #위쪽 칸이 존재하면

```python
# arr = [list(map(int, input().split())) for i in range(5)]
arr = [[0]*5 for i in range(5)]
k = 1
for i in range(0, 5):
    for j in range(0, 5):
        arr[i][j] = k
        k = k + 1

ni=dil[k]
nj=dil[k]
for k : 0 -> 3
    		ni = i + di[k]
        	nj = j + dj[k]
            if((ni>=0 and N and nj) >= and nj)

# 모든 칸의 이웃을 출력
for i in range(0, 5):
    for j in range(0, 5):
        if(j+1 <= 4): #오른쪽 칸이 존재하면
            print(arr[i][j+1], end = ' ')
        if(i+1 <= 4): #아래 칸이 존재하면
            print(arr[i+1][j], end = ' ')
        if(j-1 >= 0): #왼쪽 칸이 존재하면
            print(arr[i][j-1], end = ' ')
        if(i-1 >= 0): #윗 칸이 존재하면
            print(arr[i-1][j], end = ' ')
        print()
        
# 모든 칸의 이웃 중 짝수만 출력, 반드시 인덱스 범위 먼저 검사
for i in range(0, 5):
    for j in range(0, 5):
        if(arr[i][j+1]%2==0 and j+1 <= 4): # 오른쪽 칸이 존재하면
            print(arr[1][j+1])
        if (i + 1 <= arr[i][j+1]%2==0):  # 아래 칸이 존재하면
            print(arr[i + 1][j], end=' ')
        if (j - 1 >= arr[i][j+1]%2==0):  # 왼쪽 칸이 존재하면
            print(arr[i][j - 1], end=' ')
        if (i - 1 >= arr[i][j+1]%2==0):  # 윗 칸이 존재하면
            print(arr[i - 1][j], end=' ')
        print() 
 
```

## 부분집합 합(Subset Sum) 문제

유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는 지를 알아내는 문제

예를 들어, [-7, -3, -2, 5, 8]이라는 집합이 있을 때, [-3, -2, 5]는 이 집합의 부분집합이면서 (-3)+(-2)+5=0이므로 이 경우의 답은 참이 된다.

**부분집합 생성하는 방법**

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i				    # 0번째 원소
    for j in range(2):		
        bit[1] = j			    # 1번째 원소
        for k in range(2):
            bit[2] = k		    # 2번째 원소
            for l in range(2):
                bit[3] = l		# 3번째 원소
                print(bit)		# 생성된 부분집합 출력
```



**test1**

```python
arr = [1, 2, 3]
bit = [0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            print(bit)
```

**test2**

```python
arr = [1, 2, 3]
bit = [0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            print(bit)
            for m in range(3):
                if(bit[m]!=0): # m번 원소가 부분집합에 포함되면
                    print(arr[m], end=' ')
            print()
```



## 검색(Search)

저장되어 있는 자료 중에서 원하는 항목을 찾는 직업

목적하는 탐색 키를 가진 항목을 찾는 것

-탐색 키(search key) : 자룔를 구별하여 인식할 수 있는 키

종류

- 순차 검색(sequential search)
- 이진 검색(binary search)
- 해쉬(hash)

### 순차 검색

**일렬로 되어 있는 자료를 순서대로 검색하는 방법**

- 가장 간단하고 직관적인 검색 방법
- 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
- 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

**2가지 경우**

- 정렬되어 있지 않은 경우
- 정렬되어 있는 경우

#### 정렬되어 있지 않은 경우

**검색 과정**

- 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
- 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
- 자료구조의 마지막에 이를 때 까지 검색 대상을 찾지 못하면 검색 실패

**찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨**

- 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 비교

  시간 복잡도 : O(n)

  구현 예)

  ```python
  def sequentialsearch(a, n, key)
  	i <- 0
      while i<n and a[i]!=key : 
          i <- i+1
      if i<n : return i
      else : return i
  ```

  

#### 정렬되어 있는 경우

**검색 과정**

- 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.



### 이진 검색(Binary Search)

**자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법**

**이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.**

- 검색과정
  1. 자료의 중앙에 있는 원소를 고른다.
  2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

**구현**

```python
def binarySearch(a, key)
	start <- 0 end <- length(a)-1
    while start <= end :
        middle = (start + end)//2
        if a[middle] == key : # 검색 성공
            return True
        elif a[middle] > key : 
            end = middle - 1
        else: start = middle + 1
    return False # 검색 실패
```

**재귀함수 이용**

```python
def binarySearch2(a, low, high, key) :
    if low > high : # 검색 실패
        return False
    else :
        middle = (low + high) // 2
        if key == a[middle] : # 검색 성공
            return True
        elif key < a[middle] :
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key :
            return binarySearch2(a, middle-1, high, key)
```

**예) 이진 검색으로 20을 찾는 경우**

#개수 N

left = 0

right = N - 1

while (left = right)

#탐색 구간에 1개의 원소가 남을 때까지

​			center = (left + right) // 2

​			if (key == arr[center])

​					return 1

​			elif (arr[center] < key)

​			#작은 구간은 버림

​					left = center + 1

​			elif(key < arr[center])

​			#큰 구간도 버림

​					right = center - 1

#left > right, 1개만 남은 구간에서도 못 찾으면

return -1

## 1209. [S/W 문제해결 기본] 2일차 - Sum

```python
TC = 10
for tc in range(1, TC+1):
    lst = []
    N = int(input())
    for i in range(100):
        sub_lst = list(map(int, input().split()))
        lst.append(sub_lst)

    result = []

    for y in range(len(lst)): #각 행의 합
        sum_row = 0
        for x  in range(len(lst)):
            sum_row += lst[y][x]
        result.append(sum_row)

    for x in range(len(lst)): #각 열의 합
        sum_col = 0
        for y in range(len(lst)):
            sum_col += lst[y][x]
        result.append(sum_col)

    sum_diagonal1 = 0
    for y in range(len(lst)):   #첫번째 대각선의 합
        for x in range(len(lst)):
            if y == x:
                sum_diagonal1 += lst[y][x]
    result.append(sum_diagonal1)

    sum_diagonal2 = 0
    for y in range(len(lst)): #두번쨰 대각선의 합
        for x in range(len(lst)):
            if y == len(lst)-x:
                sum_diagonal2 += lst[y][x]
    result.append(sum_diagonal2)

    print(f'#{tc} {max(result)}')
```



## 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 D3

```python
TC = int(input())

for tc in range(1, TC + 1):
    info = list(map(int, input().split()))
    
    result = []
    for j in range(2):
        start = 1
        end = info[0]
        page = info[j+1]
        cnt = 0
        
        while start <= end:
            mid = (start + end) // 2
            if mid == page:
                break
            elif mid < page:
                start = mid
                cnt += 1
            else:
                end = mid
                cnt += 1
        result.append(cnt)
        
    if result[0] < result[1]:
        print('#%s'%tc, 'A')
    elif result[0] == result[1]:
        print('#%s'%tc, 0)
    else:
        print('#%s'%tc, 'B')
```



