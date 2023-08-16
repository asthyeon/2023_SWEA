import sys
sys.stdin = open('sample_input.txt')

'''
# 한 줄에서 하나씩 N 개의 숫자를 골라 합이 최소가 되도록 하기
1. 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음
2. 백트래킹을 이용하기
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 자연수 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최소합
    stack = []
    # 최소 합(적당한 값 설정)
    arr_min_sum = 10000

    # 방문기록
    visited = [0] * N


    def permutation(i, N):
        global arr_min_sum
        # 행 순회를 다 돌면 순회하면서 찾은 숫자들을 더한 값과 최소 합을 비교하기
        if i == N:
            if arr_min_sum > sum(stack):
                arr_min_sum = sum(stack)
        # 3 개를 다 더하기도 전에 최소 합보다 크다면 종료
        if arr_min_sum < sum(stack):
            return
        # 행 순회를 돌 때
        else:
            # i = 행, j = 열, 행과 열이 중복되면 안됨
            for j in range(N):
                # 방문 기록하기(열 중복을 방지하기 위함)
                if visited[j] == 0:
                    # 방문하지 않았다면 stack push
                    stack.append(arr[i][j])
                    # 방문 기록
                    visited[j] = 1
                    # 다음 행의 방문 안한 곳 찾아서 재귀 호출
                    permutation(i + 1, N)
                    # 행 순회를 다 돌은 후에 이전에 방문한 곳 방문 초기화
                    visited[j] = 0
                    # 방문한 곳의 값 제거하기
                    stack.pop()

    permutation(0, N)
    print(f'#{tc} {arr_min_sum}')
