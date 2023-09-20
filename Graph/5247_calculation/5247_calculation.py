import sys
sys.stdin = open('input.txt')

"""
# 최소 몇 번의 연산이 필요한지 구하기
1. 자연수 N 에 몇 번의 연산을 통해 다른 자연수 M 을 만들려고 함
2. 사용할 수 있는 연산: +1, -1, *2, -10
3. 중간 결과도 백만 이하의 자연수여야함
"""


# 연산자 함수 4가지
def plus_one(num, cnt, q, duple):
    num += 1
    cnt += 1
    if num < 1 or num > 1000000 or num in duple:
        return
    else:
        q.append((num, cnt))
        duple.add(num)


def minus_one(num, cnt, q, duple):
    num -= 1
    cnt += 1
    if num < 1 or num > 1000000 or num in duple:
        return
    else:
        q.append((num, cnt))
        duple.add(num)


def multiply_two(num, cnt, q, duple):
    num *= 2
    cnt += 1
    if num < 1 or num > 1000000 or num in duple:
        return
    else:
        q.append((num, cnt))
        duple.add(num)


def minus_ten(num, cnt, q, duple):
    num -= 10
    cnt += 1
    if num < 1 or num > 1000000 or num in duple:
        return
    else:
        q.append((num, cnt))
        duple.add(num)


# bfs 함수
def bfs(N):
    # 시작점 인큐
    q = [(N, 0)]
    # 인덱스
    top = 0
    # 중복 수 리스트
    duple = set()
    duple.add(N)
    # 큐가 빌 때까지
    while top < len(q):
        num, cnt = q[top]
        top += 1
        if num == M:
            return cnt
        plus_one(num, cnt, q, duple)
        minus_one(num, cnt, q, duple)
        multiply_two(num, cnt, q, duple)
        minus_ten(num, cnt, q, duple)


T = int(input())
for tc in range(1, T + 1):
    # 자연수 N, 다른 자연수 M
    N, M = map(int, input().split())

    result = bfs(N)

    print(f'#{tc} {result}')