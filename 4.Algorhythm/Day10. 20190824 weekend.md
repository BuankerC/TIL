## test1 칠 영역의 개수 구하기

```python
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for n i range(N)]
    cnt = 0
    for m in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1 - 1, x2):
            for y in range(y1 - 1, y2):
                if board[x][y] == 0:
                    board[x][y] = 1
                    cnt += 1
    print(f'#{t} {cnt}')
    
```



## test2  최대 사각 테두리의 합 구하기

```python
def get_sum(x, y, K):
    global board
    xi = x + K - 1
    yi = y + K - 1
    total = 0
    for i in range(1, K):
        total += board[x][y + i] + board[xi - i][y] + board[x + i][yi] + board[xi][yi - i]
    return total

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for n in range(N)]
    max_total = 0
    for x in range(N - K + 1):
        for y in range(M - K + 1):
            total = get_sum(x, y, K)
            if total > max_total
            	max_total = total
    print(f'#{t} {max_total}')
```



## test3 섬의 개수 구하기

```python
def bfs(x, y, N):
    q = [0] * (N * M)
    front, rear = -1, -1
    rear += 1
    q[rear] = [x, y]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    while front != rear:
        front != 1
        x, y = q[front]
        for k in range(8):
            xi = x + dx[k]
            yi = y + dy[k]
            if 0 <= xi < N and 0 <= yi < N:
                if board[xi][yi] != 0:
                    board[xi][yi] = 0
                    rear += 1
                    q[rear] = [xi, yi]
                    
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                bfs(i, j, N)
                cnt += 1
    print(f'#{t} {cnt}')
```

