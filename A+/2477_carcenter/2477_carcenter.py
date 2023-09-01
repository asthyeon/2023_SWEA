import sys
sys.stdin = open("sample_input.txt")

"""
# 지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객들 번호를 찾아 합 출력
1. 접수 창구에서 고장 접수
2. 정비 창구에서 차량 정비 -> 완료 후 설문지
3. 접수 및 정비 처리 시간 존재
* 접수 창구 우선순위
(1) 고객번호가 낮은 순서대로 웃너 접수
(2) 빈 창구가 여러 곳인 경우 창구번호가 작은 곳
* 정비 창구 우선순위
(1) 먼저 기다리는 고객이 우선
(2) 접수 창구에서 동시에 접수를 완료한 경우 이용했던 창구번호가 작은 고객 이우선 정비
(3) 빈 창구가 여러 곳인 경우 창구번호가 작은 곳
* 이동 시간은 0
* 이용한 고객번호를 구하기
"""

T = int(input())
for tc in range(1, T + 1):
    # 접수 창구 N, 정비 창구 M, 고객 수 K, 지갑 분실 고객 접수 A, 정비 B
    N, M, K, A, B = map(int, input().split())
    
    # 접수 창구 시간
    N_time = list(map(int, input().split()))
    
    # 정비 창구 시간
    M_time = list(map(int, input().split()))
    
    # 고객 방문 시간
    K_time = list(map(int, input().split()))

    # 시간
    
    