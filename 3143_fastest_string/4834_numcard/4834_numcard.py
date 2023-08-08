import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = int(input())

    # 각 자리 수에 해당되는 인덱스를 받을 리스트 만들기
    c = [0] * 10
    # 각 자리 수를 인덱스에 넣기
    for i in range(N):
        c[arr % 10] += 1
        arr //= 10

    # 비교할 초기 값
    num = c[0]
    # 리스트 c 의 길이만큼 반복
    for i in range(len(c)):
        # num 보다 c[i]가 크다면
        if num <= c[i]:
            # 가장 많은 카드 수로 교체
            num = c[i]
            # i 앞의 모든 인덱스 0으로 만들기
            for j in range(i):
                c[j] = 0
            # i 뒤의 모든 인덱스 0으로 만들기
            for k in range(i, len(c), -1):
                c[k] = 0
            # c[i]는 num 값으로 만들어서 인덱스 번호 출력하기
            c[i] = num
    # 출력
    print(f'#{tc} {c.index(num)} {num}')
