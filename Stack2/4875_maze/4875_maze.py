import sys
sys.stdin = open('sample_input.txt')

'''
# 출발지에서 목적지에 도착하는 경로가 존재하는지 확인
1. 도착가능 1, 아니면 0 출력
2. 0 은 통로, 1 은 벽, 2 는 출발, 3 은 도착
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 미로 형성
    arr = [list(input()) for _ in range(N)]

    # 도착점 구하기
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                x = i
                y = j

    # dfs 함수
    def dfs(N, arr):
        global x
        global y
        # 정답조건
        ans = 0
        # stack 형성
        stack = []
        # 시작점 push
        stack.append(y)
        stack.append(x)
        while True:
            # 델타탐색
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                # 벽 형성
                if 0 <= nx < N and 0 <= ny < N:
                    # 통로를 만난다면
                    if arr[nx][ny] == '0':
                        # 이동할 곳은 5 로 만들기
                        arr[nx][ny] = '5'
                        # 이동
                        x = nx
                        y = ny
                        # 이동한 곳은 push
                        stack.append(ny)
                        stack.append(nx)
                        break
                    # 출발점을 만난다면 정답 설정
                    elif arr[nx][ny] == '3':
                        ans = 1
                        break
            # 전진할 곳이 없다면
            else:
                # 스택이 비어있지 않다면 지난 좌표로 재설정
                if stack:
                    x = stack.pop()
                    y = stack.pop()
                    # 분기점이라면 재 push
                    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        nx = x + dx
                        ny = y + dy
                        # 벽 형성
                        if 0 <= nx < N and 0 <= ny < N:
                            # 통로를 만난다면
                            if arr[nx][ny] == '0':
                                stack.append(y)
                                stack.append(x)
                # 스택이 비어있다면 오답 설정
                else:
                    ans = 0
                    break
            # 정답이라면 반복 종료
            if ans == 1:
                break
        
        # 출력
        if ans == 1:
            print(f'#{tc} {1}')
        else:
            print(f'#{tc} {0}')
    
    # 함수 사용
    dfs(N, arr)



