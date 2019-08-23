T = int(input())
N, M = map(int, input().split())
# x1, x2, y1, y2 = []
K = [[list(map(int, input().split()))] for i in range]
width = 0
widthsum = 0
paper = 0
total = 0
# dx = K[x]
# dy = K[y]
for x in range(1, N - M + 1):
    for y in range(1, N-M+1):
        if K[x1, y1] != K[x2, y2]:
            width = abs((x2 - x1) * (y2 - y1))
        else:
            width = 1
            # 한 영역의 넓이 구하기
        for j in range(K):
            for k in range(K):
                # 여러 영역의 넓이 더하기
                if K[j1, k1] != K[j2, k2]:
                    widthsum = abs((j2 - j1) * (k2 - k1))

                # 여백 넓이 구하기

                if K(widthsum) != K(width):
                    pass
                else:
                    paper = abs(K(widthsum) - K(width))

# 총 면적 = 각 영역의 넓이 + 여백
total = width + widthsum - paper
# for dx in range(M):
#     for dy in range(M):
#         if dx[0], dy[0]
print('#{T} {total}'.format)