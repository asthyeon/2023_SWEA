T = int(input()) # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    # 최대값 설정
    max_v = arr[0]
    # 최소값 설정
    min_v = arr[0]
    
    # 1부터 N까지 반복
    for i in range(1, N):
        # 만약 최대값이 arr[i]보다 작다면
        if max_v < arr[i]:
            # 최대값 교체
            max_v = arr[i]
        # 만약 최소값이 arr[i]보다 크다면
        elif min_v > arr[i]:
            # 최소값 교체
            min_v = arr[i]
    # 최대값 - 최소값
    ans = max_v - min_v

    print(f'#{tc} {ans}')