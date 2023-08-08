import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    # 파리배열: NxN, 파리채배열: MxM
    N, M = map(int, input().split())
    # NxN 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 죽은 파리의 수중 가장 큰 값
    max_dead = 0

    # MxM 이 가장 큰 범위 구하기
    # arr[0, 0] 부터 시작
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 죽은 파리의 수 초기화
            dead = 0
            # MxM 배열 생성
            for k in range(i, M + i):
                for l in range(j, M + j):
                    dead += arr[k][l]
            # 죽은 파리의 수 비교
            if max_dead < dead:
                max_dead = dead

    print(f'#{tc} {max_dead}')
