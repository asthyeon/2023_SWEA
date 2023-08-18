import sys
sys.stdin = open('sample_input.txt')

'''
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자 출력하기
1. N 개의 숫자로 이루어진 수열로 주어짐
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 자연수 N 개의 수
    numbers = list(map(int, input().split()))
    
    # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M 번하기
    for i in range(M):
        numbers.append(numbers.pop(0))

    print(f'#{tc} {numbers[0]}')
