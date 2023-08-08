import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 조망권이 확보된 세대 수 초기화
    view = 0

    for i in range(N):
        # i 가 0 일 때는 건너뛰기
        if i == 0:
            continue
        else:
            # i가 좌 2칸, 우 2칸보다 클 때,
            if arr[i] > arr[i - 1] and\
                    arr[i] > arr[i - 2] and\
                    arr[i] > arr[i + 1] and\
                    arr[i] > arr[i + 2]:
                # 차이 초기화
                minus = 0
                # 차이를 담을 리스트 형성
                minus_list = []
                # 1 칸 차이, 2칸 차이 각각 비교
                for j in range(1, 3):
                    left = arr[i] - arr[i - j]
                    right = arr[i] - arr[i + j]
                    # 더 작은 값 minus 로 지정
                    if left > right:
                        minus = right
                    else:
                        minus = left
                    # 더 작은 값을 리스트에 담음
                    minus_list.append(minus)
                # 리스트에 담긴 두 값을 비교하여 작은 값을 view 에 더함
                if minus_list[0] > minus_list[1]:
                    view += minus_list[1]
                else:
                    view += minus_list[0]

    print(f'#{tc} {view}')