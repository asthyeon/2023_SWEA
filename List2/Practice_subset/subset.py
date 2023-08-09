import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    # 존재하는지 안하는지의 값
    exist = 0

    # 부분집합 생성
    # i 가 1부터 시작하는 것으로 처음에 값이 없을 때 합이 0 이 되는 것을 막음 
    for i in range(1, 1 << 10):
        # 부분집합의 합
        total = 0
        for j in range(10):
            if i & (1 << j):
                total += arr[j]
        # 합이 0이 되는 경우가 있다면 존재하므로 exist 1로 변환
        if total == 0:
            exist = 1

    print(f'#{tc} {exist}')




