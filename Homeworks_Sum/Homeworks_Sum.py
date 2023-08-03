import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 테스트 케이스 번호
    N = int(input())
    # 100X100 배열 생성
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 가로의 합 변수
    sum_i = 0
    # 세로의 합 변수
    sum_j = 0
    # 좌상단 시작 대각선의 합 변수
    sum_ij = 0
    # 우상단 시작 대각선의 합 변수
    sum_ji = 0
    # 가장 큰 합
    sum_max = 0

    # 각 가로의 합 구하기
    for j in range(100):
        sum_i2 = 0
        for i in range(100):
            sum_i2 += arr[j][i]
        # 더 큰 가로의 합으로 교체
        if sum_i < sum_i2:
            sum_i = sum_i2

    # 가장 큰 합을 가장 큰 가로의 합으로 교체
    sum_max = sum_i

    # 각 세로의 합 구하기
    for i in range(100):
        sum_j2 = 0
        for j in range(100):
            sum_j2 += arr[j][i]
        # 더 큰 세로의 합으로 교체
        if sum_j < sum_j2:
            sum_j = sum_j2
            # 가로의 합과 비교하여 큰 값으로 교체
            if sum_max < sum_j:
                sum_max = sum_j

    # 좌상단 시작 대각선의 합 구하기
    for i in range(100):
        sum_ij += arr[i][i]
    # 세로의 합과 비교하여 큰 값으로 교체
    if sum_max < sum_ij:
        sum_max = sum_ij

    # 우상단 시작 대각선의 합 구하기
    for i in range(99, -1, -1):
        sum_ji += arr[i][99 - i]
    # 좌상단 시작 대각선의 합과 비교하여 큰 값으로 교체
    if sum_max < sum_ji:
        sum_max = sum_ji
    
    # 출력
    print(f'#{tc} {sum_max}')