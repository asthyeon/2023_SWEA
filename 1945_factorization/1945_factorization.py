import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 변수 값 설정
    a = b = c = d = e = 0

    # 소인수 분해
    while True:
        if (N / 2) == int(N / 2):
            N = N / 2
            a += 1
        if (N / 3) == int(N / 3):
            N = N / 3
            b += 1
        if (N / 5) == int(N / 5):
            N = N / 5
            c += 1
        if (N / 7) == int(N / 7):
            N = N / 7
            d += 1
        if (N / 11) == int(N / 11):
            N = N / 11
            e += 1
        # N 이 1보다 작거나 같을 때 반복문 종료
        if N <= 1:
            break

    print(f'#{tc} {a} {b} {c} {d} {e}')