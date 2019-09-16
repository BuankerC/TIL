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

