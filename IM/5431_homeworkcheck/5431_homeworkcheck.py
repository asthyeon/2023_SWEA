import sys
sys.stdin = open('sample_input.txt')

"""
# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력
"""

T = int(input())
for tc in range(1, T + 1):
    # 수강생 수: N, 과제 제출한 사람 수:K
    N, K = map(int, input().split())

    # 과제 제출한 사람 번호 리스트
    K_list = list(map(int, input().split()))

    # 수강생 리스트
    N_list = [i for i in range(1, N + 1)]

    # 과제 제출한 사람 제외하기
    for Ki in K_list:
        N_list.remove(Ki)

    print(f'#{tc}', *N_list)