import sys
sys.stdin = open('sample_input.txt')

"""
# 세로로 읽은 순서대로 출력
1. 공백이 포함되어있으면 그 다음 글자를 계속 읽음
2. 세로로 읽은 순서대로 공백 없이 출력
"""

T = int(input())
for tc in range(1, T + 1):
    sentences = [input() for _ in range(5)]

    # 가장 긴 글자 수 찾기
    max_len = 0
    for i in range(5):
        if max_len < len(sentences[i]):
            max_len = len(sentences[i])

    # 가장 긴 글자 수 만큼 글자 붙여주기
    for j in range(5):
        while True:
            if len(sentences[j]) < max_len:
                sentences[j] += ' '
            else:
                break

    # 세로로 읽기
    print(f'#{tc} ', end='')
    for y in range(max_len):
        for x in range(5):
            print(sentences[x][y].strip(), end='')
    print()



