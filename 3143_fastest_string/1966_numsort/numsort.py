import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # # 버블 정렬
    # def BubbleSort(arr, N):
    #     for i in range(N - 1, 0, -1):
    #         for j in range(i):
    #             if arr[j] > arr[j + 1]:
    #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #
    #     print(f'#{tc}', *arr)
    #
    # BubbleSort(arr, N)

    # 선택 정렬
    def selectionSort(arr, N):
        for i in range(N - 1):
            # 기준 인덱스 지정
            minIdx = i
            for j in range(i + 1, N):
                # 최소값을 찾고, 기준 인덱스를 바꿔주기
                if arr[minIdx] > arr[j]:
                    minIdx = j
            # 가장 작은 값을 찾았으면 위치 교체
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
        
        # 출력
        print(f'#{tc}', *arr)
    
    # 함수 사용
    selectionSort(arr, N)
