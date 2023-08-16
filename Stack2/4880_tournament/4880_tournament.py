import sys
sys.stdin = open('sample_input.txt')

'''
# 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑기 
1. 1 번부터 N 번까지 N 명의 학생이 N 장의 카드를 나눠 갖는다.
2. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 됨
3. 그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑음
4. 두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식
5. 1: 가위, 2: 바위, 3: 보
'''

# 가위바위보 함수 생성
def rsp(arr, a, b):
    # 가위일 때 비기거나 이기는 경우
    if arr[a] == 1:
        if arr[b] == 1 or arr[b] == 3:
            return a
        else:
            return b
    # 바위일 때 비기거나 이기는 경우
    if arr[a] == 2:
        if arr[b] == 2 or arr[b] == 1:
            return a
        else:
            return b
    # 보일 때 비기거나 이기는 경우
    if arr[a] == 3:
        if arr[b] == 3 or arr[b] == 2:
            return a
        else:
            return b


# 토너먼트 함수 형성
def tournament(arr, i, j):
    # 학생 수가 한 명이 될 경우 출전
    if i == j:
        return i

    # 중간 지점을 나누기
    middle = (i + j) // 2
    # 왼쪽 학생
    i = tournament(arr, i, middle)
    # 오른쪽 학생
    j = tournament(arr, middle + 1, j)

    # 가위바위보
    return rsp(arr, i, j)


T = int(input())
for tc in range(1, T + 1):
    # 학생 수
    N = int(input())
    # 시작점과 끝점
    i = 0
    j = N - 1
    # 학생들의 가위바위보
    students = list(map(int, input().split()))

    print(f'#{tc}', tournament(students, i, j) + 1)