import sys
sys.stdin = open('input.txt')

"""
# B에 속한 어떤 수가 A에도 들어있으면서, 동시에 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수 알아보기
1. 정수 N개가 주어지면 정렬하여 리스트 A에 저장
2. 리스트 B에 저장된 M 개의 정수에 대해 A에 대해 들어있는 수인지 이진 탐색을 통해 확인
3. 시작인덱스 l, 끝 인덱스 r, 중심 원소의 인덱스 m = (l+r) // 2
4. 이진 탐색의 왼쪽구간: l ~ m-1
5. 이진 탐색의 오른쪽구간: m+1 ~ r 
"""


# 이진 탐색 함수
def binary_search(A, x):
    start = 0
    end = N - 1
    # 탐색으로 찾은 경우
    finding = False
    # 좌우를 반복탐색할 스위치
    switch = []
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == x:
            finding = True
            break
        elif A[mid] > x:
            end = mid - 1
            switch.append(1)
        else:
            start = mid + 1
            switch.append(2)
    # 탐색으로 숫자를 찾았다면
    if finding is True:
        # 스위치가 좌우를 반복했는지 확인
        for i in range(1, len(switch)):
            # 좌우를 반복하지 않았다면 False
            if switch[i - 1] == switch[i]:
                return False
        # 반복했다면
        else:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    # 리스트 A의 정수 개수 N, 리스트 B의 정수 개수 M
    N, M = map(int, input().split())
    # 리스트 A
    A = list(map(int, input().split()))
    # 리스트 A 정렬하기
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    # 리스트 B
    B = list(map(int, input().split()))
    # 조건을 만족하는 정수 개수
    cnt = 0

    # 이진 탐색
    for x in B:
        result = binary_search(A, x)
        if result is True:
            cnt += 1

    print(f'#{tc} {cnt}')