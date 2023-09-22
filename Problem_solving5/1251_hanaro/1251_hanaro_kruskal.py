import sys
sys.stdin = open('input.txt')

"""
# 총 환경 부담금을 최소로 지불하여 모든 섬 연결하기
1. 인도네시아 내 모든 섬을 해저터널로 연결하는 것을 목표로 함
2. 환경 부담금 = 환경 부담 세율(E) * (각 해저터널의 길이(L) ** 2)
 - 부담금 = E * L^2 
3. 양방향 그래프
@ 풀이
(1) MST 를 구성해야함
(2) kruskal 알고리즘 사용하기
(3) 세금을 거리를 전부 다 더한 후 구해야함
"""
import heapq


# 거리 구하는 함수
def length(x1, y1, x2, y2):
    length = ((y2 - y1) ** 2) + ((x2 - x1) ** 2)
    return length


# find_set 함수
def find_set(x):
    # 해당되는 값이면 그대로 출력
    if parents[x] == x:
        return x
    
    # 해당되지 않으면 경로 단축
    parents[x] = find_set(parents[x])
    return parents[x]


# union 함수
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    
    # 부모가 다르다면 더 작은 값으로 설정
    if x > y:
        parents[x] = y
    elif x < y:
        parents[y] = x
    # 부모가 같다면 함수 종료
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    # 섬의 개수 N
    N = int(input())
    # 각 섬들의 x 좌표
    x_list = list(map(int, input().split()))
    # 각 섬들의 y 좌표
    y_list = list(map(int, input().split()))
    # 환경 부담 세율
    E = float(input())
    # 각 섬들의 거리
    islands = []

    # 각 섬들의 거리 구하기
    for i in range(N):
        x1 = x_list[i]
        y1 = y_list[i]
        # 단방향으로 연결
        for j in range(i + 1, N):
            x2 = x_list[j]
            y2 = y_list[j]
            
            # 거리 구하기
            leng = length(x1, y1, x2, y2)

            # 길이, 시작점, 끝점 순으로 append
            islands.append((leng, i, j))

    # 길이순으로 정렬
    islands.sort()

    # 인덱스를 조정하기 위한 부모 리스트
    parents = [i for i in range(N)]
    cnt = 0
    sum_length = 0
    for l, f, t in islands:
        # 싸이클이 발생하지 않으면
        if find_set(f) != find_set(t):
            cnt += 1
            sum_length += l
            union(f, t)
            # MST 구성이 끝나면 반복 종료
            if cnt == N - 1:
                break
    
    # 세율 곱해서 반올림
    print(f'#{tc} {round(sum_length * E)}')
