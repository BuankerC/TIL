## 파리 퇴치 D2

중요함 시험문제 100

파리채에 구멍이 뚫려서 테두리만 남았을 때 최대 파리 잡는 개수



## 2005. 파스칼의 삼각형

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j==0 or i==j:
                arr[i][j] == 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        #     print(arr[i][j], end=' ') 값의 결정과 동시에 출력하는 경우
        # print()

    # 테이블 완성 후 출력하는 경우
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()
```



# 큐(Queue)

**큐의 특성**

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

  큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조

- 선입선출구조(FIFO: First In First Out)

**큐의 기본 연산**

- 삽입 : enQueue
- 삭제 : deQueue

**큐의 주요 연산**

enQueue(item) : 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산

deQueue() : 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산

createQueue() : 공백 상태의 큐를 생성하는 연산

isEmpty() : 큐가 공백상태인지를 확인하는 연산

isFull() : 큐가 포화상태인지를 확인하는 연산

Qpeek() : 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산



**선형 큐**

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front : 저장된 첫 번째 원소의 인덱스
  - rear : 저장된 마지막 원소의 인덱스
- 상태 표현
  - 초기 상태 : front = rear = -1
  - 공백 상태 : front = rear
  - 포화 상태 : rear = n-1 (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)

연습문제1

큐를 구현하여 다음 동작을 확인해 봅시다.

세 개의 데이터 1, 2, 3을 차례로 큐를 삽입하고

큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.



**선형 큐 이용시의 문제점**

- 잘못된 포화 상태 인식
  - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear = n-1 인 상태 즉, 포화 상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨.
- 해결방법 1
  - 매 연산이 이루어질 떄마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
  - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐
- 해결방법  2
  - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용

**원형 큐**

- 초기 공백 상태
  - front = rear =0
- index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
  - 이를 위해 나머지 연산자 mod를 사용함
- front 변수
  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

**연결 큐**



**우선순위 큐**

우선순위 큐의 특성

- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.



### 큐의 활용 : 버퍼(Buffer)



### BFS(Breadth First Search)

- 너비 우선 탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식



- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함.



### 연습문제 3

- 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다. 모든 정점을 너비우선탐색하여 경로를 출력하시오. 시작 정점을 1로 시작하시오.

- 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

- 출력 결과의 예는 다음과 같다.

  -1-2-3-4-5-7-6

```markdown
BFS(G, v) // 그래프 G, 탐색 시작점 v

    큐 생성

    시작 점 v를 큐에 삽입

    점  v를 방문한 것으로 표시

    while 큐가 비어있지 않은 경우

        t <- 큐의 첫 번째 원소 반환

        FOR t와 연결된 모든 선에 대해

            u <- t의 인접 정점

            u가 방문되지 않은 곳이면,

            u를 큐에 넣고, 방문한 것으로 표시
```

슈더 코드

```python
q = [0]*9 # 큐 생성
front = -1
rear = -1
rear += 1 #enq(1) # 시작점 인큐
q[rear] =1
visited[1] = 1 # 시작점 방문표시

while(front != rear): # 큐가 비어있지 않으면
    front += 1
    t = q[front] # 디큐
    # t의 인접이고 정점을 방문하지 않은 정점이면
    # 주어진 상황에 맞게 완성.
    # t 주변의 모든 i에 대해
    	if visited[i] == 0 and t에 i가 인접:
			...#enq(i)
            visited[i] = visited[t] + 1
```

## 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3

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

teacher's code

```python
    
def bfs(i, j, N):
    global maze
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    #초기화
    q = [] # 큐생성
    visited = [[0]*N for _ in range(N)] # visited 생성
    q.append([i,j]) # 시작점 인큐
    visited[i][j] = 1 # 시작점 방문표시

    #탐색
    while(len(q) != 0): # 큐가 비어있지 않으면 반복
        n = q.pop(0) # 디큐
        i, j = n[0], n[1]
        if maze[i][j] == '3': # visit()
            return visited[i][j] - 2
        # i, j에 인접하고 방문하지 않은 칸을 인큐
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N: # 미로를 벗어나지 않았고
                if maze[ni][nj]!='1' and visited[ni][nj]==0: # 벽이 아니고, 방문하지 않은 칸이면
                    q.append([ni, nj]) # 인큐
                    visited[ni][nj] = visited[i][j] + 1 # 방문 표시
    return 0                

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print('#{} {}'.format(tc, bfs(startI, startJ, N)))
```



### 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전 D2

```python
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))
    for i in range(M):
        Data.append(Data.pop(0))
    print(f'#{tc} {Data[0]}')
```



### 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 D2

```python
def BFS(start_node):
    global result
    Q.append(start_node)
    visited[start_node] = 1

    while Q:
        start_node = Q.pop(0)
        for next_node in range(1, v+1):
            if MyMap[start_node][next_node] and not visited[next_node]:
                Q.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node] + 1
                if next_node == end_node:
                    result = distance[next_node]
                    return
    return

TC = int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    MyMap = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    distance = [0] * (v+1)

    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1
        MyMap[end][start] = 1

    start_node, end_node = map(int, input().split())

    Q = []
    result = 0
    BFS(start_node)
    print(f'#{tc} {result}')

```

### 1979. 어디에 단어가 들어갈 수 있을까

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

슈더 코드

```python
1 1 1 1 0 0 1 1 0 1 1 0 1 1 1 0

# (1) 1이 연속된 경우는 몇 개?

# 주어진 리스트와 같은 길이의 used 리스트 생성
for i : 0 -> N - 3
    #arr[i]가 1이고 다른 연속 구간에 포함되지 않으면 1이 몇 개 연속인지 확인
    m = i # 연속된 1인지 확인하는 위치
    w = 0 # 연속된 1의 길이
    while(word[m]==1 and used[m]==0):
        used[m] = 1 # 연속된 1인지 확인된 구간
        m += 1
        w += 1
    if w == k:
        cnt += 1
        
```



### 1976. 시각 덧셈

```python

```



## 연속된 1의 개수

15 3
0 1 1 1 0 0 1 1 0 1 1 0 1 1 1
1 1 1 1 (4)
1 1 1 (3) -> 길이 4에 포함된 연속 1
[방법 1]
현재 위치에서 1이 시작되면
연속된 1의 개수를 확인. 
동시에 연속 구간에 포함되었음을 기록.
[방법 2]
(1)현재 위치에서 1이 시작되면
(2)연속된 1의 개수를 확인.
(3) 0이 나온 자리부터 새로운 1이 나올 때까지 이동
[방법 3]
(1) 1을 만나거나 리스트가 끝날 때까지 이동
(2) 1을 만나면 0을 만나거나 리스트가 끝날 때까지 이동하며 1의 개수를 셈
(3) (1) 반복 -> while문 
15 3
0 1 1 1 0 0 1 1 0 1 1 0 1 1 1
i 0 1 2 3 4 5 6 7 ...
cnt0 1 2 33 0 1 2 0 1 2 0 1 2 3
cntK	1	1 2