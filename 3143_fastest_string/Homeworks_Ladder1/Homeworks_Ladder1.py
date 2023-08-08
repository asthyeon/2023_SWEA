import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 테스트케이스 번호
    T = int(input())
    # 사다리 형성
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지에서부터 출발
    # 도착지 좌표
    x = 99
    y = 0
    # 도착지 y좌표 구하기
    for i in range(100):
        if arr[x][i] == 2:
            y = i
    
    # x 가 0 이 될 때 멈추기
    while True:
        # 반복문 종료 조건
        if x == 0:
            break

        # 위로 이동
        if arr[x - 1][y] == 1:
            x -= 1
        
        # 좌로 이동
        # 맨 왼쪽에 도달했을 때를 고려하여 0보다 크게 설정
        if y > 0:
            # 한 칸 이동했을 때 1 일경우
            if arr[x][y - 1] == 1:
                # 지나온 길은 0으로 만들어서 반복 중지
                arr[x][y] -= 1
                y -= 1

        # 우로 이동
        # 맨 오른쪽에 도달했을 때를 고려
        if y < 99:
            # 한 칸 이동했을 때 1 일경우
            if arr[x][y + 1] == 1:
                # 지나온 길은 0으로 만들어서 반복 중지
                arr[x][y] -= 1
                y += 1
        
    print(f'#{tc} {y}')