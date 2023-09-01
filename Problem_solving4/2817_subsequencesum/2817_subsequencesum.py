import sys
sys.stdin = open('input.txt')

"""
# N 개의 자연수 중 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수
"""


# 부분집합 함수
def subset(i, s_sum, arr):
    global cnt
    # 함수 종료
    if i == len(arr):
        return
    else:
        s_sum += arr[i]
        # 합과 같다면 횟수 + 1
        if s_sum == K:
            cnt += 1
        i += 1
        # arr[i] 를 선택
        subset(i, s_sum, arr)
        # arr[i] 를 선택 X
        subset(i, s_sum - arr[i - 1], arr)


T = int(input())
for tc in range(1, T + 1):
    # 자연수 수 N, 합 K
    N, K = map(int, input().split())

    # N 개의 자연수
    arr = list(map(int, input().split()))

    # 경우의 수
    cnt = 0

    # 부분집합의 합 경우의 수 구하기
    subset(0, 0, arr)

    print(f'#{tc} {cnt}')