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

