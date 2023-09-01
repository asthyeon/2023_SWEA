import sys
sys.stdin = open('input.txt')
from collections import deque

"""
# 땅으로 표현된 모든 칸에서 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수의 합 구하기
1. 물: W, 땅: L
2. 어떤 칸에 사람이 있으면 상하좌우로 다른 칸 이동 가능
@ 풀이
(1) 입력을 리스트로 받지 말고 큐를 튜플로 만들어서 시간 줄이기
"""


# bfs 함수
def bfs(q, arr, visited):
    global move
    # 큐가 빌 때까지
    while q:
        x, y = q.popleft()
        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, - 1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 방문하지 않았을 때
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 땅일 때
                if arr[nx][ny] == 'L':
                    # 인큐
                    q.append((nx, ny))
                    # 방문 기록 + 1
                    visited[nx][ny] = visited[x][y] + 1
                    # 이동횟수 더하기
                    move += visited[nx][ny]


T = int(input())
for tc in range(1, T + 1):
    # 세로 N, 가로 M
    N, M = map(int, input().split())

    # 물놀이판 만들기
    arr = [input() for _ in range(N)]

    # 방문 리스트
    visited = [[0] * M for _ in range(N)]

    # 이동 횟수의 합
    move = 0
    # 큐 형성
    q = deque(())

    # 물의 위치를 큐에 담기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i, j))

    # 함수 실행
    bfs(q, arr, visited)

    print(f'#{tc} {move}')