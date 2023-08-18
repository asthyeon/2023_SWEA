import sys
sys.stdin = open('input.txt')

'''
# 주어진 미로의 출발점으로부터 도착점까지 갈 수 있는 길이 있는지 판단하기
1. 벽(1), 통로(0), 출발(2), 도착(3)
2. 미로는 16 * 16 행렬
'''


# 시작점 찾기
def start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j


# bfs 함수 생성
def bfs(maze, x, y):
    # 방문 리스트 생성
    visited = [[0] * 16 for _ in range(16)]
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((x, y))
    # 시작점 방문 표시(거리)
    visited[x][y] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 도착했을 때
        if maze[x][y] == 3:
            # 도달 가능 여부 1 출력
            return 1
        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 벽(1)이 아닐 때 및 방문하지 않았을 때
            if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                # 인큐
                q.append((nx, ny))
                # 방문 기록(거리)
                visited[nx][ny] = visited[x][y] + 1
    # 도착점에 도달하지 못했을 때
    return 0


for tc in range(1, 11):
    T = int(input())
    # 미로 형성
    maze = [list(map(int, input())) for _ in range(16)]
    # 시작점
    x, y = start(maze)

    print(f'#{tc} {bfs(maze, x, y)}')