[TOC]



## swea 5356. 의석이의 세로로 말해요 D3

```python
for T in range(int(input())):
    L = [list(input()) for _ in range(5)]
    a = max(map(len, L))
    for r in L:
        while len(r) < a:
            r.append('')
    re = ''.join([L[x][y] for y in range(a) for x in range(len(L))])
    print("#{} {}".format(T+1, re))
```



## swea 4615. 재미있는 오셀로 게임 D3

```python
'''
swea 4615 재미있는 오셀로 게임

'''
def is_not_limit(a, b, n):
    if a >= 0 and a < n and b >= 0 and b < n:
        return True
    else:
        return False


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    data = [[0] * N for _ in range(N)]
    data[N//2 - 1][N//2] = 1
    data[N//2][N//2 - 1] = 1
    data[N//2 - 1][N//2 - 1] = 2
    data[N//2][N//2] = 2

    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]

    for _ in range(M):
        a, b, stone = map(int, input().split())
        x = a - 1
        y = b - 1
        data[x][y] = stone
        for i in range(8):
            count = 0
            next_x = x + dx[i]
            next_y = y + dy[i]
            while is_not_limit(next_x, next_y, N) and stone != data[next_x][next_y] and data[next_x][next_y] != 0:
                count += 1
                next_x = next_x + dx[i]
                next_y = next_y + dy[i]

            if is_not_limit(next_x, next_y, N) and data[next_x][next_y] == stone:
                next_x = x + dx[i]
                next_y = y + dy[i]
                for f in range(count):
                    data[next_x][next_y] = stone
                    next_x = next_x + dx[i]
                    next_y = next_y + dy[i]

    count1 = 0
    count2 = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                count1 += 1
            elif data[i][j] == 2:
                count2 += 1
    print('#{} {} {}'.format(t, count1, count2))
```

**슈더 코드**

```python
12222210000
21111120000

1000001

12222222222

12222220001

```

## swea 5105 미로의 거리 D3

```python
def bfs(x, y, cnt):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1
    q = [(x, y, cnt)]
    ret = 0
    while q != []:
        cx, cy, cnt = q.pop(0)
        if (cx, cy) == (fx, fy):
            ret = cnt -1
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if maze[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    return ret

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    maze = [0] * N
    sx, sy = 0, 0
    fx, fy = 0, 0
    for i in range(N):
        maze[i] = list(map(int, list(input())))
        for j in range(N):
            if maze[i][j] == 2:
                sx, sy = i, j
            elif maze[i][j] == 3:
                fx, fy = i, j
    visited = [[0] * N for _ in range(N)]
    print('#{} {}'.format(t, bfs(sx, sy, 0)))
```

### 미로

오른쪽과 아래로만 이동하는 경우

- 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
- 출발은 맨 왼쪽 위, 도착은 맨 오른쪽 아래이다.
- 출발부터 도착까지 지나는 각 칸의 합계가 최소가 되도록 움직였을 때, 합계를 계산하라.
- 각 칸은 1에서 9 사이의 숫자.

```python
'''
슈더 코드

f(i, j, s)
	if 도착지면
		if minV > s + arr[i][j]
			minV = s + arr[i][j]
	else 도착지가 아니면
		# 아래로 이동
			if i + 1 < N:
				f(i + 1, j, s + arr[i][j])
		# 오른쪽으로 이동
			if j + 1 < N:
            	f(i, j + 1, s + arr[i][j])
	
'''
```



다음 칸의 좌표 계산

- 현재 위치가 (0, 0)이면, 갈 수 있는 칸은 (0, 1)이나 (1, 0)이다.
- 재귀 호출의 각 단계에서는 현재 위치를 저장한다.
- 오른쪽 칸으로 가는 경우와 아래로 가는 경우를 나누어 호출한다.
- 현재 칸까지의 숫자의 합을 구한다.

