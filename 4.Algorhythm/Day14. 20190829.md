### swea 4014. [모의 SW 역량테스트] 활주로 건설

**혁준 코드**

```python
def check_line(line, N, X):
    fake_road = [0] * N
    for i in range(0, N - 1):

        diff = abs(line[1] - line[i + 1])

        # 두 개가 다르면
        if diff ==1:

            std = line[i]
            right = line[i + 1]

            # 왼쪽이 더 높을 때, 도로 건설은 i+1부터 +1씩이다.
            if std > right and i + X < N:
                for x in range(i + 1, i + X + 1):
                    # 해당 라인의 x자리가 기준보다 높이가 다르거나, 이미 도로 건설 안된곳.
                    if line[x] == right and fake_road[x] == 0:
                        fake_road[x] = 1
                    else:
                        return False

            # 오른쪽이 더 높을 때 도로건설은 i부터 -1씩이다.
            elif std < right and 0 <= i + 1 - X:
                for x in range(i, i - X, -1):
                    if line[x] == std and fake_road[x] == 0:
                        fake_road[x] = 1
                    else:
                        return False
            else:
                return False
        # 같으면
        elif diff == 0:
            continue

        # 단차가 1 초과
        else:
            return False # 불가능한 경우

    return True

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for row in land:
        if check_line(row, N, X):
            count += 1

    col_land = list(zip(*land))

    for col in col_land:
        if check_line(col, N, X):
            count += 1

    print('#{} {}'.format(tc, count))
```

### swea 7964. 부먹왕국의 차원 관문 D3

**선만 코드**

```python
for t in range(int(input())):
    number_castles, limit_distance = map(int, input().split())
    status = ''.join(input().split())
    ans = 0
    distances = list(map(len, status.split('1')))
    for distance in distances:
        ans += distance // limit_distance
    print('#{} {}'.format(t + 1, ans))
```



### swea 5789. 현주의 상자 바꾸기 D3

```python
for t in range(int(input())):
    N,Q=map(int,input().split())
    ans=['0']*N
    for i in range(Q):
        L,R=map(int,input().split())
        for j in range(L-1,R):
            ans[j]=str(i+1)
    print(f"#{t+1} {' '.join(ans)}")
```

### swea 7964. 부먹왕국의 차원 관문 D3

**정우 코드**

```python
T = int(input())
for t in range(1, T + 1):
    N, D = map(int, input().split())
    gate = [1] + list(map(int, input().split()))
    i = 0
    cnt = 0
    out = False
    while 1:
        temp = []
        for j in range(1, D + 1):
            if i + j > N:
                out = True
                break
            if gate[i+j] == 1:
                temp.append(i + j)
        if out:
            break
        if temp == []:
            i = i + D
            cnt += 1
        else:
            i = temp[-1]
        if i > N:
    please(cnt)
```

###  swea 2805. 농작물 수확하기 D3

슈더 코드

```python
ct = N//2
for i : 0 -> N - 1
    if i <= ct:
        for j : 0 -> N - 1
            if j >= ct-i and  j <= ct+1
            s += arr[i][j]
    else:
        for j: 0 -> N - 1
            if j >= ct-i and j <= ct+1
            	s+= arr[i][j]
```

혁준 코드

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, list(input()))) for _ in range(N)]

    half = N // 2

    total = 0

    x = 0
    for i in range(N):

        total += sum(farm[i][half - x:half + x + 1])

        if i >= half:
            x -= 1
        else:
            x += 1

    print("#{} {}".format(tc, total))
```



### swea 1860. 진기의 최고급 붕어빵 D3

```python
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N명의 손님, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음
    t = list(map(int, input().split()))

    sell = [0] * 11112 # 시간별 판매량
    for i in t:
        sell[i] += 1
    fish = 0
    for i in range(11112):
        if i > 0 and i % M == 0:  # i시간 재고 계산
            fish += K
        fish -= sell[i]  # 시간 별로 판매
        if fish < 0:
            break

    if fish < 0:
        print('#{} Impossible'.format(tc))
    else:
        print('#{} Possible'.format(tc))
```

