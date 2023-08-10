import sys
sys.stdin = open('sample_input.txt')

'''
# 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 표시한 영역을 몇 개나 만들어야 하는가?
1. 10x20, 20x20 종이로 빈틈없이 붙이기
2. 수열의 규칙을 찾는 것이 중요
3. 초항 제외 홀수 번째는 2^(n-1) 만큼 증가
4. 2항 제외 짝수 번째도 2^(n-1) 만큼 증가
'''

T = int(input())
for tc in range(1, T + 1):
    # 10 의 배수인 N
    N = int(input())

    # 테이프로 영역 만드는 횟수(홀 odd, 짝 even)
    odd = 0
    even = 0
    # N 을 10 으로 나눠서 홀수 짝수 파악하기
    for i in range(1, ((N // 10) + 1)):
        # 홀수일 때
        if (i % 2) == 1:
            # 초항은 1로 두고
            if i == 1:
                odd = 1
            # 그 다음 항부터 2^(i-1) 만큼 증가
            else:
                odd += (2 ** (i - 1))
        # 짝수일 때
        else:
            # 2항은 3으로 두고
            if i == 2:
                even = 3
            # 그 다음 항부터 2^(i-1) 만큼 증가
            else:
                even += (2 ** (i - 1))
    
    # 홀수일 땐 odd, 짝수일 땐 even 출력
    if (N // 10) % 2 == 1:
        print(f'#{tc} {odd}')
    else:
        print(f'#{tc} {even}')


