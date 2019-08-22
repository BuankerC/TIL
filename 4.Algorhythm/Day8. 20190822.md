## swea 2001 파리 잡기 응용

```python
#(1) 파리채가 X자 모양이라면(크기는 K)

#부분 배열의 왼쪽 위 모서리 좌표가 i, j 일 때,

s = 0
for m in range(K):
	s += fly[i+m][j+m] # 오른쪽 아래 방향
    s += fly[i+m][j+K-1-m] # 왼쪽 아래 방향
    # K가 홀수인 경우 가운데 원소가 두 번 더해지므로
if K%2==1:
    s -= fly[i+K//2][j+K//2] # 한 개를 빼줌
    
#(2)파리채가 ㄱ, ㄴ, ㄷ, ㄹ 모양인 경우
    
#(3) 파리채의 영역이 i+m, j+n 일 때, (0<=m, n<K)
m 짝수, n 홀수
m 홀수, n 짝수
나머지는 구멍이 나서 파리가 죽지 않는다.


```

## swea 1979. 어디에 단어가 들어갈 수 있을까(D2)

```python
tc = int(input())
for t in range(1, tc + 1):
  N, K = map(int, input().split())
  puzz = [[] * N for _ in range(N)]
  for i in range(N):
    puzz[i] = [int(n) for n in input().split()]

  ans = 0
  for i in range(N):
    rowcnt = colcnt = 0
    for j in range(N):
      if puzz[i][j] == 1:
        rowcnt += 1
      elif puzz[i][j] == 0:
        if rowcnt == K: ans += 1
        rowcnt = 0
      if puzz[j][i] == 1:
        colcnt += 1
      elif puzz[j][i] == 0:
        if colcnt == K: ans += 1
        colcnt = 0
    if rowcnt == K:
      ans += 1
    if colcnt == K:
      ans += 1
  print('#%d %d' % (t, ans))
```

## swea 1984. 중간 평균값 구하기(D2)

```python
tc = int(input())
for t in range(1, tc+1):
    nums = list(map(int, input().split()))
    maxn, minn = nums[0], nums[0]
    for i in range(1, 10):
        if nums[i] > maxn:
            maxn = nums[i]
        if nums[i] < minn:
            minn = nums[i]
    total = 0
    for n in nums:
        if n != maxn and n != minn:
            total += n
    print('#%d %d' % (t, round(total/8)))
```

## SWEA 1974. 스도쿠 검증(D2)

```python
tc = int(input())
for t in range(1, tc+1):
    ans = 1
    check = [[0] * 10 for _ in range(27)]
    for i in range(9): # row
        row = [int(n) for n in input().split()]
        if ans == 0: continue
        for j in range(9): # col
            num = row[j]
            i2 = 9 + j
            i3 = 18 + i//3 * 3 + j//3
            if check[i][num] == 0 and check[i2][num] == 0 and check[i3][num] == 0:
                check[i][num] += 1; check[i2][num] += 1; check[i3][num] += 1
            elif check[i][num] != 0 or check[i2][num] != 0 or check[i3][num] != 0:
                ans = 0; break
    print(f'#{t} {ans}')
```

## SWEA 1970. 쉬운 거스름돈(D2)

```python
for i in range(int(input())):
    exchange = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f"#{i+1}")
    for j in money:
        if exchange // j == 0:
            print(0, end=" ")
        elif exchange // j >= 1:
            print(exchange // j, end=" ")
            exchange %= j
    print()
```

## swea1959. 두 개의 숫자열 (D2)

```python
tc = int(input())
for t in range(1, tc+1):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    if a > b:
        maxn = a; maxl = arr[:]
        minn = b; minl = brr[:]
    else:
        maxn = b; maxl = brr[:]
        minn = a; minl = arr[:]

    maxsum = 0
    for i in range(minn):
        maxsum += minl[i] * maxl[i]
    for i in range(1, maxn-minn+1):
        tmpsum = 0
        for j in range(minn):
            tmpsum += minl[j] * maxl[j+i]
        if tmpsum > maxsum:
            maxsum = tmpsum
    print('#%d %d' % (t, maxsum))
```



### SWEA 1961. 숫자 배열 회전(D2)

