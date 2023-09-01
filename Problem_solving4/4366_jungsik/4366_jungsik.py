import sys
sys.stdin = open('input.txt')

"""
# 송금액을 추측하는 프로그램
1. 2진수와 3진수 각각의 수에서 단 한자리만을 잘못 기억하고 있다
@ 받은 수의 첫째 자리를 제외한 모든 자릿수를 바꿔서 나올 수 있는 모든 수를 만들어보기
(1) 첫번째 자리 수가 0이 될 수 있음
"""

T = int(input())
for tc in range(1, T + 1):
    # 2진수
    bi_num = list(map(int, input()))
    # 3진수
    tr_num = list(map(int, input()))

    # 가능한 2진수 리스트
    bi_list = []
    # 가능한 3진수 리스트
    tr_list = []

    # 가능한 2진수 리스트 구하기
    for i in range(len(bi_num)):
        # 자릿값 바꾸기
        if bi_num[i] == 0:
            bi_num[i] = 1
        else:
            bi_num[i] = 0
        # 숫자 만들고 리스트에 넣기
        change_bi = ''
        for j in bi_num:
            change_bi += str(j)
        bi_list.append(int(change_bi))
        # 자릿값 원상복귀
        if bi_num[i] == 0:
            bi_num[i] = 1
        else:
            bi_num[i] = 0

    # 가능한 3진수 리스트 구하기
    for k in range(len(tr_num)):
        if tr_num[k] == 2:
            tr_num[k] = 1
            change_tr = ''
            for l in tr_num:
                change_tr += str(l)
            tr_list.append(int(change_tr))
            tr_num[k] = 0
            change_tr = ''
            for l in tr_num:
                change_tr += str(l)
            tr_list.append(int(change_tr))
            tr_num[k] = 2
        elif tr_num[k] == 1:
            tr_num[k] = 2
            change_tr = ''
            for l in tr_num:
                change_tr += str(l)
            tr_list.append(int(change_tr))
            tr_num[k] = 0
            change_tr = ''
            for l in tr_num:
                change_tr += str(l)
            tr_list.append(int(change_tr))
            tr_num[k] = 1
        else:
            tr_num[k] = 2
            change_tr = ''
            for l in tr_num:
                change_tr += str(l)
            tr_list.append(int(change_tr))
            tr_num[k] = 1
            change_tr = ''
            for l in tr_num:
                change_tr += str(l)
            tr_list.append(int(change_tr))
            tr_num[k] = 0

    # 2진수를 10진수로 변환
    te_list = []
    for m in bi_list:
        te_list.append(int(f'{m}', 2))

    # 3진수를 10진수로 변환하고 10진수 리스트에 있으면 바로 출력
    for n in tr_list:
        if int(f'{n}', 3) in te_list:
            print(f"#{tc} {int(f'{n}', 3)}")
            break



