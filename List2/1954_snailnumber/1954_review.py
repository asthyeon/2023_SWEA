import sys
sys.stdin = open('input.txt')

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    # print(arr)
    
    count = 1 # 달팽이가 이동하면서 값을 증가시키고 기록할 변수
    x, y = 0, 0 # 시작 좌표 설정
    dir = 0 # 이동할 방향 flag
    arr[x][y] = count # 시작 위치에 1을 기록

    # 달팽이 반복 시작
    while count < N ** 2: # N * N 만큼 판이 만들어지니까, 3 * 3 -> 9
        nx = x + dx[dir] # nx = 0 + dx[0] -> 0
        ny = y + dy[dir] # nx = 0 + dx[0] -> 1
        # 다음 조사 위치가 0보다 크거나 같고, N보다 / 작다면 그리고 다음 위치가 0이면
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            count += 1
            arr[nx][ny] = count # 현재 조사하는 곳에 count 할당
            x, y = nx, ny # 내 위치 갱신
        else: # 더 이상 해당 방향으로 이동해 기록할 수 없을 때
            dir += 1
            # 방향은 4종류 뿐이다.
            if dir >= 4:
                dir = 0 # 다시 우측으로 이동

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()


