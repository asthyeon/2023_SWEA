import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 배열 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 모든 차이의 절댓값을 더할 변수
    num = 0

    # arr[i, j] = [0, 0] 부터 순회
    for i in range(N):
        for j in range(N):
            # 델타 탐색시작
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj
                # 만약 가장자리 벽 안에 있다면
                if 0 <= ni < N and 0 <= nj < N:
                    # 해당 값과 이웃한 요소들의 차이의 절대값을 num 에 더하기
                    if (arr[i][j] - arr[ni][nj]) < 0:
                        num += -(arr[i][j] - arr[ni][nj])
                    else:
                        num += arr[i][j] - arr[ni][nj]

    # 출력
    print(f'#{tc} {num}')





