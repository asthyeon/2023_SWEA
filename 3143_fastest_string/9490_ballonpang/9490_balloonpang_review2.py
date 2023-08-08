import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # i, j 인접에 대해
                for p in range(1, arr[i][j] + 1):
                    ni, nj = i + (di * p), j + (dj * p)
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj] # 주변 칸의 풍선 꽃가루 수
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')