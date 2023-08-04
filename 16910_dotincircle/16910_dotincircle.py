import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 원 안에 포함 되는 격자점의 개수
    count = 0

    # x 와 y 범위 적당하게 설정하기
    for x in range(-N, N + 1):
        for y in range(-1000, 1000):
            # 수식을 만족한다면
            if (N ** 2) >= (x ** 2) + (y ** 2):
                # 격자점 +1
                count += 1

    print(f'#{tc} {count}')