[TOC]



## 백준 1244. 스위치 켜고 끄기

문제의 번호와 인덱스의 번호를 일치시키자(스위치 번호가 0, 1이라서 인덱스 번호와 혼동이 올 수 있음)

```python
N = int(input())
sw = [0] + list(map(int, input().split())) # 스위치는 1번부터
M = int(input())
for i in range(M):
    s, c = map(int, input().split())
    if s == 1:  # 남학생일 때
        for j in range(1, N + 1):
            # if j % c == 0:
            if sw[i] == 0:
                sw[i] = 1
            else:
                sw[i] = 0
            # => sw[i] = (sw[i]+1) % 2
            # => sw[i] = 1 if sw[i]==0 else 0
        # j = 1
        # while(j * c <= N):
        #     sw[j * c] =sw([j * c] + 1) % 2
        #     j += 1
    else: # 여학생일 때, 스위치 번호를 중심으로 대칭인 구간을 반전
        sw[c] = (sw[c]+1) % 2  # 지정번호를 반전
        left = c - 1
        right = c + 1
        # 스위치 번호가 유효하고, 양 옆의 스위치 상태가 같으면
        while(left >= 1 and right <= N and sw[left] == sw[right]):
            sw[left] = (sw[left] + 1) % 2
            sw[right] = (sw[right] + 1) % 2
            left -= 1
            right += 1
        k = 1 # 스위치 개수로 관리하는 경우
        while(c-k >=1 and c+k <= N and sw[c-k] == sw[c+k]):
            sw[c-k]
            sw[c+k]
            k += 1
for i in range(1, N + 1):
    print('{}'.format(sw[i]), end = ' ')
    if(i % 20 == 0):
        print()
```

### 배열 탐색

슈더 코드

```python
for i in range(N):
    if arr[i] == 1:
        result = 1
        break

result = 0
for i in range(N):
    for j in range(N):
        if arr[i] == 1:
            result = 1
if result:
    
```



## SWEA 1289. 원재의 메모리 복구하기 D3

```python
tc = int(input())
for t in range(1, tc + 1):
    step = list(input())
    tmp = ['0'] * len(step)
    cnt = 0
    for i in range(len(step)):
        if step[i] != tmp[i]:
            cnt += 1
            for j in range(i, len(step)):
                tmp[j] = step[i]
    print('#{} {}'.format(t, cnt))
```



## swea 6190. 정곤이의 단조 증가하는 수 D3

```python

```



## 20190828 IM 기출 1

슈더코드

```python
# 어떤 방에 대한 조작으로 왼쪽의 방은 조작할 수 없다.
# 꺼진 상태에서 켜는 대신, 최종 상태에서 모두 꺼진 상태를 만들어 본다.
# 왼쪽 방부터 오른 쪽으로 가면서 켜져있는 스위치만 찾아서 끔

cnt = 0
for i : 1 -> N # 스위치가 켜져 있는지 확인
    if room[i] == 1: # i번 방이 켜져 있으면
        j = 1
        cnt += 1 # i번 방의 스위치를 끈 횟수
        while(i * j <= N): # i의 배수가 존재하는 방 번호일때
            room[i] = (room[i]+1) % 2 # 스위치 상태 반전
            j += 1
print(cnt)


```

## swea 6190. 정곤이의 단조 증가하는 수 D3

```python
def check(num):
    is_greater = True
    if not num // 10:
        return is_greater
    last = 9
    while num > 0:
        rest = num % 10
        if rest > last:
            num //= 10
    return is_greater

tc = int(input())
for t in range(1, tc + 1):
    N = int(input())
    nums = [0]
    nums += map(int, input().split())
    maxn = -1
    for i in range(1, N):
        for j in range(i+1, N+1):
            tmpn = nums[i] * nums[j]
            if check(tmpn) and tmpn > maxn:
                maxn =tmpn
    print('#{} {}'.format(t, maxn))
```

### SWEA 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

**슈더 코드**

