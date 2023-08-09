import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # arr = list(map(str, input().split('0'))) 1번에 구해보기
    arr = list(map(int, input()))
    # 연속된 횟수 카운팅
    arr_count = 0
    # 가장 큰 연속된 횟수
    max_count = 0
    # arr 만큼 i 번 반복
    for i in arr:
        # i == 1이라면
        if i == 1:
            # 카운트 + 1
            arr_count += 1
        # i != 1이라면 
        else:
            # 연속된 횟수 카운팅이 더 크다면
            if max_count < arr_count:
                # 카운팅을 교체해주기
                max_count = arr_count
                # 연속된 횟수 카운팅 초기화
                arr_count = 0
    # 마지막이 0이 아닐 때를 대비해 한 번더 교체 조건 형성
    if max_count < arr_count:
        max_count = arr_count
    # 출력
    print(f'#{tc} {max_count}')