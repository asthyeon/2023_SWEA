import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 # 최소값의 인덱스
    max_idx = 0 # 최대값의 인덱스
    for i in range(1, N):
        # 최소값의 인덱스가 i 번째보다 작으면 바꿔주기
        if arr[min_idx] > arr[i]:
            min_idx = i
        # 최대값의 인덱스가 i 번째보다 작으면 바꿔주기
        if arr[max_idx] <= arr[i]:
            max_idx = i
    # 구간의 차이
    ans = max_idx - min_idx
    # 양수 조건 만들어주기
    if ans < 0:
        ans = -ans

    print(f'#{tc} {ans}')
