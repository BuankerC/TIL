[TOC]



## swea 1954. 달팽이 숫자

슈더 코드

1) 오른쪽부터 시계방향으로 0, 1, 2, 3 방향이라 정함

2) 0번 방향으로 설정, 맨 왼쪽 위칸을 탐색 위치로 정함.

3) 설정 방향으로 탐색 시작

4) 현재 방향의 마지막 칸이거나, 다음 칸에 값이 있으면 다음 방향으로 변경

5) NxN 이내면 3) 반복

6) 더 이상 남은 칸이 없으면 종료

선생님 코드

```python
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # 빈 배열 만들기
    dir = 0
    i = 0 # 현재 칸 좌표
    j = 0
    k = 1 # 칸에 기록할 값
    while(k <= N*N): # 아직 NxN칸 이내면
        arr[i][j] = k #현재 칸에 값을 쓰고
        k += 1 # 다음 칸에 쓸 값 결정
        # 다음 칸을 결정, 배열을 벗어나지 않고 비어있어야 함.
        # 현재 방향을 다음 칸을 계산할 지, 다음 방향을 계산할 지 결정
        ni = i+di[dir]
        nj = j+dj[dir]
        if ni >= 0 and ni < N and nj >= 0 and nj < N and arr[ni][nj] == 0: # 벗어나지 않으면
            i, j = ni, nj
        else:
            dir = (dir + 1) % 4
            i += di[dir]
            j += dj[dir]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()
```



## swea 1974. 스도쿠 검증(D2)

```python
for tc in range(int(input())):
    lists = [list(map(int, input().split())) for _ in range(9)]
    lists_r = list(zip(*lists)) # zip은 세로로 배열 정렬
    count = 1
    for i in range(9):
        if len(set(lists[i])) != 9:
            count = 0
            break
        if len(set(lists_r[i])) != 9:
            count = 0
            break
    result = []
    for i in range(0, 9, 3):
        res = 0
        for j in range(3):
            res += sum(lists[i+j][i:i+3])
        if res != 45
            count = 0
            break
    print(f'#{tc+1} {count}')
```



## swea 1970. 쉬운 거스름돈 D2

```python
charges = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T + 1):
    result = []
    money = int(input())
    for charge in charges:
        mok = money // charge
        result.append(mok)
        money -= mok*charge

    print('#{}'.format(tc))
    for i in result:
        print(i, ends=' ')
    print('')
```



## swea 1959. 두 개의 숫자열 D2

**선생님 코드**

```python
def f(X, Y): # X 긴 리스트, Y 짧은 리스트
    maxV = 0
    for i in range(0, len(X)-len(Y)+1): # 긴 리스트에서 곱의 합을 구할 구간의 시작
        s = 0
        for j in range(0, len(Y)): # 짧은 리스트의 인덱스
            s += X[i+j]*Y[j]
        if maxV<s
            maxV = s
    return maxV
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        r = f(A, B)
    else:
        r = f(B, A)
    print('#{} {}'.format(tc, r))
```



## swea 1954 달팽이 숫자(D2)

```python
tc = int(input())
for t in range(1, tc+1):
	N = int(input())
	nums = [n for n in range(1, N**2+1)]
	ans = [[0] * N for _ in range(N)]

	x, y = 0, 0
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]
	dir_stat = 0 # 0: right, 1: down, 2: left, 3: up
	for i in range(N**2):
		ans[x][y] = nums[i]
		x += dx[dir_stat]
		y += dy[dir_stat]
		if x < 0 or x > N-1 or y < 0 or y > N-1 or ans[x][y]:
			x -= dx[dir_stat]
			y -= dy[dir_stat]
			dir_stat = (dir_stat + 1) % 4
			x += dx[dir_stat]
			y += dy[dir_stat]
	print('#%d' % t)
	for i in range(N):
		for j in range(N):
			print(ans[i][j], end=' ')
		print()
```

제출 코드

