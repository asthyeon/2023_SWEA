import sys
sys.stdin = open('input.txt')

"""
# 최소한의 교환횟수 출력
1. 정류장에는 교체용 충전지가 있는 교환기가 있음
2. 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있음
3. 최소한의 교체 횟수로 목적지에 도착해야함
4. 출발지에서 배터리 장착은 교환횟수에서 제외
5. 마지막 정류장에는 배터리가 없음
@ 풀이
(1) 백트래킹으로 풀기
"""


def backtracking(idx, cnt, charge):
    global min_count
    # 목적지에 도착할 경우, 그 때의 교환횟수를 기록하고 재귀 종료
    if idx == stops[0]:
        if min_count > cnt:
            min_count = cnt
            return

    # 가지치기
    if min_count <= cnt:
        return

    # 충전한 만큼 가는데 최대치만큼 우선 전진
    for i in range(charge, 0, -1):
        # 간만큼 정류장 이동
        idx += i
        # 간만큼 충전량 감소
        charge -= i
        # 이전 충전량 저장
        tmp = charge
        # 목적지에 도달하지 못했다면 재귀로 반복하되 배터리 교환진행
        if idx < stops[0]:
            # 만일 남은 충전량이 충전할 수 있는 것보다 작다면 배터리 교환
            if charge < stops[idx]:
                charge = stops[idx]
                cnt += 1
                # 가지치기
                if min_count <= cnt:
                    idx -= i
                    charge = tmp + i
                    cnt -= 1
                    return
            backtracking(idx, cnt, charge)
            # 배터리를 교환했다면 카운트 -1 및 배터리를 교체 이전으로 복구
            if tmp < stops[idx]:
                cnt -= 1
                charge = tmp
        # 목적지에 도착했다면 재귀로 반복하여 재귀 종료
        elif idx == stops[0]:
            backtracking(idx, cnt, charge)
        # 목적지를 넘어서거나 재귀에서 나온후
        # 간만큼 다시 돌아오고 충전량 복구
        idx -= i
        charge += i


T = int(input())
for tc in range(1, T + 1):
    # 정류장 수 및 정류장 별 배터리 용량
    stops = list(map(int, input().split()))

    # 현재 정류장 위치
    idx = 1
    # 현재 충전량
    charge = stops[1]
    # 교환횟수
    cnt = 0
    min_count = 100

    backtracking(idx, cnt, charge)
    print(f'#{tc} {min_count}')