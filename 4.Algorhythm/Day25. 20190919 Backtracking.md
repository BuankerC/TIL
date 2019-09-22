[TOC]



# 백트래킹(Backtracking)

## 개념

#### 여러가지 선택지들이 존재하는 상황에서 한 가지를 선택한다.

#### 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.



#### 이런 선택을 반복하면서 최종 상태에 도달한다.

- 올바른 선택을 계속하면 목표 상태(goal state)에 도달한다.



#### 당첨 리프 노드 찾기

- 루프에서 갈 수 있는 노드를 선택한다.
- 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작한다.
- 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다.
- 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 찾는 답이 없다.



#### 백트래킹과 깊이 우선 탐색과의  차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임.(Prunning 가지치기)
- 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단.
- 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제.
- <u>백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능</u>



#### 백트래킹 기법

- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감.
- 어떤 노드를 방문하였을 때, 그 노드를 포함한 경로가 해답이 될 수 없으면, 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
- 가지치기(pruning): 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다.



#### 일반 백트래킹 알고리즘

```c
checknode (node v)
    if promising( v )
        if there is a solution at v
        	write the solution
        else
        	for each child u of v
        		checknode( u )
```



#### 깊이 우선 검색 vs 백트래킹

- 순수한 깊이 우선 검색 = 155 노드
- 백트래킹 = 27 노드



#### 연습문제

- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.

```python
# k 주어진 원소의 개수,
# s는 n-1까지의 원소 중 부분 집합에 포함된 원소
# n 부분집합에 포함시킬지 고려하는 원소의 인덱스,
# m 찾고자 하는 부분집합의 합
# t 남은 구간의 합

def f(n, k, s, m, t):
    global cnt2  # 재귀 호출의 횟수 기록
    global cnt
    cnt2 += 1
    if s == m:  # 현재까지의 부분집합의 합이 찾고자 하는 합과 같은 경우
        cnt += 1  # 이후의 어떤 원소를 선택해도 10보다 크다
    elif n == k:  # 하나의 부분집합이 완성된 경우
        return
    elif s > m:  # 부분집합의 합이 찾는 값보다 커진 경우도 중단
        return
    elif s + t < m:  # 남은 원소를 모두 더해도 찾는 값에 못 미치는 경우
        return
    else:  # 고려할 원소가 남아있는 경우
        f(n+1, k, s + a[n], m, t-a[n])  # 부분집합에 포함시키는 경우
        f(n+1, k, s, m, t-a[n])  # n번 원소를 부분집합에 포함시키지 않는 경우


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
cnt2 = 0
f(0, len(a), 0, 10, sum(a))
print(cnt)
print(cnt2)
```



## 트리

#### 트리는 싸이클이 없는 무향 연결 그래프이다.

- 두 노드(또는 정점) 사이에는 유일한 경로가 존재한다.
- 각 노드는 최대 하나의 부모 노드가 존재할 수 있다.
- 각 노드는 자식 노드가 없거나 하나 이상이 존재할 수 있다.



#### 비선형 구조

- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조



## 트리 정의

#### 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.

1. 노드 중 부모가 없는 노드를 루트(root)라 한다.
2. 나머지 노드들은 n(>= 0)개의 분리 집합 T1, ... , TN으로 분리될 수 있다.

#### 이들 T1, ... , TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 서브 트리(subtree)라 한다.



## 트리 용어

#### 노드(node) : 트리의 원소이고 정점(vertex)라고도 한다.

#### 간선(edge) :  노드를 연결하는 선

#### 루트 노드(root node) : 트리의 시작 노드

#### 형제 노드(sibling node) : 같은 부모 노드의 자식 노드들

#### 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들

#### 서브 트리(subtree) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리

#### 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들



#### 차수(degree)

- 노드의 차수 : 노드에 연결된 자식 노드의 수
- 트리의 차수 트리에 있는 노드의 차수 중에서 가장 큰 값
- 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드

#### 높이

- 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
- 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨



### 이진 트리(Binary Tree)

#### 모든 노드들이 최대 2개의 서브 트리를 갖는 특별한 형태의 트리

#### 각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리

- 왼쪽 자식 노드
- 오른쪽 자식 노드



### 이진 트리 - 특성

#### 레벨 i에서의 노드의 최대 개수는 2개

#### 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2**(h+1)-1)개가 된다.



### 이진 트리 - 종류

#### 포화 이진 트리(Full Binary Tree)

#### 완전 이진 트리(Complete Binary Tree)

#### 편향 이진 트리(Skewed Binary Tree)



### 이진 트리 - 순회(traversal)

#### 순회(traversal)란 트리의 각 노드를 중복되지 않게 전부 방문하는 것을 말하는 데 트리는 비 선형 구조기 때문에 선형구조와 같이 선후 연결관계를 알 수 없다.



