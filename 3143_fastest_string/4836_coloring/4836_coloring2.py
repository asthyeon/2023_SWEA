import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 색칠되는 영역의 수: N
    N = int(input())

    # 색칠판 형성
    arr = [[0] * 10 for _ in range(10)]

    # 색칠 영역 입력 받기
    for i in range(N):
        color = list(map(int, input().split()))
        # 색칠
        for x in range(color[0], color[2] + 1):
            for y in range(color[1], color[3] + 1):
                arr[x][y] += color[4]

    # 보라색 칸 수
    counting = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                counting += 1

    print(f'#{tc} {counting}')