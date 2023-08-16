import sys
sys.stdin = open('input.txt')

'''
# 계산식을 후위 표기식으로 바꾸어 계산
'''

for tc in range(1, 11):
    # 문자열 계산식의 길이
    N = int(input())

    # 문자열 받기
    arr = input()

    # stack 형성
    stack = []

    # 합계
    arr_sum = 0

    for i in range(N):
        # 초항이라면 더하기
        if i == 0:
            arr_sum += int(arr[i])
        # 연산자라면
        if arr[i].isdigit() is False:
            stack.append(arr[i])
        # 숫자라면
        else:
            # 스택에 연산자가 있다면
            if stack:
                # 연산자가 더하기라면
                if stack.pop() == '+':
                    arr_sum += int(arr[i])

    print(f'#{tc} {arr_sum}')


