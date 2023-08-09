import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 합이 가장 큰 경우 변수 초기화
    max_v = 0
    # 합이 가장 작은 경우 변수 초기화
    min_v = 10000000
    # 두 변수의 차이 초기화
    ans = 0

    # M 개의 합이 가장 큰 경우
    # 0 부터 N-M+1까지 반복
    for i in range(0, N - M + 1):
        # arr 에서 i 부터 M+i 까지 슬라이싱
        arr_sum = arr[i:M + i]
        arr_max = 0
        # M 개의 갯수를 합한 변수 생성
        for arr_one in arr_sum:
            arr_max += arr_one
        # 이전 값과 비교
        if max_v < arr_max:
            max_v = arr_max

    # M 개의 합이 가장 작은 경우
    for i in range(0, N - M + 1):
        arr_sum2 = arr[i:M + i]
        arr_min = 0
        for arr_one2 in arr_sum2:
            arr_min += arr_one2
        if min_v > arr_min:
            min_v = arr_min

    # 두 변수의 차이
    ans = max_v - min_v

    # 출력
    print(f'#{tc} {ans}')