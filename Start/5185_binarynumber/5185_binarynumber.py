import sys
sys.stdin = open("sample_input.txt")

"""
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
1. 2진수의 앞자리 0도 반드시 출력하기
"""

T = int(input())
for tc in range(1, T + 1):
    # 자리 수 N, N자리 16진수 number
    N, numbers = input().split()

    # 테스트케이스 구분
    print(f'#{tc} ', end='')
    # 각 자리 수를 변환하기
    for number in numbers:
        if number.isdigit():
            # 이진 수로 변환하기
            bi = ['0', '0', '0', '0']
            for _ in range(int(number)):
                if bi[3] == '0':
                    bi[3] = '1'
                else:
                    bi[3] = '0'
                    if bi[2] == '0':
                        bi[2] = '1'
                    else:
                        bi[2] = '0'
                        if bi[1] == '0':
                            bi[1] = '1'
                            bi[2] = '0'
                        else:
                            bi[1] = '0'
                            if bi[0] == '0':
                                bi[0] = '1'
                                bi[1] = '0'
            print(*bi, end='', sep='')
        # 문자라면
        else:
            # 숫자로 변환
            if number == 'A':
                number = 10
            elif number == 'B':
                number = 11
            elif number == 'C':
                number = 12
            elif number == 'D':
                number = 13
            elif number == 'E':
                number = 14
            else:
                number = 15
            # 이진수로 변환하기
            bi = ['0', '0', '0', '0']
            for _ in range(int(number)):
                if bi[3] == '0':
                    bi[3] = '1'
                else:
                    bi[3] = '0'
                    if bi[2] == '0':
                        bi[2] = '1'
                    else:
                        bi[2] = '0'
                        if bi[1] == '0':
                            bi[1] = '1'
                            bi[2] = '0'
                        else:
                            bi[1] = '0'
                            if bi[0] == '0':
                                bi[0] = '1'
                                bi[1] = '0'
            print(*bi, end='', sep='')
    print()