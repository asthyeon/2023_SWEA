import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 검사할 코드
    check = input()
    # 스택 리스트
    stack = []
    # 정답 조건
    ans = 1
    
    # 검사할 코드의 한 글자씩 반복
    for i in check:
        # 만일 왼쪽 소괄호일 때
        if i == '(':
            # 스택에 추가
            stack.append(i)
        # 왼쪽 중괄호일 때
        elif i == '{':
            # 스택에 추가
            stack.append(i)
        # 오른쪽 소괄호일 때
        elif i == ')':
            # 스택이 비어있지 않다면
            if len(stack) != 0:
                # 스택의 마지막이 짝이 맞는다면
                if stack[-1] == '(':
                    # 스택의 마지막 제거
                    stack.pop()
                    continue
                # 짝이 맞지 않는다면
                else:
                    # 스택에 추가
                    stack.append(i)
            # 스택이 비어있다면 스택에 추가
            else:
                stack.append(i)
        # 오른쪽 중괄호일 때
        elif i == '}':
            # 스택이 비어있지 않다면
            if len(stack) != 0:
                # 스택의 마지막이 짝이 맞는다면
                if stack[-1] == '{':
                    # 스택의 마지막 제거
                    stack.pop()
                # 짝이 맞지 않는다면
                else:
                    # 스택에 추가
                    stack.append(i)
            # 스택이 비어있다면 스택에 추가
            else:
                stack.append(i)
    
    # 스택의 길이가 0이 아니라면
    if len(stack) != 0:
        # 오답으로 바꾸기
        ans = 0

    print(f'#{tc} {ans}')

