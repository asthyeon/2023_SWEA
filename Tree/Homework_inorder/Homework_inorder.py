import sys
sys.stdin = open('input.txt')

"""
# 주어진 트리를 중위순회로 읽기
1. 루트 정점의 번호는 항상 1
"""


# 중위 순회 함수
def inorder(n):
    global word
    # 값이 있으면 (연결되어 있으면)
    if n:
        # 왼쪽 탐색
        inorder(ch1[n])
        word += strings[n]
        # 오른쪽 탐색
        inorder(ch2[n])

for tc in range(1, 11):
    # 정점의 총 수 N
    N = int(input())
    # 부모 노드를 인덱스로 저장
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    # 각 정점에 저장할 문자들
    strings = [0] * (N + 1)

    # 노드 연결
    for _ in range(N):
        # 정점, 문자, 자식 노드 입력 받기
        arr = input().split()

        # 노드 연결
        if len(arr) > 2:
            ch1[int(arr[0])] = int(arr[2])
        if len(arr) > 3:
            ch2[int(arr[0])] = int(arr[3])
        strings[int(arr[0])] = arr[1]

    # 출력할 단어
    word = ''
    # 함수 사용(루트는 1)
    inorder(1)

    print(f'#{tc} {word}')