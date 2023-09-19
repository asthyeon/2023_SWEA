import sys
sys.stdin = open('input.txt')

"""
# 제품의 최소 생산 비용 구하기
1. N 종의 제품을 N 곳의 공장에서 한 곳당 한가지씩 생산
@ 풀이
(1) 백트래킹으로 풀기
(2) 중복이 없는 선택
"""


# 백트래킹 함수
def backtracking(cnt, cost):
    global min_cost
    # 재귀를 종료할 기저 조건
    if cnt == N - 1:
        # 최소값 교체
        if min_cost > cost:
            min_cost = cost
        return

    # 최소값보다 이미 현재 비용이 더 크다면 가지치기
    if min_cost <= cost:
        return
    
    # 조합 만들기
    for num in arr:
        # 이미 숫자가 있다면 가지치기
        if num in path:
            continue
        
        # path 에 숫자 넣고 해당하는 비용 넣기 
        path[cnt] = num
        cost += production[cnt][num]
        # 최소값보다 이미 현재 비용이 더 크다면 가지치기
        if min_cost <= cost:
            cost -= production[cnt][num]
            path[cnt] = -1
            continue
        # 재귀
        backtracking(cnt + 1, cost)
        # 재귀 후 이전 비용으로 복구 및 새로운 조합 찾기
        cost -= production[cnt][num]
        path[cnt] = -1


T = int(input())
for tc in range(1, T + 1):
    # 제품 수 N
    N = int(input())
    # 공장 x 제품 별 생산비용
    production = [list(map(int, input().split())) for _ in range(N)]
    # 최소 생산비용
    min_cost = 99 * 15
    cost = 0
    # 조합을 구하기 위한 변수들
    cnt = -1
    path = [-1] * N
    arr = [i for i in range(N)]

    backtracking(cnt, cost)

    print(f'#{tc} {min_cost}')