import sys
sys.stdin = open('input.txt')

"""
# 0 번지점에서 N 번지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하기
1. A 도시에는 E 개의 일방통행 도로 구간이 존재
2. 각 구간이 만나는 연결지점에는 0 부터 N 번까지의 번호가 붙어 있음
3. 모든 연결 지점을 거쳐가야 하는 것은 아님 => 다익스트라
@ 풀이
(1) 다익스트라 사용
(2) 직접 힙 구현하기
"""


# 최소힙 삽입 함수
def min_heap(pq, idx):
    if idx == 1:
        return
    # 부모노드보다 자식노드가 더 작다면 교체 후 부모노드에서 다시 탐색
    if pq[idx // 2][0] > pq[idx][0]:
        pq[idx // 2], pq[idx] = pq[idx], pq[idx // 2]
        min_heap(pq, idx // 2)
    # 자식노드가 더 크다면 함수 종료
    else:
        return


# 힙 삭제 함수
def delete_heap(pq):
    # 큐에 원소가 2개 이상 있을 때
    if len(pq) > 2:
        # 루트 노드 저장
        result = pq[1]
        # 마지막 노드를 루트로 가져오기
        pq[1] = pq.pop()
        # 부모 노드와 자식 노드 인덱스 구성
        p = 1
        c = p * 2
        # 자식이 한명이라도 있다면
        while c < len(pq):
            # 오른쪽 자식이 있고, 오른쪽 자식이 더 크다면 자식 교체
            if c + 1 < len(pq) and pq[c][0] < pq[c + 1][0]:
                c = c + 1

            # 부모 노드보다 자식 노드가 더 작다면 교체 후 자식노드에서 다시 탐색
            if pq[p][0] > pq[c][0]:
                pq[p], pq[c] = pq[c], pq[p]
                p = c
                c = p * 2
            # 부모 노드가 더 작다면 반복 종료
            else:
                break
        return result
    # 큐에 원소가 하나만 있을 때
    else:
        result = pq.pop()
        return result


# 다익스트라 함수
def dijkstra(start, distance, graph):
    # 우선순위큐 생성, 인덱스 조정을 위해 0 넣기
    pq = [0]
    # 시작점의 가중치 및 위치 인큐
    pq.append([0, start])
    idx = 1
    min_heap(pq, idx)
    # 시작점 거리 기록
    distance[start] = 0

    # 큐가 빌 때까지
    while len(pq) > 1:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = delete_heap(pq)
        idx -= 1

        # 이미 방문한 지점이고 누적 거리가 더 짧게 방문한 적이 있다면 넘기기
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for n_dist, next in graph[now]:
            # 누적 거리
            acc_dist = dist + n_dist

            # 누적 거리가 기존 거리보다 크다면 넘기기
            if distance[next] <= acc_dist:
                continue

            # 크지 않다면 거리 갱신 후 인큐
            distance[next] = acc_dist
            pq.append([acc_dist, next])
            idx += 1
            min_heap(pq, idx)


T = int(input())
for tc in range(1, T + 1):
    # 마지막 연결지점 N, 도로의 개수 E
    N, E = map(int, input().split())

    # 그래프 연결
    graph = [[] for _ in range(N + 1)]
    # 누적 거리 리스트
    distance = [1000 * 10] * (N + 1)
    for _ in range(E):
        # 시작 s, 끝 e, 거리 w
        s, e, w = map(int, input().split())
        graph[s].append([w, e])

    dijkstra(0, distance, graph)

    print(f'#{tc} {distance[-1]}')
