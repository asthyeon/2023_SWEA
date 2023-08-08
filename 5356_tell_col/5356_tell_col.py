import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 5줄의 문자열
    strings = [list(map(str, input().split())) for _ in range(5)]

    # 빈 어레이 만들기
    arr = [[''] * 15 for _ in range(5)]

    # 5줄의 문자열을 각 어레이에 설정하기
    # 가로 줄의 길이가 다 다르므로 따로 범위를 설정하기
    for i in range(5):
        for j in range(len(strings[i][0])):
            arr[i][j] = strings[i][0][j]

    # 세로로 읽기
    # 세로로 읽는 전체 글자를 더하기 위한 변수
    result = ''
    for y in range(15):
        for x in range(5):
            if arr[x][y] != '':
                result += arr[x][y]

<<<<<<< HEAD
    print(f'#{tc} {result}')
=======
    print(f'#{tc} {result}')
>>>>>>> ec111fdab7cfd182b608b5e2cc2ec6fe59c8bb7d
