import sys
sys.stdin = open('input.txt')

'''
# 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람 구하기
1. 중간에 비어있는 번호가 있을 수 있음
2. 일방향임
'''


# bfs 함수 생성
def bfs(N, S, numbers):
    # 방문 리스트 생성
    visited = [0] * 101
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(S)
    # 시작점 방문 기록
    visited[S] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        t = q.pop(0)
        # 인접한 위치는 인큐하고 방문 기록하기(1 부터 시작)
        for w in numbers[t]:
            if visited[w] == 0:
                # 인큐
                q.append(w)
                # 방문 기록
                visited[w] = visited[t] + 1
    # 방문기록에서 가장 큰 값 찾기
    number_max = 0
    idx_max = 0
    for j in range(1, 101):
        if number_max <= visited[j]:
            number_max = visited[j]
            idx_max = j
    return idx_max


for tc in range(1, 11):
    # 데이터의 길이 N, 시작점 S
    N, S = map(int, input().split())
    # 인접 입력받기
    arr = list(map(int, input().split()))
    # 인접리스트 생성
    numbers = [[] for _ in range(101)]
    # 연결하기
    for i in range(N // 2):
        v1, v2 = arr[i * 2], arr[(i * 2) + 1]
        # 일방향 연결
        numbers[v1].append(v2)

    print(f'#{tc} {bfs(N, S, numbers)}')