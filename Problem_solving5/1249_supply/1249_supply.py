import sys
sys.stdin = open('input.txt')

"""
# 출발지에서 도착지까지 가는 경로 중 복구 시간이 가장 짧은 경로에 대한 복구 시간 구하기
1. 도로가 파여진 깊이에 비례해서 복구 시간 증가
2. 깊이 1 당 복구 시간 1 소요
@ 풀이
(1) 다익스트라 사용
(2) 델타탐색으로 인접 지역 구하기
"""
import heapq


# 다익스트라 함수
def dijkstra(sx, sy, arr):
    # 우선순위큐 생성
    pq = []
    # 복구 깊이 및 시작점 인큐
    heapq.heappush(pq, (0, sx, sy))
    # 각 위치의 누적 복구시간이 반영된 arr
    time_arr = [[100 * 100] * N for _ in range(N)]
    # 시작점 방문 기록
    time_arr[sx][sy] = 0

    # 큐가 빌 때까지
    while heapq:
        # 가장 깊이가 낮은 인접 지역 pop
        depth, x, y = heapq.heappop(pq)

        # 도착점에 도달했다면 반복 종료
        if x == N - 1 and y == N - 1:
            break

        # 현재 위치를 이미 방문 했고 그 때보다 더 시간이 걸렸다면 넘기기
        if time_arr[x][y] < depth:
            continue

        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy

            # 벽 형성 및 방문하지 않았다면 방문
            if 0 <= nx < N and 0 <= ny < N:
                # 이전에 도착한 다음 위치의 누적 시간이 현재의 누적시간보다 크거나 같다면 넘기기
                if time_arr[nx][ny] <= depth + arr[nx][ny]:
                    continue

                # 더 작다면 다음 지역에 더하기
                n_depth = depth + arr[nx][ny]
                time_arr[nx][ny] = n_depth
                heapq.heappush(pq, (n_depth, nx, ny))
    
    # 도착점의 누적 시간 반환
    return time_arr[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    # 지도의 크기 N x N
    N = int(input())

    # 지도 입력
    arr = [list(map(int, input())) for _ in range(N)]

    # 함수 사용
    result = dijkstra(0, 0, arr)

    print(f'#{tc} {result}')
