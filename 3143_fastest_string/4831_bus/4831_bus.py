import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 한 번 충전으로 이동 가능한 정류장 수:K,
    # 종점 번호: N,
    # 충전기가 설치된 정류장 수:M
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 번호
    arr = list(map(int, input().split()))
    # 충전 횟수
    charging = 0

    # 전체 인덱스 형성
    c = [0] * (N + 1)
    for i in arr:
        c[i] = i

    # 이동가능한 거리
    distance_list = []
    for i in range(1, len(arr)):
        distance = arr[i] - arr[i - 1]
        distance_list.append(distance)

    move = K
    for j in range(1, N + 1):
        if c[j] == 0:
            if move == 0:
                break
            else:
                move -= 1
                distance_list[0] -= 1
                print(move)
        else:
            if distance_list[0] == move:
                move = K
                charging += 1
                distance_list.pop(0)
            elif distance_list[0] > move:
                break
            else:
                if distance_list[1] <= move:
                    move -= 1
                    distance_list.pop(0)


    print(f'#{tc} {charging}')