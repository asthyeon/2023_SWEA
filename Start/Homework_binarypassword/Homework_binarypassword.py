import sys
sys.stdin = open("input.txt")

"""
# 2차원 배열을 입력받아 올바른 암호코드인지 판별하기
1. 암호코드는 8개의 숫자
2. 올바른 암호코드 : (홀수 자리 합 x 3) + (짝수 자리의 합) 이 10의 배수
3. 암호코드 처음은 0, 암호코드 끝은 1
"""

T = int(input())
for tc in range(1, 2):
    # 세로 크기 N, 가로 크기 M
    N, M = map(int, input().split())

    # 배열 형성
    arr = [list(map(int, input())) for _ in range(N)]

    # 암호 코드 1줄
    password = []
    # 암호 코드 찾기
    for x in range(N):
        for y in range(M - 48):
            # 룰을 만족하는 첫 번째 부분을 찾는다면
            if arr[x][y] == 0 and arr[x][y + 6] == 1:
                # 임시 값
                tmp = []
                # 한줄씩 넣기
                for j in range(y, M - 6, 6):
                    tmp.append(arr[x][j:j + 7])
                if len(tmp) == 8:
                    password.extend(tmp)
                    break

    print(password)






