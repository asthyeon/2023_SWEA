import sys
sys.stdin = open('sample_input.txt')

'''
# 출발 노드 에서 도착 노드의 거리 구하기
1. 방향성이 없음
'''


# bfs 함수 생성
def bfs(V, S, G):
    # 방문 리스트 생성
    visited = [0] * (V + 1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(S)
    # 시작점 방문 표시
    visited[S] = 1
    # 큐가 빌 때까지
    while q:
        # 출발
        t = q.pop(0)
        # 인접한 정점 중 인큐되지 않은 정점 w 인큐하기
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐
                q.append(w)
                # 거리 표시하기
                visited[w] = visited[t] + 1

    # 도착 노드가 연결되어 있다면 출발점을 제외해야 하므로 -1
    if visited[G] > 0:
        visited[G] -= 1
    # 연결이 안되어 있으면 0 출력
    return visited[G]


T = int(input())
for tc in range(1, T + 1):
    # 노드 V, 간선 E
    V, E = map(int, input().split())
    # 인접 리스트생성
    adj_l = [[] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    # 출발 S, 도착 G
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(V, S, G)}')
