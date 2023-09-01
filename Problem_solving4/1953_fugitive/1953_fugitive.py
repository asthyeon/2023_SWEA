import sys
sys.stdin = open('input.txt')

"""
# 탈주범이 위치할 수 있는 장소의 개수 출력
1. 탈주범은 시간당 1의 거리 이동 가능
2. 맨홀 뚜껑은 항상 터널이 있는 곳에 위치
3. 터널 구조물 타입
 - 1: 상, 하, 좌, 우
 - 2: 상, 하
 - 3:        좌, 우
 - 4: 상,        우
 - 5:     하,    우
 - 6:     하, 좌
 - 7: 상,     좌
"""

# 터널 구조물 타입
tunnel = dict()
tunnel[1] = [-1, 0], [1, 0], [0, -1], [0, 1]
tunnel[2] = [-1, 0], [1, 0]
tunnel[3] = [0, -1], [0, 1]
tunnel[4] = [-1, 0], [0, 1]
tunnel[5] = [1, 0], [0, 1]
tunnel[6] = [1, 0], [0, -1]
tunnel[7] = [-1, 0], [0, -1]

# 방문가능한 타입
route = dict()
# 상
route[-1, 0] = 1, 2, 5, 6
# 하
route[1, 0] = 1, 2, 4, 7
# 좌
route[0, -1] = 1, 3, 4, 5
# 우
route[0, 1] = 1, 3, 6, 7


# bfs 함수
def bfs(sx, sy, arr, visited):
    # 소요시간이 1시간일 경우
    if L == 1:
        return 1
    # 시작점 인큐
    q = [(sx, sy)]
    # 시작점 방문 기록
    visited[sx][sy] = 1
    # 이동 횟수
    move = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 값이 K보다 크면 다음 반복
        if visited[x][y] == L:
            continue
        # 터널 구조에 맞게 이동
        for dx, dy in tunnel[arr[x][y]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 방문하지 않았고, 터널일 때
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] != 0:
                # 해당하는 루트를 가진다면 이동
                if arr[nx][ny] in route[dx, dy]:
                    # 인큐
                    q.append((nx, ny))
                    # 방문 기록
                    visited[nx][ny] = visited[x][y] + 1

    # 위치할 수 있는 장소 수 더하기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    # 세로: N, 가로: M, 맨홀 뚜껑 위치: R, C, 탈출 후 소요시간: L
    N, M, R, C, L = map(int, input().split())

    # 하수구 지도
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문 리스트
    visited =[[0] * M for _ in range(N)]

    # 함수 실행
    print(f'#{tc} {bfs(R, C, arr, visited)}')
