import sys
sys.stdin = open('input.txt')

# DFS 알고리즘

'''
<연습문제3>
다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오.
시작 정점을 1로 시작하시오.
- 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
- 정점(V)의 개수: 7개
- 엣지(E)(서로 잇게 해주는 선)의 개수: 8개
- 시작 정점: 1
# 입력 값
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 출력 결과의 예는 다음과 같다.
- 1-2-4-6-5-7-3
'''

'''
# 저장 방식
1. 2차원 배열을 형성하기
- arr = [[0] * (V + 1) for _ in range(V + 1)] 로 빈 어레이 형성
- 1 과 2 가 연결되어 있으면, arr[1][2], arr[2][1] 에 값을 넣어주는 방식
2. 인접 리스트 형성하기
- 0 과 연결 되어 있는 것 []
- 1 과 연결 되어 있는 것 [2, 3]
- 2 와 연결 되어 있는 것 [2, 4, 5]
= [[], [2, 3], [2, 4, 5]]
'''

def dfs(n, V, adj_m):
    stack = []                  # stack 생성
    visited = [0] * (V + 1)     # visited 생성
    visited[n] = 1              # 시작점 방문 표시
    print(n)                    # do[n] (방문)
    while True:
        for w in range(1, V + 1):   # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(v), v = w
                n = w
                print(n)        # do(w) (방문)
                visited[n] = 1  # w 방문 표시
                break # for w, n 에 인접인 w 찾은 경우
        else:
            if stack: # 스택에 지나온 정점(갈림길)이 남아 있으면
                n = stack.pop() # pop()해서 다시 다른 w를 찾을 n 준비
            else: # 스택이 비어있으면
                break # while True 탐색 끝
    return


V, E = map(int, input().split()) # 1번부터 V번 정점, E 개의 간선
arr = list(map(int, input().split()))
adj_m = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[(i * 2) + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)