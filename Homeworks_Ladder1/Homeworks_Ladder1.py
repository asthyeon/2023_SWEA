import sys
sys.stdin = open('test.txt')

for tc in range(1, 2):
    # 테스트케이스 번호
    T = int(input())
    # 사다리 형성
    arr = [list(map(int, input().split())) for _ in range(8)]

    # 도착지에서부터 출발
    # 도착지 좌표
    x = 7
    y = 0
    # 도착지 y좌표 구하기
    for i in range(8):
        if arr[x][i] == 2:
            y = i
    print(tc, y)
    # X가 0이 될 때 멈추기
    # while x > 0:
    #     # 위로 이동
    #     for i in range(x, -1, -1):
    #         nx = i - 1
    #         if arr[nx][y] == 0:
    #             x = i
    #             break
    #         break
    #
    #     # 좌로 이동
    #     for i in range(y, -1, -1):
    #         ny = i - 1
    #         if arr[x][ny] == 0:
    #             y = i
    #             break
    #         break
    #
    #     # 우로 이동
    #     for i in range(y, 100):
    #         ny = i + 1
    #         if arr[x][ny] == 0:
    #             y = i
    #             break
    #         break
    #
    # print(tc, y)





