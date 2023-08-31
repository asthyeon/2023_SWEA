import sys
sys.stdin = open('sample_input.txt')

"""
# 정상적인 암호코드들을 판별한 뒤 암호코드들에 적혀 있는 숫자들의 총합 출력
1. 암호코드의 규칙
- 앞 7자리: 고유 번호, 마지막: 검증 코드
- 검증 코드 계산: (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드 % 10 = 0 성립
2. 세부 규칙
- 암호코드들이 붙어있는 경우 X
- 암호 코드의 가로 길이가 길어질 경우 숫자 하나가 차지하는 길이는 7의 배수가 됨
3. 16진수로 구성된 배열을 2진수로 변환하여 그 안에 포함되어 있는 암호코드 정보를 확인하기
"""


# 암호코드 스캔 함수
def scan(password, answer, normal):
    global total
    # 해독한 암호를 넣을 숫자 리스트
    numbers = []
    # 암호 해독하기
    encode = ''
    # 역순 조사를 위한 인덱스 값
    front = len(password) - 1
    # 역순으로 조사하기
    while front >= 0:
        if len(encode) == 0:
            if password[front] == '1':
                encode = password[front] + encode
                front -= 1
            else:
                front -= 1
        else:
            encode = password[front] + encode
            front -= 1
        # 7의 배수마다 암호 체크
        if len(encode) % 7 == 0:
            # 암호가 맞다면 리스트에 넣기
            if encode in answer:
                numbers.insert(0, answer[encode])
                encode = ''
        # 8 자리가 된다면 정상 암호인지 체크하기
        if len(numbers) == 8:
            num1 = (numbers[0] + numbers[2] + numbers[4] + numbers[6]) * 3
            num2 = numbers[1] + numbers[3] + numbers[5] + numbers[7]
            # 10 의 배수라면
            if (num1 + num2) % 10 == 0:
                # 8자리 자리수를 str로 교체
                number = ''
                for n in range(8):
                    number += str(numbers[n])
                normal.append(number)
                numbers = []
            else:
                numbers = []
    # 순회를 다 돌아도 암호 코드 자릿수가 부족할 때 앞에 0 추가하기
    if numbers:
        while encode not in answer:
            encode = '0' + encode
        # 마지막 앞자리 붙이기
        numbers.insert(0, answer[encode])
    # 암호 코드라면
    if len(numbers) == 8:
        num1 = (numbers[0] + numbers[2] + numbers[4] + numbers[6]) * 3
        num2 = numbers[1] + numbers[3] + numbers[5] + numbers[7]
        # 10 의 배수라면
        if (num1 + num2) % 10 == 0:
            # 8자리 자리수를 str로 교체
            number = ''
            for n in range(8):
                number += str(numbers[n])
            normal.append(number)


# 코드 번호
answer = dict()
# 모든 경우의 수 넣기(500 * 4 / 56)
for i in range(1, 36):
    zer = '0' * 3 * i + '1' * 2 * i + '0' * 1 * i + '1' * 1 * i
    answer[zer] = 0
    one = '0' * 2 * i + '1' * 2 * i + '0' * 2 * i + '1' * 1 * i
    answer[one] = 1
    two = '0' * 2 * i + '1' * 1 * i + '0' * 2 * i + '1' * 2 * i
    answer[two] = 2
    thr = '0' * 1 * i + '1' * 4 * i + '0' * 1 * i + '1' * 1 * i
    answer[thr] = 3
    fou = '0' * 1 * i + '1' * 1 * i + '0' * 3 * i + '1' * 2 * i
    answer[fou] = 4
    fiv = '0' * 1 * i + '1' * 2 * i + '0' * 3 * i + '1' * 1 * i
    answer[fiv] = 5
    six = '0' * 1 * i + '1' * 1 * i + '0' * 1 * i + '1' * 4 * i
    answer[six] = 6
    sev = '0' * 1 * i + '1' * 3 * i + '0' * 1 * i + '1' * 2 * i
    answer[sev] = 7
    eig = '0' * 1 * i + '1' * 2 * i + '0' * 1 * i + '1' * 3 * i
    answer[eig] = 8
    nin = '0' * 3 * i + '1' * 1 * i + '0' * 1 * i + '1' * 2 * i
    answer[nin] = 9

T = int(input())
for tc in range(1, T + 1):
    # 세로 크기 N, 가로 크기 M
    N, M = map(int, input().split())

    # 암호 받기
    arr = [input().strip() for _ in range(N)]

    # 정상암호들
    normal = []

    # 숫자들의 총합
    total = 0

    # 중복 제거
    arr = list(set(arr))
    # 암호가 없는 부분 제거
    arr.remove('0' * M)
    arr.sort()

    # 16진수를 2진수로 변환하기
    for x in range(len(arr)):
        # 2진수로 변환될 암호
        password = ''
        for y in range(len(arr[x])):
            # 숫자라면
            if arr[x][y].isdigit():
                password += format(int(arr[x][y]), '04b')
            # 알파벳이라면
            else:
                if arr[x][y] == 'A':
                    password += format(10, '04b')
                elif arr[x][y] == 'B':
                    password += format(11, '04b')
                elif arr[x][y] == 'C':
                    password += format(12, '04b')
                elif arr[x][y] == 'D':
                    password += format(13, '04b')
                elif arr[x][y] == 'E':
                    password += format(14, '04b')
                else:
                    password += format(15, '04b')

        # 뒷부분 0 제거
        password = password.lstrip('0')

        # 암호코드 스캔
        scan(password, answer, normal)

    # 중복 암호 제거
    normal = list(set(normal))

    # 조건을 만족하는 모든 수를 더하기
    for m in range(len(normal)):
        for n in range(8):
            total += int(normal[m][n])

    # 출력
    print(f'#{tc} {total}')