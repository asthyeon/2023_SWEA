import sys
sys.stdin = open('sample_input.txt')

"""
# 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내기
1. 부모가 없는 노드가 전체의 루트 노드가 됨
2. 노드 번호는 1번부터 E+1번까지 존재
"""


# 전위 순회
def preorder(N):
    global cnt
    # 정점이 존재한다면(0이 아니라면)
    if N:
        # 노드 수 + 1
        cnt += 1
        # 왼쪽 자식 노드 수 세기
        preorder(ch1[N])
        # 오른쪽 자식 노드 수 세기
        preorder(ch2[N])


T = int(input())
for tc in range(1, T + 1):
    # 간선의 개수 E, 루트 N
    E, N = map(int, input().split())
    # 부모 자식 노드 번호 쌍
    arr = list(map(int, input().split()))

    # 부모 노드를 인덱스로 자식 노드 연결
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(E):
        # 부모 노드와 자식 노드 입력
        p, c = arr[i * 2], arr[(i * 2) + 1]

        # 자식1에 자식이 아직 없다면 자식1에 자식 연결
        if ch1[p] == 0:
            ch1[p] = c
        # 자식1에 자식이 있다면 자식2에 자식 연결
        else:
            ch2[p] = c

    # 노드 수
    cnt = 0

    # 함수 적용
    preorder(N)

    print(f'#{tc} {cnt}')