#### 3가지의 기본적인 순회 방법

- 전위 순회(preorder traversal) : VLR
  - 자손 노드보다 현재 노드를 먼저 방문한다.
- 중위 순회(inorder traversal) : LVR
  - 왼쪽 자손 노드, 현재 노드, 오른쪽 자손 노드 순으로 방문한다.
- 후위 훈회(postorder traversal) : LRV
  - 현재 노드보다 자손 노드를 먼저 방문한다.



#### 전위 순회(preorder traversal)

- 수행 방법
  1. 현재 노드 n을 방문하여 처리한다 : V
  2. 현재 노드 n의 왼쪽 서브트리를 순회한다 : L
  3. 현재 노드 n의 오른쪽 서브 트리를 순회한다 : R
- 전위 순회 알고리즘

```python
preorder_traverse (TREE T)
	if T is not null
    	visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```



#### 중위 순회(inorder traversal)

- 중위 순회 알고리즘

```python
inorder_traverse (TREE T)
	if T is not null
    	inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)
```



### swea 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3

```python
def solve(i, cnt):
    global mins
    if i == N:
        if cnt < mins:
            mins = cnt
        return
    for j in range(N):
        if not chk[j] and cnt + mat[i][j] <= mins:
            chk[j] = 1
            solve(i + 1, cnt + mat[i][j])
            chk[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))
    chk = [0] * N
    mins = 1500
    solve(0, 0)
    print('#{} {}'.format(tc, mins))
```

슈더 코드

```python
'''
p[0] A공장에서 만드는 물건
p[1] B공장에서 만드는 물건
p[2] C공장에서 만드는 물건

cost[p[0]][0]
'''
```



### swea 2806. N-Queen D3

```python
def nqueen(dep, n, history):
    global cnt
    if dep == n:
        cnt += 1
    else:
        for i in range(n):
            if i not in history:
                for index, value in enumerate(history):
                    if abs(dep - index) == abs(i - value):
                        break
                else:
                    history.append(i)
                    nqueen(dep + 1, n, history)
                    history.remove(i)
for t in range(int(input())):
    cnt = 0
    nqueen(0, int(input()), [])
    print('#{} {}'.format(t+1, cnt))
```



선생님 코드

```python
def f(i, N):
    global cnt
    if i==N:
        cnt += 1
    else:
        for j in range(N):
            if col[j]==0 and diag1[i+N-1-j]==0 and diag2[i+j]==0:
                col[j] = 1
                diag1[i + N - 1 - j] =1
                diag2[i + j] =1
                f(i+1, N)
                col[j] = 0
                diag1[i + N - 1 - j] = 0
                diag2[i + j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    col = [0]*N
    diag1 = [0]*2*N
    diag2 = [0]*2*N
    f(0, N)
    print('#{} {}'.format(tc, cnt))
```



슈더 코드

```python
f(i, N)
	if i == N:  # 모든 줄에 퀸을 놓으면
    	cnt += 1
    else:
        for j : 0 -> N - 1
            if col[j] == 0 and right[i + j] == 0 and left[i-j+N-1] == 0
            # 다른 줄에 j번 열에 퀸이 없어야 하고
            # 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
            #board[i][j] = 1
            col[j] = 1  # 현재 줄에서 j열을 사용함으로서 표시
            right[i+j] = 1
            left[i-j+N-1]
            f(i + 1, N)  # j열에 놓을 수 있으면 다음 줄로 이동
            col[j] = 0
            right[i+j] = 0
            left[i-j+N-1] = 0
            #board[i][j] = 0
f(0, N)
```



### 백준 13460 구슬 탈출 2

```python
from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    _rx, _ry, _bx, _by = [0]*4
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                _rx, _ry = i, j
            elif a[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True

def move(_x, _y, _dx, _dy, _c):
    while a[_x+_dx][_y+_dy] != '#' and a[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if a[nbx][nby] == 'O':
                continue
            if a[nrx][nry] == 'O':
                print(d+1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)

init()
bfs()
```



선생님 코드

