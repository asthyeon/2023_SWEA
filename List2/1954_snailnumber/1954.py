import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 빈 어레이 형성
    arr = [[0] * N for _ in range(N)]

    # 숫자를 담을 변수 형성
    count = 1

    # 초기 시작 좌표
    x = 0
    y = 0
    # 초기 값 설정
    arr[x][y] = count

    # 달팽이 만들기 count 가 N의 제곱이 되면 정지
    while count < (N ** 2):

        # 오른쪽으로 막힐 때까지 이동
        # y 값 범위 지정
        while y < (N - 1):
            # 오른쪽으로 1 칸 이동한 값이 0 일때,
            if arr[x][y + 1] == 0:
                y += 1
                count += 1
                arr[x][y] = count
            # 이동한 값이 0이 아닐 때 반복문 종료
            else:
                break


        # 아래로 막힐 때까지 이동
        # x 값 범위 지정
        while x < (N - 1):
            # 아래로 1 칸 이동한 값이 0 일때,
            if arr[x + 1][y] == 0:
                x += 1
                count += 1
                arr[x][y] = count
            else:
                break

        # 왼쪽으로 막힐 때까지 이동
        # y 값 범위 지정
        while y > 0:
            # 왼쪽으로 1칸 이동한 값이 0 일 때,
            if arr[x][y - 1] == 0:
                y -= 1
                count += 1
                arr[x][y] = count
            else:
                break

        # 위로 막힐 때까지 이동
        # x 값 범위 지정
        while x > 0:
            if arr[x - 1][y] == 0:
                x -= 1
                count += 1
                arr[x][y] = count
            else:
                break
    
    # 출력
    print(f'#{tc}')
    # 리스트를 달팽이 모양대로 공백 포함하여 출력
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()