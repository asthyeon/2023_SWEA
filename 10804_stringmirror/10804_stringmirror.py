import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()

    # 거울에 비친 글자를 넣을 문자열
    result = ''

    # 거울에 비치기
    # 먼저 글자를 뒤집기
    for i in word[::-1]:
        # 각 글자들을 거울에 비쳤을 때 나오는 글자로 치환
        if i == 'b':
            result += 'd'
        elif i == 'd':
            result += 'b'
        elif i == 'p':
            result += 'q'
        else:
            result += 'p'

    print(f'#{tc} {result}')