[TOC]



## swea 1983. 조교의 성적 매기기 D2

```python
import math
for s in range(1, int(input())+1):
    score_list = list(map(int, input().split()))
    n = score_list[0]
    k = score_list[1]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_list = []
    for i in range(1, n+1):
        score = list(map(int, input().split()))
        grade_list.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)
    j = n - 1
    for grade_check in grade_list:
        if grade_list[k-1] > grade_check:
            j -= 1
    i = math.floor(j/(n/10))
    print(f'#{s} {grade[i]}')
```



## swea 1859. 백만 장자 프로젝트 D2

``` python
T = int(input())
for tc in range(1, T + 1):
    days = int(input())
    prices = list(map(int, input().split()))
    
    max_price = prices[-1]
    temp = 0
    gain = 0
    
    for i in range(len(prices)-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            gain += (max_price - prices[i])
    print('#{} {}'.format(tc, gain))
```

## IM 모의 1번

```python
def share():
    d = int(input())
    lists = list(map(int, input().split()))
    min_p = min(lists[:-1])
    min_i = lists.index(min_p)
    max_p = max(lists[min_i+1:])
    return max_p - min_p

for tc in range(int(input())):
    print('#{} {}'.format(tc+1,share()))
```



## swea 1940. 가랏! RC카 D2

```python
tc = int(input())
for i in range(tc):
    command = int(input())
    distance = 0
    speed = 0
    for num in range(command):
        velocity = [int(v) for v in input().split()]
        if velocity[0] == 1:
            speed += velocity[1]
        elif velocity[0] == 2:
            speed -= velocity[1]
            
        if speed > 0:
            distance += speed
        else:
            speed = 0
            distance += speed
    print('#' + str(i + 1), distance)
```

