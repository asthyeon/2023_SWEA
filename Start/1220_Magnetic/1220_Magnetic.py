import sys
sys.stdin = open("input.txt")

"""
# 테이블 위에 남아있는 교착 상태의 개수 구하기
1. 푸른 자성체: N 극에 이끌림
2. 붉은 자성체: S 극에 이끌림
3. 교착 상태: 자성체끼리 충돌(반대에 1개라도 있으면 교착상태)
4. 3개 이상이 교착 상태여도 1개의 교착으로 봄
5. 좌우 인접은 다른 교착
6. 한 열에 2개 이상의 교착도 가능
7. 겹쳐있어도 각각 교착이면 따로 셈
* 1: N극 성질 -> S극에 끌림
* 2: S극 성질 -> N극에 끌림
"""

for tc in range(1, 11):
    # 테이블 한 변의 길이
    N = int(input())
    # 테이블 형성
    table = [list(map(int, input().split())) for _ in range(N)]

    # 스택 생성
    stack = []
    top = -1
    # 카운트
    cnt = 0

    # 아래로 순회하기 때문에 N극 성질부터 판단
    for y in range(N):
        for x in range(N):
            # 1 일 때 스택에 집어넣기
            if table[x][y] == 1:
                stack.append(table[x][y])
                top += 1
            # 2 일 때 스택이 있다면 수를 세고 스택 비우기
            elif table[x][y] == 2:
                if stack:
                    cnt += 1
                    stack.clear()
                    top = -1
        # 스택 초기화(남은 것들이 다음 열로 넘어가지 않게하기 위함)
        stack = []
        top = -1

    print(f'#{tc} {cnt}')
