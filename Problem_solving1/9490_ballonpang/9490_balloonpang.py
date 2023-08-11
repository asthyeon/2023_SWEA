import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T + 1):
    # N 줄, M 개의 풍선
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 제일 많은 꽃가루 수
    max_flowers = 0

    # 0,0 부터 풍선 탐색
    for i in range(N):
        for j in range(M):
            # 델타 탐색
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj
                # 꽃가루 합
                flowers = 0
                # 벽 세우기
                if 0 <= ni < N and 0 <= nj < M:
                    # 찾은 풍선의 기준 값 설정
                    finding = arr[i][j]
                    # 기준 값 꽃가루 더하기
                    flowers += finding

                    # 풍선 값만큼 상하좌우 풍선 터뜨리기
                    while True:
                        # 우방향 터뜨리기
                        for k in range(1, finding + 1):
                            # 벽 설정
                            if j + k >= M:
                                break
                            # 벽이 아니라면 터뜨리고 꽃가루 더하기
                            else:
                                flowers += arr[i][j + k]
                        # 하방향 터뜨리기
                        for k in range(1, finding + 1):
                            # 벽 설정
                            if i + k >= N:
                                break
                            # 벽이 아니라면 터뜨리고 꽃가루 더하기
                            else:
                                flowers += arr[i + k][j]
                        # 좌방향 터뜨리기
                        for k in range(1, finding + 1):
                            # 벽 설정
                            if j - k < 0:
                                break
                            # 벽이 아니라면 터뜨리고 꽃가루 더하기
                            else:
                                flowers += arr[i][j - k]
                        # 상방향 터뜨리기
                        for k in range(1, finding + 1):
                            # 벽 설정
                            if i - k < 0:
                                break
                            # 벽이 아니라면 터뜨리고 꽃가루 더하기
                            else:
                                flowers += arr[i - k][j]
                        # 반복문 종료
                        break
                if max_flowers < flowers:
                    max_flowers = flowers

    print(f'#{tc} {max_flowers}')