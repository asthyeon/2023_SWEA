import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # babygin 확인할 6자리 수
    arr = int(input())
    # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
    # run 을 계산하려면 9, 10, 11 번째 인덱스를 계산해야 하므로 12를 곱함
    c = [0] * 12
    # 뒤에서부터 각 자리 수를 추출하여 c에 해당 숫자에 해당하는 인덱스에 카운트 넣기
    for i in range(6):
        c[arr % 10] += 1
        arr //= 10

    # 반복문을 이용하여 triplet 과 run 조사
    i = 0
    tri_check = 0
    run_check = 0
    while i < 10:
        # triplet 조사 후 데이터 삭제
        if c[i] >= 3:
            c[i] -= 3
            tri_check += 1
            continue
        # run 조사 후 데이터 삭제
        if c[i] >= 1 and\
                c[i + 1] >= 1 and\
                c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run_check += 1
            continue
        i += 1

    if tri_check + run_check == 2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')