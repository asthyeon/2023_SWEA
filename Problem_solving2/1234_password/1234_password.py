import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    str_len, string = input().split()

    # 문자열의 길이를 정수화
    N = int(str_len)

    # stack 형성
    stack = []
    top = -1

    # string 의 글자만큼 반복
    for latter in string:
        # stack 에 글자 push
        stack.append(latter)
        top += 1

        # top 이 0 보다 클 때
        if top > 0:
            # stack 의 문자열이 연속으로 같다면 제거
            if stack[top] == stack[top - 1]:
                stack.pop()
                stack.pop()
                top -= 2

    print(f'#{tc} ', *stack, sep = '')

