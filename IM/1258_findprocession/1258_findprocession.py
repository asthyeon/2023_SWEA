import sys
sys.stdin = open("input.txt")

"""
# 추출된 부분 행렬들의 개수 및 행렬들의 행과 열의 크기 출력하기
1. 화학물질이 담긴 용기들이 사각형 모양
2. 용기들의 차원은 다름
3. 빈 용기는 0
* 크기가 작은 순서대로 출력(행 x 열)
* 크기가 같다면 행이 작은 순으로 출력
@ 풀이
1. bfs로 0이 아닌 가로 길이, 세로 길이 구하기
2. 리스트에 넣고 곱한 값 순서대로 출력(같으면 작은 행 순서대로)
"""


# bfs 함수
def bfs(n, sx, sy, arr):
    # 방문 리스트 생성
    visited = [[0] * n for _ in range(n)]
    # 시작점 인큐
    q = [(sx, sy)]
    # 시작점 방문 기록
    visited[sx][sy] = 1
    arr[sx][sy] = 10
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 방문하지 않았을 때
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if 0 < arr[nx][ny] < 10:
                    # 인큐
                    q.append((nx, ny))
                    # 방문 기록
                    visited[nx][ny] = visited[x][y] + 1
                    # 배열도 바꿔주기
                    arr[nx][ny] = 10
    # 행과 열 찾기
    fx = fy = 0
    wx = sx
    wy = sy
    # 열 찾기
    while True:
        if visited[sx][wy] != 0:
            wy += 1
            fy += 1
        else:
            break
    # 행 찾기
    while True:
        if visited[wx][sy] != 0:
            wx += 1
            fx += 1
        else:
            break

    return fx * fy, fx, fy


T = int(input())
for tc in range(1, T + 1):
    # 배열 크기
    n = int(input())

    # 배열 받기
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 부분행렬 수
    cnt = 0

    # 부분행렬 리스트
    processions = []

    # 부분행렬 구하기
    for sx in range(n):
        for sy in range(n):
            if 0 < arr[sx][sy] < 10:
                cnt += 1
                processions.append(bfs(n, sx, sy, arr))

    # 행렬 크기, 행 순으로 정렬
    processions.sort()

    print(f'#{tc} {cnt}', end='')
    for m in range(len(processions)):
        print(f' {processions[m][1]} {processions[m][2]}', end="")
    print()