import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 버스 노선 수
    N = int(input())

    # 빈 노선 리스트
    route_list = []

    # 각 노선을 입력받기
    for i in range(N):
        start, end = map(int, input().split())
        # 마지막 숫자에 + 1을 함으로서 마지막 정류장도 이용하도록 함
        route = list(range(start, end + 1))
        route_list.append(route)

    # 정류장 P
    P = int(input())
    # 각 버스 정류장에 몇개의 노선이 다니는지 카운트를 넣을 리스트
    count_list = []

    for i in range(P):
        # 카운트 초기화
        count = 0
        # 정류장 번호 받기
        stop = int(input())
        # 각 정류장이 각 노선 별로 포함되어 있으면 count +1
        for j in route_list:
            for k in j:
                if stop == k:
                    count += 1
        # count_list 에 count 더하기
        count_list.append(count)
    
    # 순서대로 출력(공백을 포함)
    print(f'#{tc}', *count_list)
    # print(f'#{tc}', end = " ")
    # for i in range(P):
    #     print(int(count_list[i]), end = " ")
    # print()