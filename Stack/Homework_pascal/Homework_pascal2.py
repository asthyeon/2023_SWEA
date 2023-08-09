import sys
sys.stdin = open('input.txt')

'''
# 파스칼의 삼각형이란
1. 첫 번째 줄은 항상 숫자 1이다
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
'''

# 재귀함수 써보기
T = int(input())
for tc in range(1, T + 1):
    # 크기가 N 인 파스칼의 삼각형
    N = int(input())

    # pascal 첫 째줄
    pascal = [1]

    # 재귀함수
    def recur_func(N):
        # 종료조건 형성
        if N == 0:
            return
        # 재귀함수 호출(N을 1부터 역순으로 하기 위함)
        recur_func(N - 1)
        # 역순으로 반복
        for j in range(N - 1, 0, -1):
            # j 가 마지막 열 일때 1을 붙이기
            if j == (N - 1):
                pascal.append(1)
            # 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
						# 역순이기 때문에 j - 1로 구성
            else:
                pascal[j] = pascal[j] + pascal[j - 1]
        print(*pascal)

    print(f'#{tc}')
    recur_func(N)