import sys
sys.stdin = open('input.txt')

"""
# 가장 적은 비용으로 수영장 이용하기
1. 수영장 이용권
 - 1일
 - 1달(매달 1일 시작)
 - 3달(매달 1일 시작), 그 해것만 가능(예: 11 & 12, 12 도 3달권이고 다음해로 안넘어감)
 - 1년
"""

T = int(input())
for tc in range(1, T + 1):
    # 이용권 가격들
    day, mon, three, year = map(int, input().split())

    # 12개월 이용 계획
    plan = list(map(int, input().split()))
    do_plan = [0] * 12

    # 1일 이용권과 1달 이용권 비교하여 요금으로 환산
    for i in range(12):
        if plan[i] == 0:
            do_plan[i] = 0
        elif plan[i] * day >= mon:
            do_plan[i] = mon
        else:
            do_plan[i] = plan[i] * day

    # 1달 이용권과 3달 이용권 비교하여 요금으로 환산
    dp = [0] * 12
    # 3월까지는 3달권과 비교하여 계산
    dp[0] = min(do_plan[0], 
                three)
    dp[1] = min(dp[0] + do_plan[1], 
                three)
    dp[2] = min(dp[1] + do_plan[2], 
                three)
    # 4월부터는 따로 계산
    for j in range(3, 12):
        # 자신을 포함한 각각의 3개월치 vs 3개월분  
        dp[j] = min(dp[j - 1] + do_plan[j],
                    dp[j - 2] + do_plan[j - 1] + do_plan[j],
                    dp[j - 3] + three)
        # 마지막달은 1년치와도 비교
        dp[11] = min(dp[j - 1] + do_plan[j],
                     dp[j - 2] + do_plan[j - 1] + do_plan[j],
                     dp[j - 3] + three,
                     year)

    print(f'#{tc} {dp[-1]}')
