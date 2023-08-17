import sys
sys.stdin = open('input.txt')

'''
# 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하기
1. 0 초부터 빵을 만들기 시작
2. M 초의 시간을 들이면 K 개의 붕어빵 만들 수 있음
'''


T = int(input())
for tc in range(1, T + 1):
    # 손님 N, 만드는 초 M, 만드는 붕어빵 수 K
    N, M, K = map(int, input().split())

    # 각 사람이 언제 도착하는지 초 단위
    vips = list(map(int, input().split()))

    # 손님을 시간 순으로 정렬하기
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if vips[j] > vips[j + 1]:
                vips[j], vips[j + 1] = vips[j + 1], vips[j]

    # 인덱스용
    front = 0

    # 시간
    time = 0
    realtime = 0
    remain = 0

    # 붕어빵 수
    total = 0

    while True:
        # 붕어빵 손님시간이 맞을 때 판매한 수
        count = 0
        # 붕어빵 수를 구하기 위한 시간
        time = vips[front] - realtime + remain
        # 현재 흐른 진짜 시간
        realtime = vips[front]
        # 붕어빵 수
        total += (time // M) * K

        # 현재 흐른시간하고 같은 손님 빼기
        while True:
            if front < N:
                if vips[front] == realtime:
                    count += 1
                    front += 1
                else:
                    break
            else:
                break
        
        # 판매한 수만큼 빼서 정답 오답 구분하기
        total -= count
        if total < 0:
            print(f'#{tc} Impossible')
            break

        if front == N:
            print(f'#{tc} Possible')
            break

        # 이전에 남아있던 잔여시간
        remain = time % M






