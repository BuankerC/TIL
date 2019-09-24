[TOC]



test_1.py

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N+1)]

    for k in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2 + 1): #일곱 영역의 행
            for j in range(y1, y2 + 1): #일곱 영역의 열
                arr[i][j] = 1

    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                cnt += 1
    print('#{} {}'.format(tc, cnt))

```

test_2.py

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(0, N-K+1):
        for j in range(0, N-K+1): # 왼쪽 위 모서리 좌표
            s = 0
            for p in range(K):
                s += arr[i][j+p] # 부분 배열의 맨 윗줄
                s += arr[i+K-1][j+p] # 부분 배열의 맨 아랫줄
                s += arr[i+p][j] # 왼쪽 열
                s += arr[i+p][j+K-1] # 오른쪽 열

            s -= arr[i][j]
            s -= arr[i+K-1][j]
            s -= arr[i][j+K-1]
            s -= arr[i+K-1][j+K-1]
            if maxV < s:
                maxV = s

            # s = 0 # 두번째 방법
            # for r in range(i, i+K):
            #     for c in range(j, j+K):
            #         if r==i or r==i+K-1 or c==j or c==j+K-1
            #             s += arr[r][c]
            #
            # if maxV < s:
            #     maxV = s



    print('#{} {}'.format(tc, cnt))
```

test_3.py

```python
def f(i, j, N):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    global v
    v[i][j] = 1
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= and ni < N and nj >= 0 and nj < N:
            if v[ni][nj] == 0 and arr[ni][nj] > 0:
                f(ni, nj, N)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (arr[i][j] > 0 and v[i][j] == 0):
                f(i, j, N)
                cnt = cnt + 1

    print('#{} {}'.format(tc, cnt))
```

## swea1954. 달팽이 숫자(D2)

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

슈더코드

```python
# NxN 달팽이 배열

# 초기 값 : 이동 거리 K = N, 이동 방향 dir = 1

# 모든 칸이 채워질 때까지
#(1) 수평 이동 (+1)
#(1-2) 이동거리 1 감소
# K==0이 되면 중단.
#(2) 수직 이동 (+1) 후 이동 방향 반전. dir *= -1
#(1) 반복

```

선생님 코드

```python
c = 1
N = 5
k = N
dir = 1
arr = [[0]*N for _ in range(N)]
i = 0 #시각 칸의 인덱스
j = -1 # 현재 위치로부터 k번 이동해야 하므로
while(2):
    # 수평이동
    for h in range(k):
        j += dir
        arr[i][j] = c
        c += 1
    
    k -= 1 #이동 거리 감소
    if k == 0: #이동거리가 0이면 중단
        break
    #수직 이동
    for v in range(k):
        i += dir
        arr[i][j] = c
        c += 1

    dir *= -1 # 수직 -> 수평으로 바뀔 때 인덱스 증감 바꾸기
print(arr)
```

