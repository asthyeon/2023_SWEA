import sys
sys.stdin = open('input.txt')

"""
# 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것 출력
1. 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같음
"""


# 부분집합 함수
def subset(arr):
    result = []
    for i in range(1, 1 << N):
        sub = []
        for j in range(len(arr)):
            if i & (1 << j):
                sub.append(arr[j])
        # 합의 부분집합 구하기
        result.append(sum(sub))

    # 정렬
    result.sort()
    # 중복 제거
    # result = list(set(result))

    return result


T = int(input())
for tc in range(1, T + 1):
    # 점원 수 N, 선반의 높이 B
    N, B = map(int, input().split())

    # 각 점원의 키 리스트
    arr = list(map(int, input().split()))
    arr.sort()

    result = subset(arr)

    for x in result:
        if x >= B:
            print(f'#{tc} {x - B}')
            break