```python
def solve(mat, N):
    res = [[""] * 3 for _ in range(N)]
    # 90
    j = 0
    while j <= N - 1:
        i = N - 1
        while i >= 0:
            res[j][0] += mat[i][j]
            i -= 1
        j += 1
    # 180
    i = N - 1
    while i >= 0:
        j = N - 1
        while j >= 0:
            res[N - 1 - i][1] += mat[i][j]
            j -= 1
        i -= 1
    # 270
    i = N - 1
    while i >= 0:
        j = 0
        while j <= N - 1:
            res[N - 1 - i][2] += mat[j][i]
            j += 1
        i -= 1

    for i in range(N):
        print(' '.join(res[i]))

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    mat = [[] * N for _ in range(N)]
    for i in range(N):
        mat[i] = input().split()
    print(f'#{t}')
    solve(mat, N)
```

### SWEA 1983. 조교의 성적 매기기 (D2)

```python
T = int(input())
 
for case in range(1, T+1):
    firstInput = list(map(int, input().split()))
    students = firstInput[0]
    pergrade = students//10
    target = firstInput[1]
    point = [0] * students
    grade = [0] * students
    gradeslist = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for num in range(students):
        point[num] = list(map(int, input().split()))
        point[num] = (point[num][0] * 35 + point[num][1] * 45 + point[num][2] * 20, num+1)
     
    # 정렬 구현해보기
    point.sort()
    point.reverse()
     
    for num in range(10):
        targetgrade = gradeslist[num]
        for i in range(num*pergrade, (num+1)*pergrade):
            grade[i] = targetgrade
     
    for info in range(len(point)):
        if point[info][1] == target:
            print(f'#{case} {grade[info]}')
            break
```

## after6pm

### 문제4

0과 1이 들어있는 NxN 크기의 배열이 있다. 상하좌우 모두 0으로 둘러쌓인 1은 모두 몇 개인지 알아내는 프로그램을 만드시오. 반드시 상하좌우에 숫자가 존재하는 경우만 고려한다.

첫 줄에 N, 다음 줄부터 N줄에 걸쳐 N개의 숫자가 주어진다. 3<=N=10

입력 1

5

1 0 1 0 1

0 1 0 1 1

1 0 1 0 0

0 0 1 0 0

1 1 1 1 1

출력 1

1

**슈더코드**

``` python
cnt = 0
for i:1 -> N-2
    for j:1 -> N-2
        if A[i][j+1] == 0 and A[i+1][j] == 0 and A[i][j-1] == 0 and A[i-1][j] == 0:
            cnt += 1
            
        
```



### 문제5

NxN 구역의 높이를 기록한 표를 만들었다. 어떤 지역이 모든 이웃한 지역보다 높으면 봉우리라고 한다. 몇 개의 봉우리가 존재하는지 알아내는 프로그램을 만드시오. 이웃한 지역은 표에서 상하좌우, 양 대각선 방향을 포함해 모두 8곳이고, 이웃한 지역이 부족한 경우는 고려하지 않는다.

| 이웃 | 이웃 | 이웃 |
| ---- | ---- | ---- |
| 이웃 |      | 이웃 |
| 이웃 | 이웃 | 이웃 |

입력1

5

1 2 1 1 1

1 2 1 2 1

1 2 1 1 1

1 1 3 1 1

1 2 1 1 3

출력1

2



**슈더코드**

```python

#(i-1, j-1) (i-1, j) (i-1, j+1)
#(i, j-1)   (i, j)    (i, j+1)
#(i+1, j-1) (i+1, j) (i+1, j+1)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

def f(i, j)
        for k:0 -> 7
            ni = i + di[k]
            nj = j + dj[k]
        
            if A[i][j] <= A[ni][nj]
            	return 0
        return 1
a = []
cnt = 0
for i:1 -> N-2
    for j:1 -> N-2
        cnt += f(i, j)

            #    a.append(A[ni][nj])
        #if A[i][j] > max(a):
         #   cnt += 1
```



파리채? 슈더코드

```python
# 부분 배열의 왼쪽 위 모서리(i, j)
# 부분 배열의 크기 k = 3 일때
# [] 칸은 유효하다면

#(i, j)   [i, j+1]   (i, j+2)
#[i+1, j] (i+1, j+1) [i+1, j+2]
#(i+2, j) [i+2, j+1] (i+2, j+2)

for i in range(0, N-K+1):
    for j in range(0, N-K+1):
        for m in range(K):
            for n in range(K):
                if m%2 != n%2: # m과 n의 짝수 홀수면
                    s += arr[i+m][j+n]
        if maxV < s:
        	maxV = s
                    
                
```