T = int(input())
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
i = [1, 1, 0, -1, -1, -1, 0, 1]
j = [0, -1, -1, -1, 0, 1, 1, 1]
cnt = 0
sum1 = A([i+1, j] + [i+1, j-1] + [i-1, j-1] + [i-1, j] + [i-1, j+1] + [i, j+1] + [i+1, j+1])

for i in range(1, N-M+1):
    for j in range(1, N-M+1):
        if A([i+1, j] + [i+1, j-1] + [i-1, j-1] + [i-1, j] + [i-1, j+1] + [i, j+1] + [i+1, j+1]) = max:
            cnt += A([i+1, j] + [i+1, j-1] + [i-1, j-1] + [i-1, j] + [i-1, j+1] + [i, j+1] + [i+1, j+1])
        for k in range(M):
            for l in range(K):
                pass



print('#{T} {max(sum1)}'.format)

