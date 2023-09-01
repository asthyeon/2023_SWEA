import sys
sys.stdin = open('input.txt')

"""
# 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지
1. 이동하려는 방에 숫자가 현재 방보다 1 커야함
2. 상하좌우 이동가능
3. 방의 개수가 최대인 방이 여러개라면 가장 작은 수 출력
4. 모두 서로 다른 수
"""


# dfs 함수
def dfs(sx, sy, arr, visited):
    # 이동 횟수
    move = 1
    # 시작점 방문 기록
    visited[sx][sy] = 1
    # 스택 형성
    stack = [(sx, sy)]
    # 최솟값을 찾기 위한 리스트 형성
    min_list = [arr[sx][sy]]
    # 변수 교체
    x, y = sx, sy
    while True:
        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 방문하지 않았을 때
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # +1 일 때
                if arr[nx][ny] == arr[x][y] + 1:
                    # push
                    stack.append((nx, ny))
                    # 방문 기록
                    visited[nx][ny] = 1
                    # 이동 횟수 + 1
                    move += 1
                    # 번호 넣기
                    min_list.append(arr[nx][ny])
                    break
                # -1 일 때
                elif arr[nx][ny] == arr[x][y] - 1:
                    # push
                    stack.append((nx, ny))
                    # 방문 기록
                    visited[nx][ny] = 1
                    # 이동 횟수 + 1
                    move += 1
                    # 번호 넣기
                    min_list.append(arr[nx][ny])
                    break
        # 이동할 수 없을 때
        else:
            # 스택이 비어있지 않다면
            if stack:
                x, y = stack.pop()
            # 스택이 비어있다면
            else:
                break
    # 시작점 및 이동 횟수 반환
    return min(min_list), move




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 정사각형 방
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문 리스트
    visited = [[0] * N for _ in range(N)]

    # 비교할 값
    start, move = 1000, 0

    # 시작점 찾기
    for m in range(N):
        for n in range(N):
            # 방문하지 않았을 때 함수 적용
            if visited[m][n] == 0:
                start2, move2 = dfs(m, n, arr, visited)
                # 값 교체
                if move < move2:
                    move = move2
                    start = start2
                elif move == move2:
                    if start > start2:
                        start = start2

    print(f'#{tc} {start} {move}')
