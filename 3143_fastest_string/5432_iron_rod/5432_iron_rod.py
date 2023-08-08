import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 테스트 케이스 입력
    laser = input()

    # 쇠막대기 수
    iron = 0
    laserbeam = 0

    # 쇠막대기 구하기
    for i in range(len(laser) - 1):
        if laser[i] == '(' and laser[i + 1] == '(':
            iron += 1
    # 레이저 수 구하기
    for i in range(len(laser) - 2):
        if laser[i + 1] == '(' and laser[i + 2] == ')':
            if laser[i] == '(' or laser[i] == ')':
                laserbeam += 1

    print(tc, iron)
    print(tc, laserbeam)

    # print(f'#{tc} {count}')

    # ( )(((( )( )) (( ))( ))) (( ))
    #  |     |  |     |   |      |
    #  |   --|--|-- --|-- |      |
    #  |  ---|--|-----|---|--    |
    #  | ----|--|-----|---|--- --|--
    # 레이저 5개 맞음 -> 17
    # 쇠막대기 수: 5
    #
    # (((( )(( )( ))) (( ))( ))) (( )( ))
    #     |   |  |      |   |      |  |
    #     | --|--|--    |   |      |  |
    #   --|---|--|--- --|-- |      |  |
    #  ---|---|--|------|---|--    |  |
    # ----|---|--|------|---|--- --|--|--
    # 레이저 7개 맞음 -> 24
    # 쇠막대기 수: 6