```python
# (1) 정류장 번호를 인덱스로 하는 배열을 만들고, 입력된 충전기 위치를 표시한다.
# (2) 마지막 충전위치 last = 0 (출발지에는 충전기가 있음)
# 충전횟수 cnt = 0 (출발지 충전은 포함하지 않음)
# (3) last + K >= N (마지막 충전위치 + 운행거리가 종점을 지나면 종료)
# 따라서 last + K < N 인 동안 충전과 운행을 반복

# (4) last + K인 자리 next_stop에 충전기가 있으면
# last = last + K 방금 충전한 위치를 마지막 충전위치로 기록하고 
# cnt += 1 충전횟수 1 증가

# (5) last + K인 자리 next_stop에 충전기가 없으면
# 충전기를 찾을 때까지 next_stop 1감소

# - next_stop과 last가 같아지면 운행 불가
# - last에 다다르기 전에 next_stop에 충전기가 있으면
# 충전기가 있는 위치를 마지막 충전 위치로 기록 last = next_stop
# cnt += 1, (3)부터 반복
```

```python
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    stop = [0] * (N+1) # 충전기 위치 표시
    # for i in range(M):
    #     stop[charger[i]] = 1
    for i in charger:
        stop[i] = 1
    last = 0
    cnt = 0
    next_stop = last + K  # 최대로 이동 가능한 정류장
    while(last + K < N):  # 종점에 도착하기 전이면
        if stop[next_stop] == 0:  # 다음 최대 이동 거리에 충전기가 없으면
            next_stop -= 1
            if next_stop == last:  # 마지막 충전 위치까지 되돌아 오면
                break  # 운행 중단
        else:  # 마지막 충전 위치 이후에 충전기가 있으면
            last = next_stop  # 충전기를 마지막 충전 위치로 기록
            next_stop = last + K  # 현재 위치에서 최대 이동 가능 거리 계산
            cnt += 1  # 충전 횟수 1 증가

    if next_stop == last:  # 운행중단인 경우
        print('#{} 0'.format(tc))
    else:  # 종점에 도착한 경우
        print('#{} {}'.format(tc, cnt))
```

슈더코드 2

```python
# (1)충전기 위치만 저장, 마지막으로 충전한 충전기에서 최대로 이동할 수 있는 충전기(반드시 지나쳐야 하는 정류장)를 찾는 방식
# (출발지는 충전기가 있고, 종점은 충전기는 없지만 종점까지 갈 수 있는지 확인하기 위한 용도)

[0, 1, 3, 5, 7, 9, 10]

(1) stop[i] - stop[i-1] <= K
(두 충전기 사이 간격이 최대 이동거리 이내여야 함)
만약 stop[i] - stop[i-1] > K인 상황이면 운행 중단
(2) 마지막 충전 인덱스를 last라 하면,
stop[i] - stop[last] > K 
# 마지막 충전위치에서 갈 수 없는 인덱스 i에 다다르면, last = i - 1 이전 충전기에서 충전.
# (도착할 수 있는 충전기는 통과해서 다음 충전기로 가봄. 도착할 수 없는 충전기면 바로 이전에 통과한 충전기에서 충전)

```

```python
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stop = [0] + list(map(int, input().split())) + [N]
    last = 0  # 마지막 충전기 인덱스
    cnt = 0
    result = 1
    for i in range(1, M+2):
        if stop[i] - stop[i-1] > K:  # 두 충전기 거리가 K보다 크면 중단
            result = 0
            break
        else:
            if stop[i] - stop[last] > K:  # i번 충전기에 도착할 수 없으면
                last = i - 1  # 하나 전 충전기에서 충전하고
                cnt += 1  # 충전횟수 증가
    if result == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, cnt))
```





### swea 4837 [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

```python
TC  = int(input())
num = [1,2,3,4,5,6,7,8,9,10,11,12]
Len = len(num)

#부분집합 구하기
lst = []
for i in range(1<<Len):
    sub_lst = []
    for j in range(Len):
        if i & (1<<j):
            sub_lst.append(num[j])
    lst.append(sub_lst)


for tc in range(1, TC+1):
    N, K = map(int, input().split())

    #길이 맞는 리스트 구하기
    len_lst = []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)


    #합 일치 유무 확인
    result = 0
    for i in len_lst:
        if sum(i) == K:
            result += 1

    print('#%s %d'%(tc, result))
```

## swea 7510. 상원이의 연속 합 D3

슈더 코드

```python
# 합이 N이 되는 연속된 자연수의 후보
1+2+...
2+3+...
3+4+...
4+5+...
N
cnt = 0
for i : 1 -> N # 연속된 자연수의 시작 i,
    s = 0
    for j : i -> N # 연속된 자연수 j
        s += j
        if s == N:
            cnt += 1
            break
        elif s > N:
            break
print(cnt)
        

```

