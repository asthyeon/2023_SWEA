import sys
sys.stdin = open('sample_input.txt')

# T값 받기
T = int(input())
# T+1 의 범위까지 tc 반복
for tc in range(1, T + 1):
    # N개의 수 받기
    N = int(input())
    # N개의 수를 정수형으로 만들고 리스트화하기
    arr = list(map(int, input().split()))
    # 최대 값과 최소 값의 차이를 담을 변수 생성
    ans = 0
    # 최대 값 변수 생성
    max_v = arr[0]
    # 최소 값 변수 생성
    min_v = arr[0]
    
    # N 의 범위까지 i 반복
    for i in range(1, N):
        # 만일 max_v 가 arr[i]보다 작다면
        if max_v < arr[i]:
            # 최대 값 교체
            max_v = arr[i]
        # 만일 min_v 가 arr[i]보다 크다면
        elif min_v > arr[i]:
            # 최소 값 교체
            min_v = arr[i]
    # 최대 값 - 최소 값
    ans = max_v - min_v
    
    # 출력
    print(f'#{tc} {ans}')