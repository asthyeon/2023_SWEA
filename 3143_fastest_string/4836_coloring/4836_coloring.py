import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 색칠할 빈 영역 생성
    color_list = [[0] * 10 for _ in range(10)]
    # 색칠할 영역 받기
    for _ in range(N):
        A, B, C, D, E = (map(int, input().split()))
        # 색칠할 영역 만들기
        # color_list[A, B] 부터 시작
        for i in range(A, C + 1):
            for j in range(B, D + 1):
                for di, dj in [[0, 1], [1, 0]]:
                    ni = i + di
                    nj = i + dj
                    # 벽 세우기
                    if A <= ni < (C + 1) or B <= dj < (D + 1):
                        # 빨간색일 때
                        if E == 1:
                            # 빨간색이 없다면 색칠하기
                            if color_list[i][j] == 0 or color_list[i][j] == 2:
                                color_list[i][j] += 1
                            # 빨간색이 색칠해져 있다면 넘기기
                            else:
                                continue
                        # 파란색일 때
                        else:
                            # 파란색이 없다면 색칠하기
                            if color_list[i][j] == 0 or color_list[i][j] == 1:
                                color_list[i][j] += 2
                            # 파란색이 색칠해져 있다면 넘기기
                            else:
                                continue

    # 보라색이 칠해져 있는 공간 수
    purple = 0
    # 보라색으로 칠해져 있는 공간 찾기
    for color in color_list:
        for i in color:
            if i == 3:
                purple += 1
    
    # 출력
    print(f'#{tc} {purple}')