```python
f(row, col, sum)
{
    if(도착점이면)
    	if( sum+m[row][col] < min)
    		min = sum + m[row][col]:
    else
    if(col+1<N)
    	f(row, col + 1, sum + m[row][col])
    if(row+1<N)
    	f(row + 1, col, sum + m[row][col])
}
```





모든 칸을 지나지 않고 답을 찾는 방법

- 도착점이 아닌 경우, 지나온 숫자의 합이 min보다 크면 return.

```python
f(row, col, sum)
{
    if(도착점이면)
    	if(sum+m[row][col] < min)
    		min = sum + m[row][col]
    else if(sum + m[row][col] > min)
    	return;
    else
    	f(row, col + 1, sum + m[row][col])
    	f(row + 1, col, sum + m[row][col])
}
```



### 미로의 응용

배열에 저장한 미로

- 1-벽, 0-통로, S-출발, G-도착
- 도착 가능 여부 판단, 최단 거리 구하기, 경로의 수 구하기 등

미로에서의 이동



이동할 칸의 좌표 계산

```python
# 크기가 NxN인 2차원 배열일 때,
# 현재 위치(r, c)에서 새 좌표로 이동하기.

if(c+1 < N)
	next(r, c+1); # 우측
if(r+1 < N)
	next(r+1, c); # 아래쪽
if(c > 0)
	next(r, c-1); # 왼쪽
if(r > 0)
	next(r-1, c); # 위쪽
```



반복문을 이요한 이동할 칸의 좌표 계산

```c++
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};

...
for(i = 0 ; i < 4 ; i++)
{
    nr = r + dr[i];
    nc = c + dc[i];
    if((nr >= 0)&&(nr<N)&&(nc >= 0)%%(nc<N))
    {
        next(nr, nc);
    }
}
```



경로의 존재만 확인하는 경우

- 한번 지나간 칸은 표시를 해서 다시 들어가지 않는다.
- 일단 목적지에 도착하면 나머지 경로는 확인하지 않는다.



경로의 수를 찾는 경우

- 목적지에 도착 가능한 모든 경로를 지나야 한다.



미로와 그래프

BFS를 적용한 최단 거리 계산



NxN 미로에 대한 BFS적용

- map: 미로, 1: 벽

```python
BFS(r, c)
	dr[] = {0, 1, 0, -1}
    dc[] = {1, 0, -1, 0}
    enQ(r, c)
    v[r][c] = 1
    while(Q_is_not_empty())
    	t = deQ()
        for i : 0 -> 3
            r = t.r + dr[i]
            c = t.c + dc[i]
            if(r>0 && r<N && c>=0 && c<N)
            	if(map[r][c] != 1 && v[r][c] == 0)
                	enQ(r, c)
                    v[r][c] = v[t.r][t.c] + 1

   
```

## swea 1949. [모의 SW 역량테스트] 등산로 조성

```python
'''
swea 1949. [모의 sw 역량테스트] 등산로 조성
'''

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(x, y, use, leng):
    temp = leng
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            if data[x][y] > data[nx][ny]:
                temp = max(temp, dfs(nx, ny, use, leng + 1))
            elif data[x][y] <= data[nx][ny] and not use and data[x][y] > data[nx][ny] - K:
                temp_height, data[nx][ny] = data[nx][ny], data[x][y] - 1
                temp = max(temp, dfs(nx, ny, True, leng + 1))
                data[nx][ny] = temp_height
            visited[nx][ny] = False
    return temp

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    start = [0, set({})]
    for i in range(N):
        for j in range(N):
            if start[0] < data[i][j]:
                start[0] = data[i][j]
                start[1].clear()
                start[1].add((i, j))
            elif start[0] == data[i][j]:
                start[1].add((i, j))
    result = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for x, y in start[1]:
        visited[x][y] = True
        result = max(result, dfs(x, y, False, 1))
        visited[x][y] = False
    print('#{} {}'.format(T, result))
```

