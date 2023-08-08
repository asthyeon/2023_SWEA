import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 가로, 세로의 길이: N, 단어의 길이: K
    N, K = map(int, input().split())
    # 퍼즐의 모양
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 총 단어를 담을 수 있는 수
    count = 0

    # 퍼즐에서 가로 길이 구하기
    for i in range(N):
        # 가로 길이 초기화
        row = 0
        # 가로 길이 만큼 +1을 하기
        for j in range(N):
            # 흰색 부분일 때 +1
            if arr[i][j] == 1:
                row += 1
            # 검은색 부분을 만났을 때
            else:
                # row 가 k와 같다면 카운트 +1, row 값 초기화
                if row == K:
                    count += 1
                    row = 0
                # row 가 k보다 크거나 작으면 row 값 초기화
                else:
                    row = 0
        # 흰 부분이 단어 길이와 같다면 총 수 +1
        if row == K:
            count += 1

    # 퍼즐에서 세로 길이 구하기 (가로 길이 구할 때랑 반복)
    for j in range(N):
        col = 0
        for i in range(N):
            if arr[i][j] == 1:
                col += 1
            else:
                if col == K:
                    count += 1
                    col = 0
                else:
                    col = 0
        if col == K:
            count += 1

    print(f'#{tc} {count}')








