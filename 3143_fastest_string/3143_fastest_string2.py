import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    cnt = 0
    i, j = 0, 0

    while i < len(A):
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == len(B):
            j = 0
            cnt += 1

    print(f'#{tc} {cnt}')
