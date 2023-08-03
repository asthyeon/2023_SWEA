# 행열 탐색 연습

# 0 으로 초기화 된 N * M 의 2 차원 배열 생성하기
from pprint import pprint as pp
m = 5
n = 5

arr = []
for i in range(n):
    row = [0] * m
    arr.append(row)
# pp(arr)

# 행 우선 순회를 다른 것보다 우선시 하여 학습하자!

num_list = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# # 1. 행 우선 순회 정상적으로 순서대로 진행되는지 확인
# for r in range(len(num_list)):
#     for c in range(len(num_list)):
#         print(f'{num_list[r][c]}', end=' ')
#     print()
#
# print()
# # 2. 열 우선 순회
# for c in range(len(num_list)):
#     for r in range(len(num_list)):
#         print(f'{num_list[r][c]}', end=' ')
#     print()
#
# print()
# # 3. 역-행 우선 순회
# for i in range(len(num_list)):
#     for j in range(len(num_list) - 1, -1, -1):
#         print(num_list[i][j], end=' ')
#     print()
#
# print()
# # 4. 역-열 우선 순회
# for j in range(len(num_list)):
#     for i in range(len(num_list) - 1, -1, -1):
#         print(num_list[i][j], end=' ')
#     print()
    
num_list = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


# 가장자리의 합
def edge_sum(arr):
    #  순회를 하면서, 2차원 리스트의 가장자리에 있는 원소들을 합한다.
    edge_sum_result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 or i == (len(arr) - 1) or j == 0 or j == (len(arr) - 1):
                print(arr[i][j])
                edge_sum_result += arr[i][j]

    return edge_sum_result

result = edge_sum(num_list)
print(result)

# 델타 탐색
# 문제에 제시된 제약 조건에 따라 탐색 순서는 달라질 수 있다.
# 대각선
# 하 우 좌 상
# 1 이면 상
# 2 라면 하 등으로 방향을 설정해주기도 함

        # 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
# 튜플로 선언하는게 맞을 수 있음

# 대각선
        # 좌상단 / 좌하단 / 우하단 / 우상단
dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
for nx, ny in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    pass

# 1 인 값을 가진 인덱스 찾기
# 미로 시작점은 1 탈출구는 2

# 1. 1인 좌표 찾기
# 2. 탈출구 찾기

def without_delta():
    print(num_list[r - 1][c]) # 상
    print(num_list[r + 1][c]) # 하
    print(num_list[r][c - 1]) # 좌
    print(num_list[r][c + 1]) # 우

# 벽을 세워야한다.
# 주어진 2차원 리스트의 범위를 벗어나지 않도록 제한을 두는 행위

# 1. 벽의 제한을 두는데, 벽을 넘어가는 경우, 아무것도 하지 않는다.
# 2. 벽을 넘어가지 않는 경우에만 기능을 수행한다.

x = 0
y = 1

for d in range(4):
    # 다음에 이동할(탐색할) 좌표 담기
    nx = x + dx[d]
    ny = y + dy[d]

    # map 을 벗어나는 경우 아무것도 하지 않기.
    # if nx < 0 or nx >= N or ny < 0 or ny >= N:
    if isSafeArea: # 탐색 가능한 좌표 확인
        continue
    # print(결과 프린트)
    # 특정 로직 수행
    
    # 벽을 넘어가지 않는 경우에만 수행하기
    if nx <= 0 < N and 0 <= ny < N:
        # 로직 수행


def isSafeArea(nx, ny, N):
    if nx <= 0 < N and 0 <= ny < N:
        return True
    return False