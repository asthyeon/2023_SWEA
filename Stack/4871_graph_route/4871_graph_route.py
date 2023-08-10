import sys
sys.stdin = open('sample_input.txt')

'''
# 특정한 두 개의 노드에 경로가 존재하는지 확인하기
1. 경로가 있으면 1, 없으면 0 출력
'''

# 노드연결을 간편하게 보기 위함
# from pprint import pprint

T = int(input())
for tc in range(1, T + 1):
    # V개 이내의 노드, E개의 간선
    V, E = map(int, input().split())

    # 각 노드에 연결된 간선을 받을 리스트 생성
    arr = []
    for _ in range(E):
        v, w = map(int, input().split())
        arr.append(v)
        arr.append(w)

    # 출발 노드 S, 도착 노드 G
    S, G = map(int, input().split())

    # 각 노드를 엣지로 연결하기
    # 빈 2차원 배열 형성
    adj_m = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        # v1 과 v2 를 연결되어 있는 노드 값을 할당
        v1, v2 = arr[i * 2], arr[(i * 2) + 1]
        # 할당된 값을 빈 2차원 배열의 인덱스 값에 1로 넣어서 연결
        adj_m[v1][v2] = 1
        # 일방향이기때문에 돌아오는 것은 고려 X
        # adj_m[v2][v1] = 1

    # dfs 함수 설정
    def dfs(S, V, adj_m):
        # stack 생성
        stack = []
        # 방문을 기록할 visited 생성
        visited = [0] * (V + 1)
        # 시작 노드 방문 표시
        visited[S] = 1

        # 방문 반복문
        while True:
            # 현재 정점에 인접하고 미방문 w 찾기
            for w in range(1, V + 1):
                # 정점과 연결되어 있고, 방문한 곳이 아닐 때
                if adj_m[S][w] == 1 and visited[w] == 0:
                    # 지나온 곳을 stack 에 push
                    stack.append(S)
                    # 현재 위치를 w 로 바꾸기
                    S = w
                    # 방문 기록하기
                    visited[w] = 1
                    # 미방문 w 를 찾은 경우엔 break 를 실행함으로써 else 구문 미실행
                    break
            # 미방문 w를 찾지 못한 경우
            else:
                # stack 에 방문한 곳이 남아있을 경우
                if stack:
                    # pop()을 통해서 현재 위치는 이전 곳으로 돌아가고 다시 다른 w 를 찾을 준비
                    S = stack.pop()
                # stack 에 방문한 곳이 없다면
                else:
                    # G 까지 경로가 없는 곳으로 간주하고 while 반복문 종료
                    print(f'#{tc} {0}')
                    break
            # 현재 노드가 도착 노드에 도착할 경우 반복문 종료
            if S == G:
                print(f'#{tc} {1}')
                break
        return

    # 함수 사용
    dfs(S, V, adj_m)