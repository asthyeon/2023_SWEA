import sys
sys.stdin = open('sample_input.txt')

"""
# 입력 순서대로 이진 최소힙에 저장, 마지막 노드의 조상 노드에 저장된 정수의 합 알아내기
1. 부모 노드의 값 < 자식 노드의 값
2. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때 까지 부모 노드와 교체
"""


# 최소 힙 함수
def heap(arr, arr_idx):
    # 부모 노드보다 작다면 교체
    if arr[arr_idx // 2] > arr[arr_idx]:
        arr[arr_idx // 2], arr[arr_idx] = arr[arr_idx], arr[arr_idx // 2]
        # 부모 위치에서 다시 힙 함수 적용
        heap(arr, (arr_idx // 2))
    # 부모 노드보다 크다면 함수 종료
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N 개의 자연수
    numbers = list(map(int, input().split()))

    # 빈 이진 힙 배열 만들기
    arr = [0] * (N + 1)

    # 배열 순서
    arr_idx = 1

    # 입력받은 자연수를 arr 에 배열하기
    for number in numbers:
        # 마지막 노드에 값 추가
        arr[arr_idx] = number
        # 힙
        heap(arr, arr_idx)
        # 인덱스 이동
        arr_idx += 1

    # 마지막 노드의 조상 노드의 합 구하기
    total = 0
    while True:
        if N >= 1:
            total += arr[N // 2]
            N = N // 2
        else:
            break

    print(f'#{tc} {total}')