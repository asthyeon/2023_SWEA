import sys
sys.stdin = open('sample_input.txt')

"""
# 이진 탐색 트리 -> N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값 출력 
# N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값 출력
1. 왼쪽 서브트리 루트 < 현재 노드 < 오른쪽 서브 트리의 루트
2. 중위 순회 방향으로 값이 증가하는 것을 이용하기
3. 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들 수 있음
"""


# 중위 순회 함수 생성
def inorder(K, N):
    global i
    if K <= N:
        inorder(K * 2, N)
        nodes[K] = i
        i += 1
        inorder((K * 2) + 1, N)
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    # 1 부터 N 까지의 자연수를 이진 탐색 트리에 저장
    N = int(input())

    # 노드를 인덱스로 저장
    nodes = [0] * (N + 1)

    K = 1
    i = 1

    inorder(K, N)

    print(nodes[1], nodes[N//2])