import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # D: 기차 전면부 사이 거리. A: A기차 속력, B: B기차 속력, F: 파리 속력
    D, A, B, F = map(int, input().split())

    # 기차가 충돌하는 시간 구하기
    # D = Ax + Bx = (A + B)x
    # x = D / (A + B)
    crash = D / (A + B)

    # 파리가 이동한 거리
    F_distance = F * crash

    print(f'#{tc} {F_distance}')
