import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 가로세로 길이: N, 단어길이: K
    N, K = map(int, input().split())
    # 낱말판 형성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행에 들어갈 수 있는 횟수
    count = 0
    # 0, 0 부터 시작 행 우선 순회
    for i in range(N):
        # 빈 칸 길이 확인
        length = 0
        for j in range(N):
            # 우방향, 하방향으로만 움직임
            for di, dj in [[0, 1]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj <= N:
                    if arr[i][j] == 1:
                        length += 1
                    else:
                        if length == K:
                            count += 1
                            length = 0
                        else:
                            length = 0
        if length == K:
            count += 1
    # 열에 들어갈 수 있는 단어의 횟수
    count2 = 0
    # 0, 0 부터 시작 열 우선 순회
    for x in range(N):
        # 빈 칸 길이 확인
        length2 = 0
        for y in range(N):
            # 우방향, 하방향으로만 움직임
            for dx, dy in [[1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= N and 0 <= ny <= N:
                    if arr[y][x] == 1:
                        length2 += 1
                    else:
                        if length2 == K:
                            count2 += 1
                            length2 = 0
                        else:
                            length2 = 0
        if length2 == K:
            count2 += 1

    print(f'#{tc} {count + count2}')