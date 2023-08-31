import sys
sys.stdin = open("input.txt")

"""
# 가장 긴 회문의 길이 구하기
1. 가로 세로 모두 보기
2. A, B, C 글자만 들어감
@ 풀이
1. 첫 글자와 같은 가장 마지막 글자를 찾고 안에 글자들이 같은지 보기
2. 다르면 다음 마지막 글자 찾고 반복
"""

for tc in range(1, 11):
    T = int(input())
    # 글자판 받기
    arr = [input() for _ in range(100)]

    # 회문 길이 최댓값(1글자도 회문)
    result = 1

    # 가로 회문 찾기
    for x in range(100):
        for y in range(100):
            # 가장 마지막 글자가 같다면
            for i in range(99, y, -1):
                if arr[x][y] == arr[x][i]:
                    string = ''
                    # 그 글자까지 모든 글자 확인하기
                    for j in range(i - y + 1):
                        if arr[x][y + j] == arr[x][i - j]:
                            string += arr[x][y + j]
                        else:
                            string = ''
                            break
                    if len(string) > 0:
                        if result < len(string):
                            result = len(string)

    # 세로 회문 찾기
    for y in range(100):
        for x in range(100):
            # 가장 마지막 글자가 같다면
            for k in range(99, x, -1):
                if arr[x][y] == arr[k][y]:
                    string2 = ''
                    # 그 글자까지 모든 글자 확인하기
                    for m in range(k - x + 1):
                        if arr[x + m][y] == arr[k - m][y]:
                            string2 += arr[x + m][y]
                        else:
                            string2 = ''
                            break
                    if len(string2) > 0:
                        if result < len(string2):
                            result = len(string2)

    print(f'#{T} {result}')
