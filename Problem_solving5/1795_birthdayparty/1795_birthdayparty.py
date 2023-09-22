import sys
sys.stdin = open('input.txt')

"""
# 각 사람들이 자신의 집에서 인수의 집으로 오고 가는데 드는 시간 중 이 가장 긴 시간 구하기
1. 인수가 사는 마을에는 N 개의 집, 각 집 에는 1명 존재
2. 단방향 간선 이므로 오고 갈 때 시간이 다름
@ 풀이
(1) 다익스트라 사용
(2) 각 노드에서 인수의 집까지 가는 최단시간을 구하고 가장 오래 걸리는 노드의 시간을 출력 
"""
import heapq


# 다익스트라 함수
def dijkstra(start):
    # 우선순위 큐 생성
    pq = []
    # 시작점 인큐
    heapq.heappush(pq, (0, start))
    # 각 누적 거리를 구할 리스트
    distance = [100 * 10000] * (N + 1)
    # 시작점 방문 기록
    distance[start] = 0

    # 큐가 빌 때까지
    while pq:
        dist, now = heapq.heappop(pq)

        # 방문했거나 이전 기록이 더 거리가 짧다면 넘기기
        if distance[now] < dist:
            continue

        # 갈 수 있는 곳 확인
        for new in graph[now]:
            n_dist = new[0] + dist
            n_loc = new[1]

            # 이전 기록이 더 거리가 짧거나 같다면 넘기기
            if distance[n_loc] <= n_dist:
                continue

            # 더 길다면 교체 및 인큐
            distance[n_loc] = n_dist
            heapq.heappush(pq, (n_dist, n_loc))

    if start == X:
        return distance
    else:
        return distance[X]


T = int(input())
for tc in range(1, T + 1):
    # 집의 수 N, # 간선 수 M, 인수의 집 X
    N, M, X = map(int, input().split())
    # 인접 리스트
    graph = [[] for _ in range(N + 1)]

    # 각 집 연결
    for _ in range(M):
        # x 번 집에서 y 번 집으로 가는데 걸리는 시간 c
        x, y, c = map(int, input().split())

        # 걸리는 시간을 먼저 append
        graph[x].append((c, y))

    # 인수의 집에서 각 집으로 돌아올 때 걸리는 시간 구하기
    back = dijkstra(X)

    # 각 집에서 인수의 집으로 갈 때 걸리는 시간 구하기
    max_time = 0
    for i in range(1, N + 1):
        # 인수의 집에서 출발할 경우 넘기기
        if i == X:
            continue
        time = dijkstra(i)

        # 가장 오래 걸리는 시간 비교(출발 시간 및 돌아오는 시간 더하기)
        if max_time < time + back[i]:
            max_time = time + back[i]

    print(f'#{tc} {max_time}')