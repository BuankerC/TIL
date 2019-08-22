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

