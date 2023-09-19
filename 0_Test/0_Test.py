def perm(i, N):
    global min_v
    if i == N:
        tmp = sum(p)
        if tmp < min_v:
            min_v = tmp
        return

    for j in range(N):
        if used[j] == 0:
            used[j] = 1
            p[i] = arr[i][j]

            # 가지치기
            if sum(p) > min_v:
                p[i] = 0
                used[j] = 0
                continue
            perm(i + 1, N)
            used[j] = 0

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 T
for test in range(1, T + 1):
    N = int(input()) # 제품의 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    p = [0] * N
    min_v = 99 * N
    perm(0, N)
    print(f'#{test}', min_v)