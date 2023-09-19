import sys
sys.stdin = open('input.txt')

"""
# 만들 수 있는 서로 다른 일곱 자리 수들의 개수 구하기
1. 4 x 4 크기의 격자판
2. 각 격자판에는 0 ~ 9 숫자가 적혀 있음
3. 격자판의 임의의 위치에서 시작해서 상하좌우 인접한 격자로 총 여섯 번 이동 -> 7자리 숫자
4. 한 번 거쳤던 격자칸을 다시 거칠 수 있음
5. 0 으로 시작하는 수를 만들 수 있음
@ 풀이
(1) set 로 중복 제거하기(set.add())
(2) 앞에 0을 붙여야 하기 때문에 str 형태로 넣기
(3) 브루트포스로 해보기
"""


# bfs 함수
def bfs(sx, sy, sevens):
    # 시작점 인큐
    q = [(sx, sy, str(grid[sx][sy]))]
    idx = 0
    # 큐가 빌 때까지
    while q:
        x, y, word = q.pop(0)
        if len(word) == 7:
            sevens.add(word)
            continue
        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, word + str(grid[nx][ny])))


T = int(input())
for tc in range(1, T + 1):
    # 격자판의 정보
    grid = [list(map(int, input().split())) for _ in range(4)]

    # 브루트포스
    sevens = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j, sevens)

    print(f'#{tc} {len(sevens)}')