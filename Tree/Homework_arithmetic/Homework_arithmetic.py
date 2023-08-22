import sys
sys.stdin = open('input.txt')

"""
# 계산한 결과 출력하기
1. 임의의 정점에 연산자 존재시, 왼쪽 서브 트리와 오른쪽 서브트리의 결과에 해당 연산자 적용
2. 루트 정점의 번호는 항상 1
3. 후위순회로 계산하기
"""


# 후위순회
def postorder(n, stack):
    global top
    if n:
        # 왼쪽 서브트리
        postorder(ch1[n], stack)
        # 오른쪽 서브트리
        postorder(ch2[n], stack)
        # 값이 피연산자라면 스택에 넣기
        if keys[n].isdigit():
            stack.append(int(keys[n]))
            top += 1
        # 값이 연산자라면 스택에 넣고
        else:
            stack.append(keys[n])
            top += 1
            # 이전 연산자 2개와 연산자로 계산하기
            if stack[top] == '+':
                number = stack[top - 2] + stack[top -1]
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(number)
                top -= 2
            elif stack[top] == '-':
                number = stack[top - 2] - stack[top - 1]
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(number)
                top -= 2
            elif stack[top] == '*':
                number = stack[top - 2] * stack[top - 1]
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(number)
                top -= 2
            elif stack[top] == '/':
                number = stack[top - 2] // stack[top -1]
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(number)
                top -= 2


for tc in range(1, 11):
    # 정점의 개수
    N = int(input())

    # 부모 노드를 인덱스 번호로 저장
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    # 자식 노드를 인덱스 번호로 저장
    par = [0] * (N + 1)
    # 각 정점의 값
    keys = [0] * (N + 1)

    for _ in range(N):
        arr = list(input().split())

        # 정수라면
        if arr[1].isdigit():
            keys[int(arr[0])] = arr[1]
        # 정수가 아니라면
        else:
            # 자식 연결
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
            # 정점의 값 부여
            keys[int(arr[0])] = arr[1]

    # 스택 형성
    stack = []
    top = -1

    postorder(1, stack)

    print(f'#{tc} {stack[0]}')