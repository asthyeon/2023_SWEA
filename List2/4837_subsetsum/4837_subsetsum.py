import sys
sys.stdin = open('sample_input.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T + 1):
    # 부분집합 원소의 수: N, 부분집합의 합: K
    N, K = map(int, input().split())
    # 존재 여부
    exist = 0

    # A의 부분집합 구하기
    for i in range(1 << 12):
        # 부분집합의 합
        total = 0
        # 부분집합의 원소의 수를 구할 리스트 생성
        subset_list = []
        for j in range(12):
            # 부분집합이라면 합하고, 리스트에 넣기
            if i & (1 << j):
                total += A[j]
                subset_list.append(A[j])
        # 만약 합이 K와 같고, 원소의 수의 길이가 N과 같다면
        if total == K and len(subset_list) == N:
            # 존재하는 것으로 여기고 exist 1로 바꾸기
            exist += 1

    print(f'#{tc} {exist}')
