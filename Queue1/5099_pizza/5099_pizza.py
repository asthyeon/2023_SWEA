import sys
sys.stdin = open('sample_input.txt')

'''
# 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내기
1. N 개의 피자를 동시에 구울 수 있다.
2. 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다
3. 피자는 1번 위치에서 넣거나 뺄 수 있음(시계방향 회전)
4. M 개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지 않은 치즈의 양은 반으로 줄어듦
5. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어듦
6. 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그자리에 남은 피자를 순서대로 넣는다.
'''

T = int(input())
for tc in range(1, T + 1):
    # 화덕의 크기 N, 피자 개수 M
    N, M = map(int, input().split())
    # 치즈의 양
    Ci = list(map(int, input().split()))

    # 화덕생성
    cQ = [0] * N
    cQ_idx = [0] * N

    # 화덕 피자받침 번호
    front = 0

    # 화덕에 넣을 피자 번호
    insert = 0

    # 꺼내진 피자
    pizza = [0] * M
    pizza_out = []

    # 화덕에 피자 넣기
    while len(pizza_out) < M - 1:
        # 화덕에 피자가 있다면(치즈가 다 안녹았다면)
        if cQ[front] > 0:
            # 치즈 녹여주기
            cQ[front] = cQ[front] // 2
            # 치즈를 녹였을 때 다 녹았다면
            if cQ[front] == 0:
                # 피자 꺼내기
                pizza_out.append(cQ_idx[front])
                pizza[cQ_idx[front] - 1] = 1
                cQ_idx[front] = 0

        # 화덕이 비어있으면
        if cQ[front] == 0:
            # 넣을 피자가 있다면
            if insert < M:
                # 피자 넣기
                cQ[front] = Ci[insert]
                cQ_idx[front] = insert + 1
                # 다음 피자로 순서 바꾸기
                insert += 1
        
        # 화덕 돌리기
        front += 1
        # 화덕 돌리기 초기화
        if front == N:
            front = 0

    print(f'#{tc} {pizza.index(0) + 1}')
