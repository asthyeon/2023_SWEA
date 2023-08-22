import sys
sys.stdin = open('sample_input.txt')

"""
# 리프 노드의 값이 주어지면 나머지 노드에 자식 노드의 값의 합을 저장, 지정 번호 값 출력
1. 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있음
"""

T = int(input())
for tc in range(1, T + 1):
    # 노드의 개수 N, 리프 노드의 개수 M, 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    # 배열 형성
    arr = [0] * (N + 1)
    # 리프 노드 삽입하기
    for _ in range(M):
        num, key = map(int, input().split())
        arr[num] = key

    # 자식 노드 더한 값은 부모 노드
    for i in range(N, 0, -1):
        if i // 2 > 0:
            arr[i // 2] += arr[i]

    print(f'#{tc} {arr[L]}')
