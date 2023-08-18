import sys
sys.stdin = open('input.txt')

'''
# 미로의 출발점부터 도착점까지 길이 있는지 판단하기
1. 미로는 100 * 100 행렬
2. 미로의 시작점 = (1, 1)
3. 미로의 도착점 = (13, 13)
4. 길 = 0, 벽 = 1, 출발점 = 2, 도착점 = 3
'''


# bfs 함수 생성
def bfs(maze, sx, sy):
    # 방문 리스트 생성
    visited = [[0] * 100 for _ in range(100)]
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sx, sy))
    # 시작점 방문 기록
    visited[sx][sy] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 도착점에 도달했을 때
        if maze[x][y] == 3:
            return 1
        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 벽(1)이 아닐 때 및 방문한 적이 없을 때
            if 0 <= nx < 100 and 0 <= ny < 100 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                # 인큐
                q.append((nx, ny))
                # 방문 기록
                visited[nx][ny] = 1
    # 도착점에 도달하지 못했을 때
    return 0


for tc in range(1, 11):
    T = int(input())
    # 미로 생성
    maze = [list(map(int, input())) for _ in range(100)]
    # 시작점
    sx, sy = 1, 1

    print(f'#{T} {bfs(maze, sx, sy)}')