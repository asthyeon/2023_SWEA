import sys
sys.stdin = open('sample_input.txt')

'''
# 최소 몇 단위 시간 만에 학생들이 이동하는지
1. 복도 구간이 겹치면 안됨
2. 겹치는 모든 부분 조사하기
3. 돌아가는 방이 현재 방보다 낮은 경우 고려하기
4. 홀수 도착(도착 짝수 고려 안됨 + 1 필요), 역순일시 홀수 시작 +1 필요
5. 짝수 시작(시작 홀수 고려 안됨 - 1 필요), 역순일시 짝수 도착 +1 필요
'''

T = int(input())
for tc in range(1, T + 1):
    # 돌아가야 할 학생들의 수 N
    N = int(input())

    # 구간 만들기
    corridor = [0] * 401

    # 현재 방과 돌아갈 방
    for i in range(N):
        Now, Go = map(int, input().split())

        # 현재 방이 돌아갈 방 보다 낮거나 같다면 위치 체인지
        if Now > Go:
            Now, Go = Go, Now
        # 시작점이 짝수라면 - 1
        if Now % 2 == 0:
            Now -= 1
        # 도착점이 홀수라면 + 1
        if Go % 2 == 1:
            Go += 1
        # 같은 구간 지나갈 때마다 횟수 + 1
        for j in range(Now, Go + 1):
            corridor[j] += 1

    # 횟수가 가장 큰 값 출력
    print(f'#{tc} {max(corridor)}')
