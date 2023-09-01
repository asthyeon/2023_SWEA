import sys
sys.stdin = open('input.txt')

"""
# 손님에게 거슬러야할 돈을 최소 개수로 거슬러주기
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 각 화폐를 최대 수로 넣어보기
    moneys = []
    moneys.append(N // 50000)
    N %= 50000
    moneys.append(N // 10000)
    N %= 10000
    moneys.append(N // 5000)
    N %= 5000
    moneys.append(N // 1000)
    N %= 1000
    moneys.append(N // 500)
    N %= 500
    moneys.append(N // 100)
    N %= 100
    moneys.append(N // 50)
    N %= 50
    moneys.append(N // 10)

    # 최소 개수 출력
    print(f'#{tc}')
    print(*moneys)
