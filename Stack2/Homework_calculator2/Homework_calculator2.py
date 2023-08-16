import sys
sys.stdin = open('input.txt')

'''
# 계산식을 후위 표기식으로 바꾸어 계산
'''

# 우선순위 저장하기
# 스택 외부 우선순위
icp = {'*': 2, '+': 1}
# 스택 내부 우선순위
isp = {'*': 2, '+': 1}

for tc in range(1, 11):
    # 숫자의 길이
    N = int(input())

    # 문자열 입력받기
    string = input()

    # stack 형성
    stack = []

    # 후위 표기식으로 나타내기
    rear = ''
    
    # 후위 표기식 변환
    for s in string:
        # 피연산자라면
        if s not in '*+':
            rear += s
        # 연산자라면
        else:
            # 스택이 비어있거나 해당 연산자의 우선순위가 스택 내의 연산자보다 우선순위가 높다면
            if len(stack) == 0 or isp[stack[-1]] < icp[s]:
                # push
                stack.append(s)
            # 우선순위가 스택 내의 연산자가 더 높거나 같다면
            elif isp[stack[-1]] >= icp[s]:
                # 스택이 비거나 더 높은 우선순위의 연산자를 만날 때까지 pop()하여 rear 에 넣기 반복
                while len(stack) > 0 and isp[stack[-1]] >= icp[s]:
                    rear += stack.pop()
                # 마지막에 push
                stack.append(s)
    # stack 에 남아있는 연산자 넣어주기
    while len(stack) > 0:
        rear += stack.pop()

    # 후위 표기식 계산
    for i in rear:
        # 피연산자라면
        if i not in '*+':
            stack.append(int(i))
        # 연산자라면
        else:
            # 연산을 받을 피연산자 변수를 구성
            op2 = stack.pop()
            op1 = stack.pop()
            # '+' 라면
            if i == '+':
                stack.append(op1 + op2)
            # '*' 라면
            elif i == '*':
                stack.append(op1 * op2)

    print(f'#{tc} {stack[0]}')
