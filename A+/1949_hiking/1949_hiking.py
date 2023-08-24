import sys
sys.stdin = open('sample_input.txt')

"""
# 가장 긴 등산로 만들기
1. 등산로는 가장 높은 봉우리에서 시작
2. 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 연결
3. 높이가 같거나 낮거나 대각선 연결 X
4. 딱 한곳만 최대 K 깊이만큼 지형을 깎을 수 있음
"""


# dfs 함수
def dfs(N, sx, sy, arr):
    # 방문 리스트 만들기
    visited = [[0] * N for _ in range(N)]
    # 스택 생성
    stack = []
    # 시작점 푸쉬
    stack.append((sx, sy))
    # 시작점 방문 표시
    visited[sx][sy] = 1
    while True:
        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = sx + dx, sy + dy
            # 벽 형성 및 거리가 더 작을 때 교체하기
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] < visited[sx][sy]:
                if arr[nx][ny] < arr[sx][sy]:
                    stack.append((nx, ny))
                    visited[nx][ny] = visited[sx][sy] + 1
                    break
        else:
            if stack:
                sx, sy = stack.pop()
            else:
                break
    # 최대 값 출력
    road_max = 0
    for j in range(N):
        road = max(visited[j])
        if road_max < road:
            road_max = road
    return road_max


T = int(input())
for tc in range(1, T + 1):
    # 지도 크기 N, 공사 가능 깊이 K
    N, K = map(int, input().split())

    # 지도 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    top = 0
    location = []
    for i in range(N):
        for j in range(N):
            # 현재 정상보다 높다면 기존 봉우리 비우고 새로 추가
            if top < arr[i][j]:
               location.clear()
               top = arr[i][j]
               location.append((i, j))
            # 현재 정상과 같다면 봉우리 위치 추가
            elif top == arr[i][j]:
               location.append((i, j))

    # 최대 길이
    length_max = 0
    # 봉우리 하나씩 K만큼 파고 진행
    for k in range(N):
        for l in range(N):
            for m in range(1, K + 1):
                arr[k][l] -= m
                # 제일 높은 봉우리에서 진행
                for sx, sy in location:
                    # 파인 봉우리라면 진행 X
                    if sx != k or sy != l:
                        length = dfs(N, sx, sy, arr)
                        # 가장 긴 등산로 길이랑 비교하여 교체
                        if length_max < length:
                            length_max = length
                arr[k][l] += m

    print(f'#{tc} {length_max}')


