import sys
sys.stdin = open('sample_input.txt')

'''
# 잘려진 쇠막대기 조각의 총 개수를 구하기
1. 레이저와 막대가 증가하는 것을 구분하는 것이 관건
'''

T = int(input())
for tc in range(1, T + 1):
    word = input()

    # 막대 수
    rod = 0

    # 잘려진 조각의 총 개수
    cnt = 0

    for i in range(len(word)):
        # '(' 로 시작하면 일단 막대 하나 추가
        if word[i] == '(':
            rod += 1
        # word 의 i 번째가 ')' 일 때
        else:
            # 레이저로 판정
            if word[i - 1] == '(':
                # 직전의 '(' 를 막대로 보지 않고
                rod -= 1
                # 이제 까지의 막대 수를 잘라서 넣기
                cnt += rod
            # 막대를 닫는 것일 때
            else:
                # 갯수 늘리기
                cnt += 1
                # 막대 수 줄이기
                rod -= 1

    print(f'#{tc} {cnt}')
