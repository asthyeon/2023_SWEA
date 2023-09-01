import sys
sys.stdin = open("sample_input.txt")

"""
# 최대한 많은 수익 얻기
1. 두 명의 일꾼은 가로로 연속되도록 M 개의 벌통을 선택(겹치면 안됨)
2. 일꾼이 채취할 수 있는 꿀의 최대 양은 C
3. 각 용기에 있는 꿀의 양의 제곱만큼 수익이 생김
"""

T = int(input())
for tc in range(1, T + 1):
    # 벌통 크기 N, 선택가능한 벌통 수 M, 최대 양 C
    N, M, C = map(int, input().split())
    
    # 벌통 만들기
    hive = [list(map(int, input().split())) for _ in range(N)]

    # 일꾼 1의 이익 형성
    profit = 0
    # 일꾼 1 최대 수익
    for x in range(N):
        for y in range(N):
            # 델타 탐색
            for dx, dy in [[0, 1], [0, -1]]:
                # q 형성(일꾼 1이 꿀을 채취하고 그 자리를 비우게 하기 위함)
                q = []
                # 현재 위치 인큐
                q.append((x, y))
                nx, ny = x, y
                # 벌통 선택하기
                for _ in range(M - 1):
                    nx, ny = nx + dx, ny + dy
                    # 벽 형성
                    if 0 <= nx < N and 0 <= ny < N:
                        q.append((nx, ny))
                # M 개만큼 벌통이 선택되었다면
                if len(q) == M:
                    # 모든 부분집합 구하기(모든 경우의 수)
                    for i in range(1 << M):
                        subset = []
                        revenue = 0
                        total = 0
                        for j in range(M):
                            if i & (1 << j):
                                subset.append(q[j])
                        # 모든 부분집합의 합이 C 보다 작다면 제곱으로 수익으로 넣기
                        for k in range(len(subset)):
                            total += hive[subset[k][0]][subset[k][1]]
                            revenue += hive[subset[k][0]][subset[k][1]] ** 2
                        if total <= C:
                            if profit < revenue:
                                profit = revenue
                                nq = q

    # 채취한 벌꿀 제거
    for i in range(len(nq)):
        hive[nq[i][0]][nq[i][1]] = 0

    # 일꾼 2의 이익 형성
    profit2 = 0
    # 일꾼 2 최대 수익
    for x in range(N):
        for y in range(N):
            # 채취한 꿀 제외
            if hive[x][y] != 0:
                # 델타 탐색
                for dx, dy in [[0, 1], [0, -1]]:
                    # q 형성(일꾼 1이 꿀을 채취하고 그 자리를 비우게 하기 위함)
                    q2 = []
                    # 현재 위치 인큐
                    q2.append((x, y))
                    nx, ny = x, y
                    # 벌통 선택하기
                    for _ in range(M - 1):
                        nx, ny = nx + dx, ny + dy
                        # 벽 형성
                        if 0 <= nx < N and 0 <= ny < N:
                            # 채취한 꿀 제외
                            if hive[nx][ny] == 0:
                                break
                            q2.append((nx, ny))
                    # M 개만큼 벌통이 선택되었다면
                    if len(q2) == M:
                        # 모든 부분집합 구하기(모든 경우의 수)
                        for i in range(1 << M):
                            subset = []
                            revenue2 = 0
                            total2 = 0
                            for j in range(M):
                                if i & (1 << j):
                                    subset.append(q2[j])
                            # 모든 부분집합의 합이 C 보다 작다면 제곱으로 수익으로 넣기
                            for k in range(len(subset)):
                                total2 += hive[subset[k][0]][subset[k][1]]
                                revenue2 += hive[subset[k][0]][subset[k][1]] ** 2
                            if total2 <= C:
                                if profit2 < revenue2:
                                    profit2 = revenue2
                                    nq2 = q2

    # 최대 이익 만들기
    result = profit + profit2

    print(f'#{tc} {result}')

