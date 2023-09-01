import sys
sys.stdin = open('s_input.txt')

"""
# 단조 증가 수를 구하고 최댓값 출력하기
1. 단조 증가: 각 숫자의 자릿수가 단순하게 증가
2. 정수들 중에서 곱한 값이 단조 증가인지 구하고 최댓값 출력
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N개의 정수
    numbers = list(map(int, input().split()))

    # 정답 조건
    answer = -1

    # 최댓값 구하기
    for i in range(N - 1):
        for j in range(i + 1, N):
            number = numbers[i] * numbers[j]
            # 단조 증가 확인
            monotone = 0
            for k in range(1, len(str(number))):
                if str(number)[k] < str(number)[k - 1]:
                    monotone = -1
                    break
            if monotone != -1:
                if answer < number:
                    answer = number

    print(f'#{tc} {answer}')


