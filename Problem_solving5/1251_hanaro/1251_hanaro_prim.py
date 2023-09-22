import sys
sys.stdin = open('input.txt')

"""
# 총 환경 부담금을 최소로 지불하여 모든 섬 연결하기
1. 인도네시아 내 모든 섬을 해저터널로 연결하는 것을 목표로 함
2. 환경 부담금 = 환경 부담 세율(E) * (각 해저터널의 길이(L) ** 2)
 - 부담금 = E * L^2 
3. 양방향 그래프
@ 풀이
(1) MST 를 구성해야함
(2) prim 알고리즘 사용하기
(3) 세금을 거리를 전부 다 더한 후 구해야함
"""
import heapq


# 거리 구하는 함수
def length(x1, y1, x2, y2):
    length = ((y2 - y1) ** 2) + ((x2 - x1) ** 2)
    return length


# prim 함수
def prim(start):
    global distance
    # 힙큐 생성
    heap = []
    # MST 생성
    MST = [0] * N
    # 큐에 시작점 인큐
    heapq.heappush(heap, (0, start))
    # 누적 거리
    sum_dist = 0

    # 큐가 빌 때까지
    while heap:
        # 가장 적은 거리를 가진 위치를 꺼냄
        dist, now = heapq.heappop(heap)

        # 방문한 곳이라면 넘기기
        if MST[now] == 1:
            continue

        # 방문 기록
        MST[now] = 1

        # 누적 거리 추가
        sum_dist += dist

        # 방문 가능한 섬들을 찾기기
        for island in islands[now]:
            n_dist = island[0]
            next = island[1]
            
            # 이미 방문한 곳이면 넘기기
            if MST[next] == 1:
                continue
            
            # 방문하지 않았다면 인큐
            heapq.heappush(heap, (n_dist, next))

    return sum_dist


T = int(input())
for tc in range(1, T + 1):
    # 섬의 개수 N
    N = int(input())
    # 각 섬들의 x 좌표
    x_list = list(map(int, input().split()))
    # 각 섬들의 y 좌표
    y_list = list(map(int, input().split()))
    # 환경 부담 세율
    E = float(input())
    # 각 섬들의 거리
    islands = [[] for _ in range(N)]

    # 각 섬들의 거리 구하기
    for i in range(N):
        x1 = x_list[i]
        y1 = y_list[i]
        # 양방향으로 연결
        for j in range(N):
            # 같은 섬이 될 경우 넘기기
            if i == j:
                continue
            x2 = x_list[j]
            y2 = y_list[j]
            
            # 거리 구하기
            leng = length(x1, y1, x2, y2)
        
            islands[i].append((leng, j))

    print(f'#{tc} {round(prim(0) * E)}')
