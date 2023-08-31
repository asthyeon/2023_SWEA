import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    # 숫자열 A 길이 N, 숫자열 B 길이 M
    N, M = map(int, input().split())

    # A 숫자열 받기
    A = list(map(int, input().split()))

    # B 숫자열 받기
    B = list(map(int, input().split()))

    # 최댓값
    result = 0

    # 현재 상태의 최댓값을 구하기
    if N > M:
        for k in range(M):
            result += A[k] * B[k]
    else:
        for k in range(N):
            result += A[k] * B[k]

    # 더 짧은 숫자열의 위치를 한칸씩 밀며 최댓값을 구하기
    if N > M:
        for m in range(1, N - M + 1):
            plus = 0
            for n in range(M):
                plus += A[n + m] * B[n]
            # 최댓값 교체
            if result < plus:
                result = plus
    # 같다면 패스
    elif N == M:
        pass
    else:
        for o in range(1, M - N + 1):
            plus = 0
            for p in range(N):
                plus += A[p] * B[p + o]
            # 최댓값 교체
            if result < plus:
                result = plus

    print(f'#{tc} {result}')


