[TOC]



## 모의 테스트 리뷰

**슈더 코드**

```python
# T
# N M K 행 열 칠한 횟수
# r1 c1 r2 c2

# 문제 조건
# 좌표 (0, 0) - > (N-1, M-1)
# 칠하는 조건 : 새로운 영역의 명도가 크면 칠할 수 있음, 칠하려는 영역에 칠해진 명도가 크면 칠할 수 없음
# 너비가 1인 경우도 있음
# 명도 범위 0 ~ 10

# 출력
# 가장 넓게 칠해진 명도에 해당하는 칸 수

# 풀이
# NxM 빈 배열을 준비하고 일단 칠한다.
# => 칠할 수 있는 영역인지 확인한다(명도가 더 큰 칸이 있는 지 확인)
# 명도가 더 큰 칸이 없으면 칠함.
# 전체 영역에 대해 각 명도의 개수를 기록한다. 0~10번 카운트 배열 작성
# 카운트 배열에서 가장 큰 값을 출력한다.

```

리뷰 코드

```python
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]  # 0으로 칠해진 영역
    DRAW = [[int(num) for num in input().split()] for _ in range(K)]
    for i in range(K):  # 칠하기
        # a, b, c, d, e = map(int, input().split())
        a, b, c, d, e = DRAW[i][0], DRAW[i][1], DRAW[i][2], DRAW[i][3], DRAW[i][4]
        # 해당 영역에 더 큰 명도로 칠해진 칸이 있는 지 확인
        result = 0
        for row in range(a, c+1):
            for col in range(b, d+1):
                if board[row][col] > e:
                    result = 1
        # 칠할 수 있으면 칠함
        if result == 0:  # 더 큰 명도가 없었으면
            for row in range(a, c + 1):
                for col in range(b, d + 1):
                    board[row][col] = e
    # 명도 개수 기록
    bright = [0]*11
    for i in range(N):
        for j in range(M):
            bright[board[i][j]] += 1
    print('#{} {}'.format(tc, max(bright)))
```

보충 문제 슈더 코드

```python
# 기지국과 집 위치를 2차원 리스트에 저장한다.
# 모든 영역에서 기지국을 찾는다.
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A' or 'B' or 'C':
            
# 기지국 타입에 따라 커버되는 집을 지운다.
            
            cover('기지국')
# 전체 영역에 남은 집의 개수를 출력한다.
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'H'
            cnt += 1
print(cnt)
            
```

