import sys
sys.stdin = open("sample_input.txt")

"""
# 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾기
1. 1일 이용권
2. 1달 이용권(1일 시작)
3. 3달 이용권(11월에 구매하면 12월까지)
4. 1년 이용권
"""

T = int(input())
for tc in range(1, T + 1):
    # 이용권 요금
    day, mon, thr_mon, year = map(int, input().split())
    # 이용 계획
    plan = list(map(int, input().split()))

    # 각 달의 요금
    fees = [0] * 12
    # 각 달의 요금 계산하기
    for i in range(12):
        if plan[i] != 0:
            # 해당 일수 x 일일요금이 한달 요금보다 크다면
            if plan[i] * day > mon:
                # 한달 요금
                fees[i] = mon
            # 반대라면 일일 요금
            else:
                fees[i] = plan[i] * day

    # 역순 복사본 만들기
    fees2 = fees[::-1]
    # 3개월 요금과 비교하기(순차적)
    for j in range(12):
        if fees[j] != 0:
            triple = 0
            # 요금이 있는 월일 때 3개월 치를 넣음
            for k in range(j, j + 3):
                if k < 12:
                    triple += fees[k]
            # 3개월 요금이 더 저렴하면 3개월 요금으로 교체
            if triple > thr_mon:
                fees[j] = thr_mon
                if j + 1 < 12:
                    fees[j + 1] = 0
                    if j + 2 < 12:
                        fees[j + 2] = 0

    # 3개월 요금과 비교하기(역순)
    for j in range(12):
        if fees2[j] != 0:
            triple = 0
            # 요금이 있는 월일 때 3개월 치를 넣음
            for k in range(j, j + 3):
                if k < 12:
                    triple += fees2[k]
            # 3개월 요금이 더 저렴하면 3개월 요금으로 교체
            if triple > thr_mon:
                fees2[j] = thr_mon
                if j + 1 < 12:
                    fees2[j + 1] = 0
                    if j + 2 < 12:
                        fees2[j + 2] = 0

    # 두 값 비교
    result = 0
    if sum(fees) > sum(fees2):
        result = sum(fees2)
    else:
        result = sum(fees)

    # 1년 요금과 비교
    if result > year:
        print(f'#{tc} {year}')
    else:
        print(f'#{tc} {result}')



