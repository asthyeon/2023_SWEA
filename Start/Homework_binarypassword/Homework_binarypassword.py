import sys
sys.stdin = open("input.txt")

"""
# 2차원 배열을 입력받아 올바른 암호코드인지 판별하기
1. 암호코드는 8개의 숫자
2. 올바른 암호코드 : (홀수 자리 합 x 3) + (짝수 자리의 합) 이 10의 배수
3. 암호코드 처음은 0, 암호코드 끝은 1
"""

T = int(input())
for tc in range(1, T + 1):
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
                for j in range(y, M - 6, 7):
                    # 다시 조건을 만족한다면
                    if arr[x][j] == 0 and arr[x][j + 6] == 1:
                        tmp.append(arr[x][j:j + 7])
                # 임시 값에 조건을 만족한 코드가 8개라면 패스워드에 합치기
                if len(tmp) == 8:
                    password.extend(tmp)
                    break
            # 패스워드가 8개라면 반복문 종료
            if len(password) == 8:
                break
        # 패스워드가 8개라면 반복문 종료
        if len(password) == 8:
            break

    # 암호 해독하기
    for i in range(8):
        if password[i] == [0, 0, 0, 1, 1, 0, 1]:
            password[i] = 0
        elif password[i] == [0, 0, 1, 1, 0, 0, 1]:
            password[i] = 1
        elif password[i] == [0, 0, 1, 0, 0, 1, 1]:
            password[i] = 2
        elif password[i] == [0, 1, 1, 1, 1, 0, 1]:
            password[i] = 3
        elif password[i] == [0, 1, 0, 0, 0, 1, 1]:
            password[i] = 4
        elif password[i] == [0, 1, 1, 0, 0, 0, 1]:
            password[i] = 5
        elif password[i] == [0, 1, 0, 1, 1, 1, 1]:
            password[i] = 6
        elif password[i] == [0, 1, 1, 1, 0, 1, 1]:
            password[i] = 7
        elif password[i] == [0, 1, 1, 0, 1, 1, 1]:
            password[i] = 8
        else:
            password[i] = 9


    # 올바른지 판단하기
    odd = 0
    even = 0
    for k in range(8):
        # 홀수라면(인덱스 값은 짝수)
        if k % 2 == 0:
            odd += password[k]
        # 짝수라면(인덱스 값은 홀수)
        else:
            even += password[k]

    # 전체 합
    total = odd + even
    # 비교를 위한 전체 합
    result = (odd * 3) + even

    # 출력조건
    if result % 10 == 0:
        print(f'#{tc} {total}')
    else:
        print(f'#{tc} {0}')
