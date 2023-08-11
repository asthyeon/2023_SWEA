import sys
sys.stdin = open('input1.txt')

'''
# 각 구역 별로 가장 긴 구조물의 길이를 찾기
'''

T = int(input())
for tc in range(1, T + 1):
    # N 개의 줄, M 개의 데이터
    N, M = map(int, input().split())

    # data 형성
    data = [list(map(int, input().split())) for _ in range(N)]

    # 가장 큰 구조물의 길이
    max_length = 0
    
    # 0,0 부터 탐색
    for x in range(N):
        for y in range(M):
            # 길이 초기화
            length = 0
            # 해당 위치가 1일 때
            if data[x][y] == 1:
                # 길이 1 추가
                length += 1
                # y 범위 설정
                if y + 1 < M:
                    # 같은 행의 다음 열이 1 일 때
                    if data[x][y + 1] == 1:
                        # 1 이 있는 만큼 길이 늘리기
                        for i in range(y + 1, M):
                            if data[x][i] == 1:
                                length += 1
                            # 다음 열이 1이 아니면 반복 종료
                            else:
                                break
                        # 가장 큰 길이 찾기
                        if max_length < length:
                            max_length = length
                        # 해당 위치의 다음 행의 위치에 1이 있을 수도 있으므로 길이를 1 추가한 채로 다음 실행
                        length = 1
                # x 범위 설정
                if x + 1 < N:
                    # 같은 열의 다음 행이 1 일 때
                    if data[x + 1][y] == 1:
                        # 1 이 있는 만큼 길이 늘리기
                        for j in range(x + 1, N):
                            if data[j][y] == 1:
                                length += 1
                            # 다음 행이 1 이 아니면 반복 종료
                            else:
                                break
                if max_length < length:
                    max_length = length

    print(f'#{tc} {max_length}')

