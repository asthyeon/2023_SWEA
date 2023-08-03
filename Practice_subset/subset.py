import sys
sys.stdin = open('input.txt')

T = 3
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    # 부분집합 리스트 형성
    subset_list = []
    for i in range(1 << 10):
        for j in range(10):
            if i & (1 << j):
                print(arr[j], end = ' ')
        print()
    print(subset_list)



