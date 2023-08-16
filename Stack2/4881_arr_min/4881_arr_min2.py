import sys
sys.stdin = open('sample_input.txt')

'''
# 한 줄에서 하나씩 N 개의 숫자를 골라 합이 최소가 되도록 하기
1. 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음
2. 순열을 이용하기
'''

T = int(input())
for tc in range(1, T + 1):
    # N x N 배열
    N = int(input())

    # 배열 형성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 순열 형성을 위한 리스트
    per_list = [k for k in range(N)]

    # stack 형성
    stack = []

    # 최소 합
    arr_min_sum = 100000

    # 순열 함수
    def permutation(i, N, per_list):
        global arr_min_sum

        # 모든 행 순회가 끝난다면
        if i == N:
            # 각 순열에 해당하는 행과 열의 값 더하기
            arr_min = 0
            for k in range(N):
                arr_min += arr[k][per_list[k]]
                # 다 더하기 이전에 최소값보다 커지면 중단하기
                if arr_min_sum < arr_min:
                    break
            # 최소 합과 비교하여 최소 합으로 교체하기
            if arr_min_sum > arr_min:
                arr_min_sum = arr_min

        # 행 순회
        else:
            # 자신과 자신의 오른쪽만 자리 바꾸기 (중복을 제거하기 위함)
            for j in range(i, N):
                # 위치 바꾸기
                per_list[i], per_list[j] = per_list[j], per_list[i]
                # 행을 바꾸고 재귀 호출하기
                permutation(i + 1, N, per_list)
                # 위치 복귀
                per_list[i], per_list[j] = per_list[j], per_list[i]

    permutation(0, N, per_list)
    print(f'#{tc} {arr_min_sum}')
