import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 책의 전체 쪽수: P, A가 찾을 쪽수: Pa, B가 찾을 쪽수: Pb
    P, Pa, Pb = map(int, input().split())
    # 책 리스트
    P_list = list(range(1, P + 1))
    # A가 찾은 횟수
    count_A = 0
    # B가 찾은 횟수
    count_B = 0

    # A 탐색
    # 시작페이지
    start_A = 0
    # 끝페이지
    end_A = P - 1
    # 이진 탐색
    while start_A <= end_A:
        # 중간값 설정
        middle = (start_A + end_A) // 2
        # 찾았을 때 횟수를 추가하고 반복문 종료
        if P_list[middle] == Pa:
            count_A += 1
            break
        # 못찾았을 때 중간 값이 찾는 값보다 크다면 왼쪽에서 찾기 
        elif P_list[middle] > Pa:
            end_A = middle
            count_A += 1
        # 못찾았을 때 중간 값이 찾는 값보다 작다면 오른쪽에서 찾기
        else:
            start_A = middle
            count_A += 1

    # B 탐색
    # 시작페이지
    start_B = 0
    # 끝페이지
    end_B = P - 1
    while start_B <= end_B:
        middle = (start_B + end_B) // 2
        if P_list[middle] == Pb:
            count_B += 1
            break
        elif P_list[middle] > Pb:
            end_B = middle
            count_B += 1
        else:
            start_B = middle
            count_B += 1
    
    # 승리자 찾기
    if count_A < count_B:
        print(f'#{tc} {"A"}')
    elif count_A > count_B:
        print(f'#{tc} {"B"}')
    else:
        print(f'#{tc} {0}')
