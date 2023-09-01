import sys
sys.stdin = open('in1.txt')

"""
# 한 번에 잡을 수 있는 최대 파리 수 출력
1. M 의 세기로 십자가 모양 or X자 모양으로 스프레이 분사
2. 뿌려진 일부가 영역을 벗어나도 상관 없음
"""

T = int(input())
for tc in range(1, T + 1):
    # 파리 배열: N, 분사 세기: M
    N, M = map(int, input().split())

    # 파리 배열 형성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 파리 죽은 수
    dead_max = 0
    # 십자가 분사(분사 시작점과 끝점을 잘 잡기)
    for x in range(N):
        for y in range(N):
            # 파리 죽은 수
            dead = arr[x][y]
            # 델타탐색
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                # 변수 교체
                nx, ny = x, y
                for _ in range(M - 1):
                    nx, ny = nx + dx, ny + dy
                    # 벽 형성
                    if 0 <= nx < N and 0 <= ny < N:
                        dead += arr[nx][ny]
            # 최대값 교체
            if dead_max < dead:
                dead_max = dead

    # X 자 분사
    for x in range(N):
        for y in range(N):
            # 파리 죽은 수
            dead = arr[x][y]
            # 델타탐색
            for dx, dy in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                # 변수 교체
                nx, ny = x, y
                for _ in range(M - 1):
                    nx, ny = nx + dx, ny + dy
                    # 벽 형성
                    if 0 <= nx < N and 0 <= ny < N:
                        dead += arr[nx][ny]
            # 최대값 교체
            if dead_max < dead:
                dead_max = dead

    print(f'#{tc} {dead_max}')