import sys

sys.stdin = open('input.txt')

# N 개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력하라

# 이미 가진 랜선의 개수: K, 필요한 랜선의 개수: N
K, N = map(int, input().split())

# 랜선 리스트
lan = []

# 각 랜선의 길이 받기
for _ in range(K):
    lan.append(int(input()))

# 랜선 리스트 길이
lan_length = 0
for i in lan:
    lan_length += 1

# 오름차순 정렬
for i in range(lan_length - 1, 0, -1):
    for j in range(i):
        if lan[j] > lan[j + 1]:
            lan[j], lan[j + 1] = lan[j + 1], lan[j]

# 각 랜선의 합
lan_sum = 0
for i in lan:
    lan_sum += i

# N 으로 나눴을 때 대략적으로 필요한 랜선의 길이
lan_need = lan_sum / 11

# 잘라서 생긴 랜선 수
lan_cut = 0

# 자른 랜선의 길이중 최대 길이를 구하기 위한 리스트
lan_min_list = []

# 반복문
while len(lan_min_list) < len(lan):
    # 이진 탐색
    for i in range(lan_length):
        start = 0
        end = lan[i] - 1
        while start <= end:
            middle = (start + end) / 2
            if middle == lan_need:
                lan_min_list.append(middle)
                break
            elif middle > lan_need:
                end = middle - 1
            else:
                start = middle + 1

print(lan_min_list)