```python
tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    nums = [n for n in range(1, N**2+1)]
    ans = [[0] * N for _ in range(N)]

    x, y = 0, 0
    dx = [0, 1, -0 ,-1]
    dy = [1, 0, -1, 0]
    dir_stat = 0
    for i in range(N**2):
        ans[x][y] = nums[i]
        x += dx[dir_stat]
        y += dy[dir_stat]
        if x < 0 or x > N-1 or y < 0 or y > N-1 or ans[x][y]:
            x -= dx[dir_stat]
            y -= dy[dir_stat]
            dir_stat = (dir_stat + 1) % 4
            x += dx[dir_stat]
            y += dy[dir_stat]
    print('#%d' % t)
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end = ' ')
        print()
```



## swea 1948. 날짜 계산기 D2

```python
tc = int(input())
for t in range(1, tc+1):
    m1, d1, m2, d2 = map(int, input().split())
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m1 == m2:
        ans = d2 - d1 + 1
    else:
        ans = days[m1] - d1 + d2 + 1
        for m in range(m1+1, m2):
            ans += days[m]
    print('#%d %d' % (t, ans))
```

## swea 4828 min max D2

```python
def get_max(init_num):
    my_max = init_num[0]
    for i in range(1, len(init_num)):
        if my_max < init_num[i]:
            my_max = init_num[i]

    return my_max

def get_min(init_num):
    my_min = init_num[0]
    for i in range(1,len(init_num)):
        if my_min > init_num[i]:
            my_min = init_num[i]

    return my_min

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    init_num = list(map(int, input().split()))
    result = get_max(init_num) - get_min(init_num)
    print(f'#{tc} {result}')
```

## swea 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = input()
    card = [0] * 10
    for i in range(0, N):
        v = int[num[i]]
        card[v] = card[v] + 1

    maxIdx = 0
    for i in range(0, 10):
        if(card[maxIdx] <= card[i]):
            maxIdx = i
    print('#{} {} {}'.format(tc. maxIdx, card[maxIdx]))
```

## swea 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

```python
T = int(input())
for tc in range(1, T + 1):
    input()
    scores = list(map(int, input().split()))
    cnt = {}
    for score in scores:
        if score in cnt:
            cnt[score] += 1
        else:
            cnt[score] = 1
    ans = -1
    maxcnt = -1
    for k, v in cnt.items():
        if v > maxcnt:
            maxcnt = v
            ans = k
    print('#{} {}'.format(tc, ans))
```

## swea 1945. 간단한 소인수분해

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N % 2 == 0:
        N //= 2
        a += 1
    while N % 3 == 0:
        N //= 3
        b += 1
    while N % 5 == 0:
        N //= 5
        c += 1
    while N % 7 == 0:
        N //= 7
        d += 1
    while N % 11 == 0:
        N //= 11
        e += 1
    print('#%d %d %d %d %d %d' % (t, a, b, c, d, e))
```

## swea 1946. 간단한 압축 풀기 D2

```python
tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    st = ' '
    for i in range(n):
        a, b = input().split()
        st += a * int(b)
    print(f'#{t}')
    for i in range(len(st)):
        print(st[i], end='')
        if i % 10 == 9:
            print()
    print()
```



## swea 1928. Base64 Decoder D2

```python
keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
table = {value: index for index, value in enumerate(keys)}

for t in range(int(input())):
    base = list(input())
    decode = []
    binary = []
    binary24 = []
    for i in base:
        decode.append(table[i])
    for i in decode:
        a = bin(i)[2:]
        while len(a) < 6:
            a = '0' + a
        binary.append(a)
    for n in range(0, len(binary), 4):
        binary24.append(binary[n] + binary[n + 1] + binary[n + 2] + binary[n + 3])
    string = ''
    for m in binary24:
        string += chr(int(m[0:8], 2))
        string += chr(int(m[8:16], 2))
        string += chr(int(m[16:24], 2))
    print('#' + str(t + 1), string)
```

### swea 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3

**슈더 코드**

```python
# (1) 1개의 열에 대해
# (2) N극을 만날 때까지 아래로 탐색
# - 맨 아랫줄에 이르면 다음 열에 대해 (1)부터 반복
# (3) s극 자성체를 만날 때까지 아래로 탐색
# (4) 맨 아랫줄에 이르면 다음 열에 대해 (1)부터 반복
# (5) 중간에 s극을 만나면 교착 개수를 1 증가하고,
# 다시 해당 위치부터 (2)를 반복
```

