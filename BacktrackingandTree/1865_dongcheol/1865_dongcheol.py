import sys
sys.stdin = open('input.txt')

"""
# 주어진 일이 모두 성공할 확률의 최대값 구하기
1. 직원들에게 공평하게 일을 하나씩 분배해야함
2. i 번 직원이 j 번 일을 성공할 확률 = p
3. 확률을 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력
@ 풀이
(1) 백트래킹으로 풀기
"""


# 백트래킹 함수
def backtracking(cnt, per):
    global max_per
    # 재귀를 종료하기 위한 기저 조건
    if cnt == N - 1:
        if max_per < per:
            max_per = per
        return

    # 가지치기
    if max_per >= per:
        return

    # 조합 만들기
    for num in arr:
        # 이미 숫자가 path 에 들어있다면 가지치기
        if num in path:
            continue
        # 확률이 0 일 때 가지치기
        if probability[cnt][num] == 0:
            continue
        # 숫자가 path 에 없다면
        path[cnt] = num
        per *= probability[cnt][num] / 100
        # 가지치기
        if max_per >= per:
            path[cnt] = -1
            per /= probability[cnt][num] / 100
            continue
        backtracking(cnt + 1, per)
        # 재귀 후 원상복구
        per /= probability[cnt][num] / 100
        path[cnt] = -1


T = int(input())
for tc in range(1, T + 1):
    # 직원 N 명
    N = int(input())
    
    # 각 직원이 성공할 확률
    probability = [list(map(int, input().split())) for _ in range(N)]
    # 최대 확률
    max_per = 0
    per = 1
    # 조합을 구하기 위한 변수들
    arr = [i for i in range(N)]
    path = [-1] * N
    cnt = -1

    backtracking(cnt, per)
    print(f'#{tc} {max_per * 100:.6f}')