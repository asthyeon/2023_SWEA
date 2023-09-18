import sys
sys.stdin = open('input.txt')

"""
# 제약 조건을 만족하는 병합 정렬
1. N 개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0: N // 2], L[N // 2: N]으로 분할
2. N // 2 번째 원소 출력
3. 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 출력(오른쪽 원소가 먼저 복사되는 경우의 수)
"""


# 병합 함수
def merge(l, r):
    global cnt
    result = []
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크다면 cnt += 1(오른쪽 원소가 먼저 복사)
    if l[-1] > r[-1]:
        cnt += 1
    # 인덱스 조정
    l_idx = 0
    r_idx = 0
    # 한쪽이 빌 때까지 반복
    while len(l) > l_idx or len(r) > r_idx:
        # 둘 다 비지 않았다면
        if len(l) > l_idx and len(r) > r_idx:
            # 두 리스트의 가장 앞에 있는 것 중 작은 것을 선택하여 result에 추가
            if l[l_idx] <= r[r_idx]:
                result.append(l[l_idx])
                l_idx += 1
            else:
                result.append(r[r_idx])
                r_idx += 1
        # 한 쪽만 비어있다면, 남은 것을 모두 result에 추가
        elif len(l) > l_idx:
            result.append(l[l_idx])
            l_idx += 1
        elif len(r) > r_idx:
            result.append(r[r_idx])
            r_idx += 1

    return result


# 병합 정렬 함수
def merge_sort(arr):
    # 길이가 1인 배열까지 나누면 stop
    if len(arr) == 1:
        return arr

    l = []
    r = []
    mid = len(arr) // 2
    # 왼쪽을 따로 리스트에 저장
    for left in arr[:mid]:
        l.append(left)
    # 오른쪽을 따로 리스트에 저장
    for right in arr[mid:]:
        r.append(right)

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)


T = int(input())
for tc in range(1, T + 1):
    # 정수의 개수 N
    N = int(input())

    # N 개의 정수
    arr = list(map(int, input().split()))

    # 오른쪽 원소가 먼저 복사되는 경우의 수
    cnt = 0

    # 병합 정렬
    arr = merge_sort(arr)

    print(f'#{tc} {arr[N // 2]} {cnt}')