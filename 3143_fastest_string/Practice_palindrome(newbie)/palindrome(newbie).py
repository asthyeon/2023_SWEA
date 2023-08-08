import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 단어 입력
    word = input()
    # 만약 단어가 거꾸로 돌린 단어와 같다면
    if word == word[::-1]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')