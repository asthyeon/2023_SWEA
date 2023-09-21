import sys
sys.stdin = open('input.txt')

"""
# 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램 만들기
1. 지역의 높이 차이에 따라 연료 소비량이 달라짐
2. 출발지는 맨 왼쪽 위, 도착지는 가장 오른쪽 아래
3. 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동 가능
4. 인접 지역으로 이동시에는 연료 1 소비, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료 소비
@ 풀이
(1) 다익스트라 사용
"""
import heapq


# 다익스트라 함수
def dijkstra(sx, sy, distance):
    # 우선순위 큐
    pq = []
    # 출발점 인큐
    heapq.heappush(pq, (0, sx, sy))
    distance[sx][sy] = 0

    # 큐가 빌 때까지
    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문했다면 넘기기
        if distance[x][y] < dist:
            continue

        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < N:
                # 비용 계산
                # 현재위치보다 높다면
                if arr[x][y] < arr[nx][ny]:
                    # 높이 차이만큼 비용 추가
                    cost = 1 + (arr[nx][ny] - arr[x][y])
                # 현재위치보다 낮거나 같다면
                else:
                    cost = 1

                # 누적 비용 구하기
                acc_cost = dist + cost

                # 누적 비용이 기존보다 크다면 넘기기
                if distance[nx][ny] <= acc_cost:
                    continue

                # 그렇지 않다면 갱신 후 누적 비용 및 위치 인큐
                distance[nx][ny] = acc_cost
                heapq.heappush(pq, (acc_cost, nx, ny))


T = int(input())
for tc in range(1, T + 1):
    # 가로 x 세로 칸 수 N
    N = int(input())

    # 맵 형성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 누적거리 형성
    distance = [[1000 * 200] * N for _ in range(N)]

    dijkstra(0, 0, distance)

    print(f'#{tc} {distance[N - 1][N - 1]}')