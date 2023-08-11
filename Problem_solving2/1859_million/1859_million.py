import sys
sys.stdin = open('input.txt')

'''
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 돕기
1. 원재는 연속된 N 일 동안의 물건의 매매가를 예측하여 알고 있음
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입 가능
3. 판매는 언제든지 가능
4. 오늘 날짜와 가장 큰 날짜 값의 차이들을 계속 더하기
5. 날짜를 역순으로 해서 계산하기
'''

T = int(input())
for tc in range(1, T + 1):
    # 연속된 N 일
    N = int(input())

    # 각 날의 매매가를 나타내는 N 개의 자연수
    price = list(map(int, input().split()))

    # 전체 이익
    profit = 0

    # 최대 값(맨 마지막날)
    price_max = price[-1]

    # 역순으로 계산하기
    for i in range(N - 2, -1, -1):
        # 최대값보다 i 번째 가격이 더 크다면
        if price_max < price[i]:
            # 최대값 교체
            price_max = price[i]
        # 최대값이 i 번째 가격보다 크다면
        if price[i] < price_max:
            # 둘의 차이를 이익에 더하기
            profit += price_max - price[i]

    print(f'#{tc} {profit}')