```python
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# n 기울인 횟수
# c 빠져나온 구슬 정보   R 1, B 2, R+B 3

def f(n, iR, jR, iB, jB, c, dir):
    global minV
    if c==1: # 빨간공만 빠져 나온 경우
        if minV>n:
            minV = n
    elif c>1: # 파란공이 빠져 나오거나 둘 다 나온 경우
        return
    elif n==10: # 10번을 움직인 경우
        return
    else: # 각 방향으로 기울이기
        for k in range(4):
            p = [iR, jR, iB, jB]
            if dir==-1 or (k!= dir and k!=(dir+2)%4): # 이전 방향이나 반대 방향이 아닌 경우
                c, p = move(p, k) # 구슬 이동
                if c==0 and iR==p[0] and jR==p[1] and iB==p[2] and jB==p[3]: # 구슬이 움직이지 않은 경우
                    continue
                else:
                    f(n+1, p[0], p[1], p[2], p[3], c, k)

def move(p, d):
    niR, njR = p[0], p[1]
    niB, njB = p[2], p[3]
    cnt = 0
    while(bd[niR+di[d]][njR+dj[d]]!='#' and bd[niR+di[d]][njR+dj[d]]!='O'):
        niR, njR = niR+di[d], njR+dj[d]
    if bd[niR+di[d]][njR+dj[d]]=='O':
        cnt += 1
    while(bd[niB+di[d]][njB+dj[d]]!='#' and bd[niB+di[d]][njB+dj[d]]!='O'):
        niB, njB = niB+di[d], njB+dj[d]
    if bd[niB+di[d]][njB+dj[d]]=='O':
        cnt += 2

    if cnt>0:

        return cnt, p # 빠져나간 구슬 갯수 리턴
    #구슬이 겹치면 원래 순서 유지

    if niR==niB and njR==njB:
        if d == 0: # 오른쪽인 경우, column 비교
            t1 = njR - 1 if p[1]<p[3] else njR # B가 오른쪽이면
            t3 = njB if p[1]<p[3] else njB-1
            p = [niR, t1, niB, t3]
        elif d == 1: # 아래쪽인 경우, row 비교
            t0 = niR -1 if p[0]<p[2] else niR # B가 아래면
            t2 = niB if p[0]<p[2] else niB -1
            p = [t0, njR, t2, njB]
        elif d == 2: # 왼쪽인 경우 column 비교
            t1 = njR if p[1] < p[3] else njR + 1  # B가 오른쪽이면
            t3 = njB+1 if p[1] < p[3] else njB
            p = [niR, t1, niB, t3]
        elif d == 3: # 위쪽인 경우, row 비교
            t0 = niR if p[0]<p[2] else niR +1# B가 아래면
            t2 = niB+1 if p[0]<p[2] else niB
            p = [t0, njR, t2, njB]
    else:
        p = [niR, njR, niB, njB]
    return cnt, p

N, M = map(int, input().split())
bd = [list(input()) for _ in range(N)]
R = []
B = []
for i in range(N):
    for j in range(M):
        if bd[i][j]=='R':
            R.append(i)
            R.append(j)
            bd[i][j] = '.'
        if bd[i][j]=='B':
            B.append(i)
            B.append(j)
            bd[i][j] == '.'
minV = 11
f(0, R[0], R[1], B[0], B[1], 0, -1)
if minV == 11:
    minV = -1
print(minV)
```



## 백준 14502 연구소

```python
import copy
import sys

n = m = 0
arr = []
virusList = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0

def getSafeArea(copied):
    safe = 0
    for i in range(n):
        for j in range(m):
            if copied[i][j] == 0:
                safe += 1
    return safe

def spreadVirus(x, y, copied):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if copied[nx][ny] == 0:
                copied[nx][ny] = 2
                spreadVirus(nx, ny, copied)

def setWall(start, depth):
    global maxVal

    if depth == 3:
        copied = copy.deepcopy(arr)

        length = len(virusList)
        for i in range(length):
            [virusX, virusY] = virusList[i]
            spreadVirus(virusX, virusY, copied)

        maxVal = max(maxVal, getSafeArea(copied))
        return

    for i in range(start, n * m):
        x = (int) (i / m)
        y = (int) (i % m)

        if arr[x][y] == 0:
            arr[x][y] = 1
            setWall(i + 1, depth + 1)
            arr[x][y] = 0

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                 virusList.append([i, j])

    setWall(0, 0)
    print(maxVal)
```

슈더 코드

```python
# 3개의 기둥을 세울 칸의 번호를 정한다.

for i in range(N * M - 2):  # 첫번째 기둥
    if lab[i // M][i % M] == 0:  # 기둥을 세울 수 있으면
        for j in range(i + 1, N * M - 1):  # 두번째 기둥
            if lab[j // M][j % M] == 0:
                for k in range(j + 1, N * M):  # 세번째 기둥
                    if lab[k // M][j % M] == 0:
                        lab[i // M][i % M] = 1  # 해당위치에 기둥을 세우고
                        lab[j // M][j % M] = 1
                        lab[k // M][j % M] = 1
                        bfs(lab, N, M)
                        lab[i // M][i % M] = 0  # 다른 위치에 기둥을 세우려면
                        lab[j // M][j % M] = 0
                        lab[k // M][j % M] = 0
```













