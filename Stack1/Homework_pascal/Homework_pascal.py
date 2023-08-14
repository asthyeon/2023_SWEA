import sys
sys.stdin = open('input.txt')

'''
# 파스칼의 삼각형이란
1. 첫 번째 줄은 항상 숫자 1이다
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
'''

T = int(input())
for tc in range(1, T + 1):
    # 크기가 N 인 파스칼의 삼각형
    N = int(input())
    # 스택 생성
    stack =[]
    for i in range(1, N + 1):
        stack.append([0] * i)
    
    # N 까지 x 줄 반복
    for x in range(N):
        # 처음과 마지막은 항상 숫자 1
        stack[x][0] = 1
        stack[x][-1] = 1
        # x 줄에 (x + 1) 개의 각 요소에 대하여
        for y in range(x + 1):
            # 만일 x 가 첫 째줄이 아니고
            if x > 0:
                # y 가 맨 처음과 끝이 아니라면
                if 0 < y < x:
                    # 각 숫자들은 자신의 왼쪽 위와 오른쪽 위의 숫자의 합
                    stack[x][y] = stack[x - 1][y - 1] + stack[x - 1][y]

    # 삼각형으로 출력
    print(f'#{tc}')
    for j in range(N):
        # 리스트를 언패킹해서 출력
        print(*stack[j])