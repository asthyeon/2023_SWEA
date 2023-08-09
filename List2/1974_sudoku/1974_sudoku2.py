import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 스도쿠 퍼즐 생성
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 정답 맞추기
    answer = 1

    # 행 우선 순회
    for x1 in range(9):
        # set()로 중복 제거하기
        arr_set = set()
        for y1 in range(9):
            # set() 에 숫자 넣기
            arr_set.add(arr[x1][y1])
        # set 의 길이가 9가 안되면 오답
        if len(arr_set) < 9:
            answer = 0

    # 열 우선 순회
    for y2 in range(9):
        # set()로 중복 제거하기
        arr_set = set()
        for x2 in range(9):
            arr_set.add(arr[x2][y2])
        if len(arr_set) < 9:
            answer = 0

    # 3 x 3 순회 (3칸씩 건너 뛰기)
    for x3 in range(0, 7, 3):
        for y3 in range(0, 7, 3):
            arr_set = set()
            for xx3 in range(x3, x3 + 3):
                for yy3 in range(y3, y3 + 3):
                    arr_set.add(arr[xx3][yy3])
            if len(arr_set) < 9:
                answer = 0

    print(f'#{tc} {answer}')