import sys
sys.stdin = open('sample_input.txt')

"""
# N 개의 과목 중 K 개의 과목을 선택해서 넣어서 총점 만들기
"""

T = int(input())
for tc in range(1, T + 1):
    # 과목 N개, 선택 K개
    N, K = map(int, input().split())

    # N 개의 점수들
    grades = list(map(int, input().split()))

    # 역순 정렬
    grades.sort(reverse=True)

    # 총점 만들기
    total = 0
    for i in range(K):
        total += grades[i]

    print(f'#{tc} {total}')