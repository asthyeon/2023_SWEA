import sys
sys.stdin = open('input.txt')

"""
# 퀵 정렬을 구현해 N 개의 정수를 정렬해 리스트 A에 넣고, A[N // 2]에 저장된 값 출력하기
@ 풀이
(1) 피봇을 중앙값으로 설정하기
"""


# 분할 함수
def hoare_partition(arr, l, r):
    p = arr[(l + r) // 2]
    print(f'p = arr[{(l + r) // 2}] = {p}')

    while l <= r:
        # 피봇보다 크거나 같은 수 찾기
        while arr[l] < p:
            l += 1
        # 피봇보다 작거나 같은 수 찾기
        while arr[r] > p:
            r -= 1

        print(f'left = {l} / right = {r} / arr = {arr}')

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    return l


# 퀵 정렬 함수
def quicksort(arr, l, r):
    if l >= r:
        return

    p = hoare_partition(arr, l, r)
    quicksort(arr, l, p - 1)
    quicksort(arr, p, r)


T = int(input())
for tc in range(1, T + 1):
    # 정수의 개수 N
    N = int(input())
    # N 개의 정수
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N - 1)

    print(f'#{tc} {arr[N // 2]}')


