import sys
sys.stdin = open('input.txt')

"""
# 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람 구하기
1. 최대 연락 인원: 100명, 부여될 수 있는 번호 1 ~ 100
2. 비어 있는 번호가 있을 수 있음
3. 한 명이 다수에게 연락 가능한 경우 동시에 전달 및 연락이 퍼지는 속도는 항상 일정
4. 연락을 받은 사람에게 다시 연락 하는 일 X
5. 연락을 받을 수 없는 사람도 존재 가능
6. 단방향 그래프
@ 풀이
(1) bfs 사용
"""


# bfs 함수
def bfs(S, adj):
    # 방문 리스트
    visited = [0] * 101
    # 시작점 인큐 및 방문 기록
    q = [S]
    visited[S] = 1
    # 큐가 빌 때까지
    while q:
        x = q.pop(0)
        # 인접 사람 찾기
        for j in range(1, 101):
            # 인접하고 방문한 적이 없다면
            if adj[x][j] == 1 and visited[j] == 0:
                q.append(j)
                visited[j] = visited[x] + 1

    # 가장 큰 번호 찾기
    cnt = max(visited)
    for k in range(100, -1, -1):
        if visited[k] == cnt:
            return k


for tc in range(1, 11):
    # 데이터의 길이 N, 시작점 S
    N, S = map(int, input().split())
    # 입력받은 데이터
    data = list(map(int, input().split()))
    # 인접행렬
    adj = [[0] * 101 for _ in range(101)]

    # 인접행렬 연결
    for i in range(N // 2):
        x, y = data[i * 2], data[(i * 2) + 1]

        adj[x][y] = 1

    result = bfs(S, adj)

    print(f'#{tc} {result}')