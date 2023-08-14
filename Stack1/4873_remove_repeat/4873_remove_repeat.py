import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 문자열 입력
    string = input()

    # 스택 형성
    stack = []
    # top 형성
    top = -1

    # 스택 쌓기
    for i in string:
        # 문자열의 각 글자를 스택에 넣어주기
        stack.append(i)
        # 문자열이 하나 추가될 때마다 top 증가
        top += 1
        # top 이 0보다 클 때(0 일 때는 top - 1 이 음수가 되므로)
        if top > 0:
            # top 번째 글자가 바로 뒤의 글자와 같다면
            if stack[top] == stack[top - 1]:
                # 두 글자를 제거
                stack.pop()
                stack.pop()
                # 제거된 글자 만큼 top 빼주기
                top -= 2

    print(f'#{tc} {len(stack)}')