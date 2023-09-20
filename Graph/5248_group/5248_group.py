import sys
sys.stdin = open('input.txt')

"""
# 전체 몇 개의 조가 만들어지는 출력하기
1. 한 조의 인원 제한 X
2. 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조
3. 번호를 적지도 않고 다른 사람에게 지목되지 않은 사람은 단독으로 조를 구성
@ 풀이
(1) 상호배타 집합 사용하기
(2) 랭크 사용 및 자식도 같은 그룹에 넣어야함
"""


# find_set 함수
# 어떤 조에 속해있는지 찾기(루트 노드를 찾기)
def find_set(num):
    if N_list[num] == num:
        return N_list[num]

    N_list[num] = find_set(N_list[num])
    return N_list[num]


# union 함수
# 신청서를 합치기
def union(x, y, N_list, rank):
    root_x = find_set(x)
    root_y = find_set(y)

    # 루트가 다르다면
    if root_x != root_y:
        if rank[root_x] == rank[root_y]:
            # 루트 및 자식들 또한 바꿔주기
            for k in range(N + 1):
                if N_list[k] == root_y:
                    N_list[k] = root_x
            rank[root_x] += 1
        elif rank[root_x] > rank[root_y]:
            # 루트 및 자식들 또한 바꿔주기
            for k in range(N + 1):
                if N_list[k] == root_y:
                    N_list[k] = root_x
        else:
            # 루트 및 자식들 또한 바꿔주기
            for k in range(N + 1):
                if N_list[k] == root_x:
                    N_list[k] = root_y


T = int(input())
for tc in range(1, T + 1):
    # 출석번호 N, 신청서 수 M
    N, M = map(int, input().split())
    # 출석리스트
    N_list = [i for i in range(N + 1)]
    # 신청서 리스트
    apply = list(map(int, input().split()))
    # 트리의 높이를 찾기 위한 랭크
    rank = [0] * (N + 1)

    # 신청서를 받고 조를 구성하기
    for j in range(M):
        x, y = apply[j * 2], apply[(j * 2) + 1]

        union(x, y, N_list, rank)

    # 조의 개수를 구하기 위해 0 제거 및, set로 중복 제거
    N_list.pop(0)
    result = set(N_list)

    print(f'#{tc} {len(result)}')


