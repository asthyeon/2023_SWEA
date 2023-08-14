import sys
sys.stdin = open('sample_input.txt')

'''
# Forth 연산(후위 표기법)
1. 숫자는 스택에 넣는다
2. 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣기
3. '.'은 스택에서 숫자를 꺼내 출력
4. 형식이 잘못되어 연산이 불가능한 경우 'error' 출력
'''

T = int(input())
for tc in range(1, T + 1):
    # 코드 입력
    arr = input().split()

    # stack 형성
    stack = []

    for i in range(len(arr)):
        # 초항일 때 숫자가 아니라면 error 출력
        if i == 0:
            if arr[i].isdigit():
                stack.append(int(arr[i]))
            else:
                print('error')
                break
        # 초항이 아닐 때
        else:
            # 숫자일 때 스택에 넣기
            if arr[i].isdigit():
                stack.append(int(arr[i]))
            # 더하기일 때 더하기 변수에 넣고 pop 한 후 다시 push
            if arr[i] == '+':
                if len(stack) > 1:
                    plus = 0
                    plus += stack.pop()
                    plus += stack.pop()
                    stack.append(plus)
                else:
                    print(f'#{tc} error')
                    break
            # 빼기일 때 변수 2개로 나누고 뺀 값을 push
            if arr[i] == '-':
                if len(stack) > 1:
                    minus1 = stack.pop()
                    minus2 = stack.pop()
                    minus = minus2 - minus1
                    stack.append(minus)
                else:
                    print(f'#{tc} error')
                    break
            # 곱하기일 때 곱하기 변수에 곱해놓고 pop 후 push
            if arr[i] == '*':
                if len(stack) > 1:
                    multiple = 1
                    multiple *= stack.pop()
                    multiple *= stack.pop()
                    stack.append(multiple)
                else:
                    print(f'#{tc} error')
                    break
            # 나누기일 때 변수 2개로 나누고 나눈 값을 push
            if arr[i] == '/':
                if len(stack) > 1:
                    divide1 = stack.pop()
                    divide2 = stack.pop()
                    divide = int(divide2 / divide1)
                    stack.append(divide)
                else:
                    print(f'#{tc} error')
                    break


            # 온점일 때 남은 것 출력
            if arr[i] == '.':
                if len(stack) > 1:
                    print(f'#{tc} error')
                else:
                    print(f'#{tc} {stack[0]}')
