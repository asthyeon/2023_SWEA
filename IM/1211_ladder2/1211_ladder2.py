import sys
sys.stdin = open('input.txt')

"""
# 바닥에 내려가는 최단경로 찾기
"""


# 사다리 타기 함수 형성
def ladder(sx, sy, arr):
    # 움직인 횟수
    cnt = 0
    # 사다리 복사
    arr2 = [a[:] for a in arr]
    # 사다리 타기
    while sx > 0:
        # 상이동
        if arr2[sx - 1][sy] == 1:
            sx -= 1
            cnt += 1

        # 좌이동
        # 벽형성
        if sy > 0:
            if arr2[sx][sy - 1] == 1:
                # 지나온 길은 0으로 만들기
                arr2[sx][sy] = 0
                sy -= 1
                cnt += 1

        # 우이동
        # 벽 형성
        if sy < 99:
            # 한 칸 이동했을 때 1 일경우
            if arr2[sx][sy + 1] == 1:
                # 지나온 길은 0으로 만들기
                arr2[sx][sy] = 0
                sy += 1
                cnt += 1

    return cnt, sy


for tc in range(1, 11):
    T = int(input())
    # 사다리 받기
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최단거리 리스트
    short = []

    # 사다리 타기
    for sy in range(100):
        if arr[99][sy] == 1:
            short.append(ladder(99, sy, arr))

    # 오름차순 정렬
    short.sort()

    print(f'#{T} {short[0][1]}')
