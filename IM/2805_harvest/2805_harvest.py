import sys
sys.stdin = open('input.txt')

"""
# 최대 수익 구하기
1. 농장의 크기는 항상 홀수
2. 수확은 농장의 크기에 딱맞는 정사각형 마름모 형태로만 가능
"""

T = int(input())
for tc in range(1, T + 1):
    # 농장 크기 N
    N = int(input())

    # 농장 형성
    arr = [list(map(int, input())) for _ in range(N)]

    # 조정할 변수 생성
    num = -1

    # 수익
    profit = 0

    # 1 칸일 때는 바로 출력
    if N == 1:
        profit += arr[0][0]
    # 그 외 세로부터 출발해서 좌우로 1칸씩 늘리고 줄이기
    else:
        for i in range(N):
            # 중간에 도달하기 전까지는 늘리기
            if i <= N // 2:
                num += 1
                for j in range(N // 2 - num, N // 2 + num + 1):
                    profit += arr[j][i]
            # 중간 이후로는 줄이기
            else:
                num -= 1
                for k in range(N // 2 - num, N // 2 + num + 1):
                    profit += arr[k][i]

    print(f'#{tc} {profit}')
                    