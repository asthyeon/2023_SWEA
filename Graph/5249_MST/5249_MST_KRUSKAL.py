import sys
sys.stdin = open('input.txt')

"""
# 그래프로부터 최소 신장 트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램 만들기
1. 최소 신장 트리: 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
                 가중치의 합이 최소가 되도록 만든 경우
2. 무방향 그래프
@ 풀이
(1) MST 중 KRUSKAL 사용
(2) 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르는 알고리즘
"""


# 싸이클 발생 여부를 union find 로 해결
# find_set 함수
def find_set(x):
    # 자기 자신이라면 그대로 반환
    if parents[x] == x:
        return x
    # 경로 단축
    parents[x] = find_set(parents[x])
    return parents[x]


# union 함수
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x > y:
        parents[x] = y
    elif x < y:
        parents[y] = x
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    # 노드번호 V, 간선 개수 E
    V, E = map(int, input().split())

    # 간선 리스트 edge 형성
    edge = []

    # 간선 연결
    for _ in range(E):
        f, t, w = map(int, input().split())

        edge.append([f, t, w])

    # 가중치를 기준으로 정렬
    edge.sort(key=lambda x: x[2])

    parents = [i for i in range(V + 1)]

    # 현재 방문한 정점 수
    cnt = 0
    # 최소 합
    sum_weight = 0
    for f, t, w in edge:
        # 싸이클이 발생하는지 확인(서로 연결되어 있는지 확인)
        if find_set(f) != find_set(t):
            # 연결되지 않았다면 간선 연결 및 가중치 더하기
            cnt += 1
            sum_weight += w
            # 간선이 연결되었으므로 싸이클이 발생하지 않도록 연결
            union(f, t)
            if cnt == V:
                break

    print(f'#{tc} {sum_weight}')
            






