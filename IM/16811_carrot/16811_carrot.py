import sys
sys.stdin = open("sample_in.txt")

"""
# 당근의 개수 차이 중 최소 값 출력
1. N 개의 당근 주문 -> 대, 중, 소 구분
2. 같은 크기의 당근은 같은 상자
3. 비어 있는 상자 X
4. 한 상자에 N/2개 초과 X -> N//2 로 풀기
5. 각 상자에 든 당근의 개수 차이가 최소일 때의 차이 값 출력
* 포장할 수 없는 경우 -1 출력
* 당근의 최대 크기 30
"""

T = int(input())
for tc in range(1, T + 1):
    # 당근의 수 N
    N = int(input())

    # 당근 N 개 리스트
    arr = list(map(int, input().split()))

    # 당근 크기를 인덱스로 개수를 받을 리스트
    Ci_list = [0] * 31
    for i in arr:
        Ci_list[i] += 1

    # 당근 개수를 리스트에 넣기
    new_arr = []
    for Ci in Ci_list:
        if Ci != 0:
            new_arr.append(Ci)

    # 최소 차이 구하기
    differ_min = 1000
    # 3 박스로 나눠 담는 경우의 수 구하기(합으로 구하기)
    for x in range(1, N):
        for y in range(x + 1, N):
            box1 = sum(new_arr[:x])
            box2 = sum(new_arr[x:y])
            box3 = sum(new_arr[y:])
            
            # 박스가 N / 2 를 초과하지 않고 최소 1개 이상 들어있다면
            if box1 <= N // 2 and box2 <= N // 2 and box3 <= N // 2:
                if box1 > 0 and box2 > 0 and box3 > 0:
                    # 차이 비교하기
                    differ = []
                    differ.append(abs(box1 - box2))
                    differ.append(abs(box2 - box3))
                    differ.append(abs(box3 - box1))
                    if differ_min > max(differ):
                        differ_min = max(differ)

    # 포장을 못했다면 -1 출력을 위한 조건 형성
    if differ_min == 1000:
        differ_min = -1

    # 출력하기
    print(f'#{tc} {differ_min}')
