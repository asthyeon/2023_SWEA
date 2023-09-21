import sys
sys.stdin = open('input.txt')

"""
# 그래프로부터 최소 신장 트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램 만들기
1. 최소 신장 트리: 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
                 가중치의 합이 최소가 되도록 만든 경우
2. 무방향 그래프
@ 풀이
(1) MST 중 Prim 알고리즘 사용
"""
import heapq


# prim 함수
def prim(start):
    # 힙큐 생성
    heap = []
    # MST 생성(방문리스트)
    MST = [0] * (V + 1)
    # 시작점 시작가중치 및 위치 인큐
    heapq.heappush(heap, (0, start))
    # 누적 최소합
    sum_weight = 0
    # 힙큐가 빌 때 까지
    while heap:
        # 가중치가 가장 적은 가중치와 위치를 팝
        weight, v = heapq.heappop(heap)

        # 방문한 곳이라면 넘기기
        if MST[v] == 1:
            continue

        # 방문 기록
        MST[v] = 1

        # 누적 최소합에 가중치 더하기
        sum_weight += weight

        # 방문가능한 노드 탐색
        for i in range(V + 1):
            # 방문할 수 없거나 이미 방문했다면 넘기기
            if graph[v][i] == 0 or MST[i] == 1:
                continue

            heapq.heappush(heap, (graph[v][i], i))

    return sum_weight


T = int(input())
for tc in range(1, T + 1):
    # 노드번호 V, 간선의 개수 E
    V, E = map(int, input().split())
    # 그래프 만들기
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    # 간선의 양 끝 노드 n1, n2 및 가중치 w
    for _ in range(E):
        n1, n2, w = map(int, input().split())

        # 무방향 그래프
        graph[n1][n2] = w
        graph[n2][n1] = w

    print(graph)
    result = prim(0)

    print(f'#{tc} {result}')



