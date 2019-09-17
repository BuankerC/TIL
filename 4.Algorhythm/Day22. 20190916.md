### swea 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

슈더코드

```python
'''
s = '47FE' -> 4, 7, 15, 14로 바꾸면서 
b3, b2, b1, b0를 차례로 검사
for i in range(N):
	if '0' <= s[i] <= '9':
		digit = ord(s[i]) - ord('0')
	else: # 'A' <= s[i] <= 'F'
		digit = ord(s[i]) - ord(s[i]) - ord('A') + 10
	for j in range(3, -1, -1):
		if digit & (1 << j) == 0:
			print('0', end='')
		else:
			print('1', end='')
		
'''
```

코드

```python
T = int(input())
for tc in range(1, T+1):
    N, hexn = input().split()
    N = int(N)
    binn = ''
    for i in range(N):
        for j in range(3, -1, -1):
            if int(hexn[i], 16) & 1 << j:
                binn += '1'
            else:
                binn += '0'
    print('#{} {}'.format(tc, binn))
```



### swea 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

슈더코드

```python
'''
0.625 * 2 = 1.25  1
0.25 * 2 = 0.5    0
0.5 * 2 = 1.0     1

'''
```

코드

```python
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    c = -1
    while N != 0:
        if c == -13:
            ans = 'overflow'
            break
        if N >= 2 ** c:
            ans += 1
            N -= 2 ** c
        else:
            ans += '0'
        c -= 1
    print('#{} {}'.format(tc, ans))
    
```

### swea 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔 D5

```python
'''
swea 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔 D5
'''

Conversion = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
         '4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

decryption = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}

def reduce(c, b, a):
    min_num = min(c,b,a)
    c //= min_num
    b //= min_num
    a //= min_num
    return str(c)+str(b)+str(a)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Scannner = [input() for _ in range(N)]

    Binary_lst = [''] * N
    for i in range(N):
        for j in range(M):
            Binary_lst[i] += Conversion[Scannner[i][j]]
    # print(Binary_lst)

    result = []
    visited = []
    ans = 0
    for y in range(N):
        a = b = c = 0
        for x in range(M*4-1, -1, -1):
            if b == 0 and c == 0 and Binary_lst[y][x] == '1':
                a += 1
            elif a > 0 and c == 0 and Binary_lst[y][x] == '0':
                b += 1
            elif a > 0 and b > 0 and Binary_lst[y][x] == '1':
                c += 1

            if a > 0 and b > 0 and c > 0 and Binary_lst[y][x] == '0':
                result.append(decryption[reduce(c, b, a)])
                a = b = c = 0

            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
                        (result[1] + result[3] + result[5]) + result[7]

                if value % 10 == 0 and result not in visited:
                    ans += sum(result)

                visited.append(result)
                result = []

    print('#%d %d'%(tc, ans))
```

선생님 코드

```python

```

