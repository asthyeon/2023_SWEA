import sys
sys.stdin = open('sample_input.txt')

"""
# 손해를 보지 않는 한 최대한 많은 집에 홈방범 서비스 제공하기
1. 운영 비용: K * K + (K - 1) * (K - 1) (K 는 1 이상의 정수)
2. 도시를 벗어난 영역에 제공해도 운영 비용은 변경되지 않음
3. 집이 있는 위치: 1, 나머지: 0
@ 풀이
(1) 마름모 영역을 구하는 함수를 만들고 K 가 최대가 될 때까지 반복
"""


# 마름모 영역 구하는 함수
def rhombus(x, y, K):
    # 탐색하는 한 줄의 수를 조절할 변수
    left = -1
    right = 0
    # 수익
    revenue = 0
    # 집들의 수
    cnt = 0
    for fy in range(y - K + 1, y + K):
        # 마름모 중간 포함한 윗부분
        if fy <= y:
            left += 1
            right += 1
        # 아랫부분
        else:
            left -= 1
            right -= 1
        for fx in range(x - left, x + right):
            # 벽 형성
            if 0 <= fx < N and 0 <= fy < N:
                if city[fx][fy] == 1:
                    revenue += M
                    cnt += 1
    return cnt, revenue


T = int(input())
for tc in range(1, T + 1):
    # 도시의 크기 N, 하나의 집이 지불하는 비용 M
    N, M = map(int, input().split())

    # 도시 입력
    city = [list(map(int, input().split())) for _ in range(N)]

    # 서비스를 제공받는 최대 집 수
    cnt_max = 0

    # 도시 탐색
    K = 0
    # 마름모가 전체를 덮을 때까지 반복
    while K < N + 1:
        K += 1
        # 운영 비용
        fee = (K * K) + ((K - 1) * (K - 1))

        # 전체 탐색
        for x in range(N):
            for y in range(N):
                cnt, revenue = rhombus(x, y, K)
                if revenue >= fee:
                    if cnt_max < cnt:
                        cnt_max = cnt

    print(f'#{tc} {cnt_max}')