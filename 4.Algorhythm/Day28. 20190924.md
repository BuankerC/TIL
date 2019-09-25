[TOC]



#### 최소 이동거리 선생님 코드

```python
import sys

def dij(n):
    D = [99999999] * (n + 1)  # 0번까지의 거리
    D[0] = 0  # 출발점
    for x in adj[0]:
        D[x] = adj[0][x]  # D 초기화
    V = [0] * (n + 1)  # 거리를 결정한 노드 기록
    V[0] = 1  # 시작노드
    c = 0  # 처리된 노드 수
    while c < n:  # 출발을 빼고 n개가 처리되면 됨
        minV = 999999
        minidx = 0
        for i in range(n+1):
            if V[i] == 0 and D[i] < minV:
                minidx = i
                minV = D[i]
        V[minidx] = 1
        for x in adj[minidx]:
            if D[x] > (D[minidx] + adj[minidx][x]):
                D[x] = D[minidx] + adj[minidx][x]
        c += 1
        
    return D[n]

sys.stdin = open('input.txt', 'r')

```



#### 최소 비용 선생님 코드

```python
import sys

def find(N):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    D = [[10000000000] * N for i in range(N)]
    D[0][0] = 0
    q = []
    q.append((0, 0))
    while q:
        t = q.pop(0)
        for i in range(4):
            r = t[0] + dr[i]
            c = t[1] + dc[i]
            if r >= 0 and r < N and c >= 0 and c < N:
                diff = 0
                if H[r][c] > F[t[0]][t[1]]:
                    diff = H[r][c] - H[t[0]][t[1]]
                if D[r][c] > (D[t[0]][t[1]] + diff + 1):
                    D[r][c] = (D[t[0]][t[1]] + diff + 1)    
```

오늘 풀어볼 문제

swea7465 창용 마을 무리의 개수(상호배타집합)

swea 5521  상원이의 생일파티(그래프 탐색)

swea 1861 정사각형 방(그래프 탐색 응용)

swea 1795 인수의 생일파티(양방향 다익스트라)

swea 1244 최대 상금(옵션)



## 재귀

슈더코드

```python
'''
[1 2 3]

 v         v         v 
[1 2 3] [2 1 3] [3 2 1]
 ^       ^       ^
   v         v	
[1 2 3] [1 3 2]
 ^       ^
 
'''
```

- 1, 2, 3으로 3자리 수 만들기

```c
for (int i = 0; i < k; i++)
{
    if (used[i] == 0)
    {
        used[i] = 1;
        p[n] = a[i];
        f(n + 1, k);
        used[i] = 0;
    }
}
```

- {1, 2, 3, 4, 5의 원소를 한번씩만 사용해 3자리 수 만들기}
  - n : 고른 숫자를 저장할 위치
  - k : 골라야 할 숫자의 개수
  - m : 고를 수 있는 숫자의 개수

```c
f(n, k, m)
{
    if( n == k )
        ...
    else
    {
        for (int i = 0; i < m; i++)
        {
            if (used[i] == 0)
            {
                used[i] = 1;
                p[n] = a[i];
                f(n + 1, k)
                used[i] = 0;
            }
       }
    }
}
```



#### 문제 풀기

```
1. 딸기 케이크 딸기 배분 문제 : IM때 풀었던것 처럼
    - for i : 0 -> N-2
       - for j : 0 -> N- 2
            - f(0,0, i, j) # 왼쪽 위 영역
            - f(0,j+1, i, N-1)# 오른쪽 위 영역
            - f(i+1, 0, N-1, j) # 왼쪽 아래 영역
            - f(i+1, j+1,N-1,N-1) #  오른쪽 아래 영역
- 이를 이용해 최솟값, 최댓값 구하기

2. 그리드 내부의 가로줄 한줄의 총합과 세로줄 한줄의 총합 중 최소량 구하기
   - minV = 9999999
   - for i : 0->2 # 행
   - s1 = 0
   - s2 =0
   - for j :0 ->2
   - s1+= A[i][j] # 행의 합계
   - if minV > s1
   -    minV = s1
   - s2 += A[j][i] # 열의 합계
   - for i: 0 -> 2   # 열
   -    s2 = 0
   -    for j:0->2
   -        s2 += A[j][i]
   -        if minV > s2
   -            minV =s2
3. 4개의 섬이 각각 그리드 끝에 있을 때 가로 축과 세로축을 잇는 다리를 각각 하나 씩 만들 때의 최소 비용
    - M,N = map(int, input().split())
    - minV = INF
    - for i in range(3):
    -   for j in range(3):
    -       for k in range(3):
    -           s += A[i][k]
    -           s += A[k][j]
    -           s += A[i][j]
    -       if minV
4. 평탄화 높이 범위 1,2,3 일때 최소비용으로 평탄화, 같을 경우 더 낮은 높이
- 1) 높이를 1로 만드는 비용을 비교
- 2) 높이를 2로 만드는 비용을 비교
- 3) 높이를 3으로 만드는 비용을 비교
- .... n 높이 까지

minV = INF
minh = 0
for h : 1->3
    s = 0
    for i : 0 -> 2
        for j :0 ->2
            s += abs(A[i][j] - h)
            
            if minV > S
                minV = S
                minh = h
```



#### swea 1795 인수의 생일파티 슈더 코드

```python
'''
모든 노드에서 1번 노드에 도착하는 최소비용

D[] 생성
모든 i에 대해 1에 도착하는 초기비용
	D[i] = adj[i][1]
V[] 생성
V[1] = 1
모든 노드가 경유지로 고려될 때까지 반복
	V[w]가 0이고, D[w]가 최소인 w선택
	w로 진입하는 모든 노드 i에 대해
		w를 거쳐 1로 가는 비용과 기존의 비용 중 작은 쪽을 선택
		D[i] = min(D[i], adj[i][w] + D[w])
'''
```



#### 백준 17471 게리맨더링

슈더코드

```python
'''
N개의 원소에 대한 부분집합
[1, 2, 3]
      A          B
000  []        [1, 2, 3]
001  [3]       [1, 2]
010  [2]       [1, 3]
011  [2, 3]    [1]
100  [1]       [2, 3]
101  [1, 3]    [2]
110  [1, 2]    [3]
111  [1, 2, 3] []
'''
for i in range(1 << N):
    for j in range(N):
        if i & (1 << j) != 0:
            A.append(j+1)  # j+1을 선거구 번호로 활용 
        else:
            B.append(j+1)

# [[][2 4][1 3 6 5][4 2][1 3][ 2][ 2]]
            
            


```

#### 백준 17135 캐슬 디펜스

슈더코드

```python
maxV = 0
for i : 1 -> M - 2
    for j : i+1 -> M - 1
        for k : j+1 -> M
            kill = f(i, j, k)
            if maxV < kill
            	maxV = kill
```



#### SUM문제 변형

100 X100의 2차원 배열을 같은 높이로 만든다. 높이의 범위는 1 ~ 29이다.

이때 각 칸의 비용이 정해지면 이 비용으로 SUM 문제를 풀어본다.

SUM의 최소 값 구하기, 이 때의 높이 (최소 값이 같다면 더 낮은 높이)











