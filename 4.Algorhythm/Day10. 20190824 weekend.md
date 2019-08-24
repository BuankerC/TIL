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



## swea 2070. 큰 놈, 작은 놈, 같은 놈(D1)

```python
t = int(input())
for i in range(1,t + 1):
    a, b = map(int, input().split())
    print(f'#{i} ', end="")
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
```



## swea 2056. 연월일 달력 D1

```python
t = int(input())
for i in range(1, t+1):
    test = input()
    
    m1 = ['01', '03', '05', '07', '08', '10', '12']
    m2 = ['04', '06', '09', '11']
    if  (test[4:6] in m1) and 1 <= int(test[6:]) <= 31:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    elif test[4:6] =='02' and 1 <= int(test[6:]) <= 28:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    elif (test[4:6] in m2) and 1 <= int(test[6:]) <= 30:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    else:
        print(f'#{i} -1')
```

## swea 2043. 서랍의 비밀번호 D1

```python
p, k = map(int, input().split())
print(p-k+1)
```

## swea 2025 N줄 덧셈 D1

```python
T = int(input())
total = 0
for i in range(T+1):
    total += i
print(total)
```

## swea 2027. 대각선 출력하기 D1

```python
print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')
```

## swea 2050. 알파벳을 숫자로 변환하기 D1

```python
for word in input():
    print(ord(word)-64, end=' ')
```



## ord

ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.

> ※ ord 함수는 chr 함수와 반대이다.

```
>>> ord('a')
97
>>> ord('0')
48
```

**출처  위키독스 / 점프 투 파이썬**

## swea 2047. 신문 헤드라인 D1

```python
T = input()
print(T.upper())
```

## swea 1938. 아주 간단한 계산기 D1

```python
a, b = map(int,input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
```

## swea 1933. 간단한 N 의 약수 D1

```python
t = int(input())
for n in range(1, t + 1):
    if t % n ==0:
        print(n, end=' ') 
```

## swea 1936. 1대1 가위바위보 D1

```python
t = input()
leftwin = ['1 3', '2 1', '3 2']
if t in leftwin:
    print('A')
else:
    print('B')
```

## swea 2019. 더블더블 D1

```python
t = int(input())
for n in range(t+1):
    print(2 ** n, end=' ')
```

## swea 1545. 거꾸로 출력해보아요 D1

```python
t = int(input())
for i in range(t, -1, -1):
    print(i, end=' ')
```

