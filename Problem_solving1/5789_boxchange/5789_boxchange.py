import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N 개의 상자, Q 회 동안의 작업
    N, Q = map(int, input().split())

    # N 개의 상자 리스트 생성
    arr = [0] * N

    # Q 번 을 반복하는 i 번째 줄
    for i in range(1, Q + 1):
        # L 번 상자부터 R 번 상자의 값
        L, R = map(int, input().split())
        # L 번 상자부터 R 번 상자의 값을 i 로 변경
        for j in range(L - 1, R):
            arr[j] = i

    print(f'#{tc}', *arr)