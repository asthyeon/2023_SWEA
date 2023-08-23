import sys
sys.stdin = open('sample_input(1).txt')

"""
# 오셀로 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수 출력
1. 보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임 종료
2. 정가운데에 백, 흑, 백, 흑 으로 배치하고 시작
3. 보드는 4x4, 6x6, 8x8을 사용
4. 1 = 흑돌, 2 = 백돌
5. 대각선도 포함
"""

# delta 좌표(8방향)
delta = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]


# 오셀로 함수
def othello(N, x, y, board):
    # 델타 탐색 8방향
    for dx, dy in delta:
        nx, ny = x, y
        # 벽 형성
        if 1 <= nx < (N + 1) and 1 <= ny < (N + 1):
            board[nx][ny] = color
            # 스택 형성
            stack = []
            top = -1
            # 해당하는 라인의 색깔 확인
            while True:
                nx, ny = nx + dx, ny + dy
                # 벽 형성
                if 1 <= nx < (N + 1) and 1 <= ny < (N + 1):
                    # 해당 숫자가 color라면 반복문 종료
                    if board[nx][ny] == color:
                        break
                    # 해당 숫자가 0 이라면 스택을 비우고 반복문 종료
                    elif board[nx][ny] == 0:
                        stack.clear()
                        top = -1
                        break
                    # 다른 색상의 돌이라면 푸쉬
                    else:
                        stack.append((nx, ny))
                        top += 1
                # 벽을 벗어나면 스택을 비우고 반복문 종료
                else:
                    stack.clear()
                    top = -1
                    break
            # 스택에 들어가 있는 다른 색상들을 같은 컬러로 바꿔주기
            for i, j in stack:
                board[i][j] = color


T = int(input())
for tc in range(1, T + 1):
    # 보드 한 변의 길이 N, 플레이어가 돌을 놓는 횟수 M
    N, M = map(int, input().split())

    # 보드판 형성
    board = [[0] * (N + 1) for _ in range(N + 1)]
    
    # 보드 크기에 따라 정가운데 4 칸에 돌 배치
    board[N // 2][N // 2] = 2
    board[N // 2][(N // 2) + 1] = 1
    board[(N // 2) + 1][N // 2] = 1
    board[(N // 2) + 1][(N // 2) + 1] = 2

    # 돌 놓기
    for _ in range(M):
        x, y, color = map(int, input().split())
        othello(N, x, y, board)

    # 흑돌, 백돌 수 세기
    black = 0
    white = 0
    for line in board:
        black += line.count(1)
        white += line.count(2)

    print(f'#{tc} {black} {white}')

