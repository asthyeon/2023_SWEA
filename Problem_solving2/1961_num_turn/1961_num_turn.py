import sys
sys.stdin = open('input.txt')

'''
# N x N 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양 출력
1. 각 회전 각도에 맞게 몇번째를 출력하는지 확인하기
'''
from pprint import pprint
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N x N 행렬
    data = [list(input().split()) for _ in range(N)]

    # 빈 어레이 형성
    arr = ['' * N for _ in range(N)]

    for i in range(N):
        # 90도
        for j in range(N):
            arr[i] += data[N - j - 1][i]
        
        # 공백 삽입
        arr[i] += ' '

        # 180도
        for k in range(N):
            arr[i] += data[N - i - 1][N - k - 1]
        
        # 공백 삽입
        arr[i] += ' '

        # 270도
        for l in range(N):
            arr[i] += data[l][N - i - 1]

    # 출력
    print(f'#{tc}')
    for m in range(N):
        print(arr[m])

