import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(T, T + 1):
    N = int(input())
    cnt = [0] * 5001 # 1-5000번 각 정류장을 지나는
    for _ in range(N): # N 개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1 # 현재 노선

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end = ' ')
    for x in bus_stop:
        print(cnt[x], end = ' ')
    print()