import sys
sys.stdin = open('input.txt')

'''
# A 도시에서 B 도시로 가는 길 조사
'''

# from pprint import pprint

for tc in range(1, 11):
    # 테스트 케이스 T, 길의 총 개수 N
    T, N = map(int, input().split())

    # 출발점 S, 도착점 G
    S = 0
    G = 99

    # 길 입력 받기
    arr = list(map(int, input().split()))

    # 100 x 100 배열 형성
    adj_m = [[0] * 100 for _ in range(100)]

    # 길 연결하기(일방향)
    for i in range(N):
        v1, v2 = arr[i * 2], arr[(i * 2) + 1]
        adj_m[v1][v2] = 1

    # 함수 설정
    def dfs(S, N, adj_m):
        # 스택 형성
        stack = []
        # 방문 리스트 형성
        visited = [0] * 100
        # 시작점 방문 기록
        visited[S] = 1

        # 길찾기
        while True:
            # 배열 크기 만큼 반복
            for w in range(100):
                # 만약 다음 갈 곳(w)이 인접하고, 방문한 적이 없다면
                if adj_m[S][w] == 1 and visited[w] == 0:
                    # 지나온 곳을 스택에 넣고
                    stack.append(S)
                    # 현재 위치 = w
                    S = w
                    # 방문 기록
                    visited[w] = 1
                    break
            # 다음 갈 곳을 못찾았다면
            else:
                # 지나온 곳의 다른 길을 찾기 위해 돌아가기
                if stack:
                    S = stack.pop()
                # 스택이 비어있다면 경로를 못 찾은 것
                else:
                    print(f'#{T}, {0}')
                    break
            # 도착점에 도달한다면
            if S == G:
                print(f'#{T} {1}')
                break

    # 함수 사용
    dfs(S, N, adj_m)



