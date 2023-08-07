import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 테스트 케이스 번호와 길이
    tc_num, tc_length = input().split()
    # 테스트 케이스 입력받기
    arr = list(input().split())

    # 빈 딕셔너리 만들기
    arr_dict = {}
    # 빈 딕셔너리에 각 숫자를 더하기
    for i in arr:
        if i in arr_dict:
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1

    # 각 숫자를 순서대로 출력하기
    print(tc_num)
    print('ZRO ' * arr_dict['ZRO'], end = '')
    print('ONE ' * arr_dict['ONE'], end = '')
    print('TWO ' * arr_dict['TWO'], end = '')
    print('THR ' * arr_dict['THR'], end = '')
    print('FOR ' * arr_dict['FOR'], end = '')
    print('FIV ' * arr_dict['FIV'], end = '')
    print('SIX ' * arr_dict['SIX'], end = '')
    print('SVN ' * arr_dict['SVN'], end = '')
    print('EGT ' * arr_dict['EGT'], end = '')
    print('NIN ' * arr_dict['NIN'], end = '')