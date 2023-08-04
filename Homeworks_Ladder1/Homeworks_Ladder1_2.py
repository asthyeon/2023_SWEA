import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 테스트케이스 번호
    T = int(input())
    # 사다리 형성
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 델타 탐색을 위한 좌표
    dx = [-1, 0, 0]
    dy = [0, 1, -1]

    # 도착지 좌표 구하기
    x = 0
    y = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                x = i
                y = j

    # 도착지에서부터 시작해 x 가 0 이 되면 탐색 종료
    while x > 0:
        for k in range(3):
            nx = x + dx[k]
            ny = y + dy[k]
            # 위로 이동할 때 값이 1이라면
            if arr[nx][y] == 1:
                # 지나온 값 0 으로 만들기(반복 방지)
                arr[x][y] = 0
                x = nx

            # 오른쪽으로 이동할 때
            if k == 1:
                # 벽 생성
                if y < 99:
                    if arr[x][ny] == 1:
                        arr[x][y] = 0
                        y = ny

            # 왼쪽으로 이동할 때
            if k == 2:
                # 벽 생성
                if y > 0:
                    if arr[x][ny] == 1:
                        arr[x][y] = 0
                        y = ny

    print(f'#{tc} {y}')