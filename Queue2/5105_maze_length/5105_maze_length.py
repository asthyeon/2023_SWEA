import sys
sys.stdin = open('sample_input.txt')

'''
# 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다르는지
1. 경로가 있는 경우 지나야 하는 최소한의 칸수 출력
2. 경로가 없는 경우 0 출력
3. 출발지는 2, 도착지는 3
'''


# 시작점 좌표 찾는 함수 생성
def start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


# # bfs 함수 생성
def bfs(N, x, y):
    # 방문 리스트 생성
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((x, y))
    # 시작점 방문
    visited[x][y] = 1
    # 큐가 빌 때까지
    while q:
        # 이동
        x, y = q.pop(0)
        # 도착점에 도착했을 때
        if maze[x][y] == 3:
            # 돌아온 칸수 반환(시작점과 도착점 카운트 제외)
            return visited[x][y] - 2
        # 델타탐색으로 통로 찾기
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 벽(1)이 아니고 방문한 적이 없으면
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                # 인큐
                q.append((nx, ny))
                # 방문 기록(거리 표시)
                visited[nx][ny] = visited[x][y] + 1
    # 도착점에 도달하지 못했을 때 0 반환
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 미로 형성
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작점 좌표 생성
    x, y = start(N, maze)
    print(f'#{tc} {bfs(N, x, y)}')