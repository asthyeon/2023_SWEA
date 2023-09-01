import sys
sys.stdin = open('sample_input.txt')

"""
# 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 갯수의 최솟값 구하기
1. 한 줄 이상 흰색, 파란색, 빨간색
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 색깔 받기
    colors = [input() for _ in range(N)]

    # 칠해야할 색 최솟값
    cnt = 100000000

    # 칠해야할 색 수 세기
    W = [0] * N
    B = [0] * N
    R = [0] * N
    for i in range(N):
        for j in range(M):
            if colors[i][j] != 'W':
                W[i] += 1
            if colors[i][j] != 'B':
                B[i] += 1
            if colors[i][j] != 'R':
                R[i] += 1

    # 누적으로 순서대로 더하기
    for k in range(1, N):
        W[k] += W[k - 1]
        B[k] += B[k - 1]
        R[k] += R[k - 1]

    # 한 줄 이상씩 확보하여 색칠
    for m in range(N - 2):
        for n in range(m + 1, N - 1):
            W_painting = W[m]
            B_painting = B[n] - B[m]
            R_painting = R[N - 1] - R[n]
            # cnt 비교
            if cnt > W_painting + B_painting + R_painting:
                cnt = W_painting + B_painting + R_painting

    print(f'#{tc} {cnt}')

