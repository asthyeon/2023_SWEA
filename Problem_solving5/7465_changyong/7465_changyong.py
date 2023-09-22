import sys
sys.stdin = open('input.txt')

"""
# 창용 마을에 몇 개의 무리가 존재?
1. 창용 마을 N 명 거주
2. 1 ~ N 번 사람 존재
3. 임의의 두 사람이 서로 아는 관계거나 몇 사람을 거쳐서 알 수 있다면 하나의 무리
@ 풀이
(1) 유니온-파인드 이용하기
"""


# find_set 함수
def find_set(x):
    # 해당 값이 그대로라면 그대로 반환
    if parents[x] == x:
        return x

    # 경로 단축
    parents[x] = find_set(parents[x])
    return parents[x]


# union 함수
def union(x, y, parents, rank):
    x = find_set(x)
    y = find_set(y)

    # 랭크가 다르다면 더 큰 쪽으로 부모를 같게 해주기
    if rank[x] != rank[y]:
        if rank[x] > rank[y]:
            for j in range(1, N + 1):
                if parents[j] == y:
                    parents[j] = x
        else:
            for j in range(1, N + 1):
                if parents[j] == x:
                    parents[j] = y
    # 랭크가 같다면 번호가 낮은 쪽으로 붙이고 랭크 올려주기
    else:
        if x > y:
            for j in range(1, N + 1):
                if parents[j] == x:
                    parents[j] = y
            rank[y] += 1
        elif x < y:
            for j in range(1, N + 1):
                if parents[j] == y:
                    parents[j] = x
            rank[x] += 1
        else:
            return


T = int(input())
for tc in range(1, T + 1):
    # 마을에 사는 사람 수 N, 서로를 알고 있는 사람의 관계 수 M
    N, M = map(int, input().split())

    # 마을에 있는 사람들의 부모 노드 및 랭크
    parents = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    # 서로 알고 있는 관계들을 무리로 묶기
    for _ in range(M):
        x, y = map(int, input().split())

        union(x, y, parents, rank)

    # set로 중복 제거하기
    result = set(parents)

    # 0을 제외한 무리 수 출력
    print(f'#{tc} {len(result) - 1}')
