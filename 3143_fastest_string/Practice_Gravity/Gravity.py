import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    # arr 길이 재기
    arr_len = 0
    for i in arr:
        arr_len += 1
    # 해당 숫자 초기화
    num = 0
    # 낙차 초기화
    differ = 0
    # 가장 큰 낙차를 구할 리스트 형성
    differ_list = []
    # 모든 요소 중복 수 구하기
    for i in arr:
        num = i
        num_duple = 0
        for j in arr:
            if num <= j:
                num_duple += 1
        # 모든 요소별 낙차 구하기
        differ = arr_len - arr.index(num) - num_duple
        # 가장 큰 낙차를 구할 리스트에 개별 낙차값 붙이기
        differ_list.append(differ)
    # 가장 큰 낙차 구하기
    differ_one = differ_list[0]
    for i in differ_list:
        if differ_one < i:
            differ_one = i
    ans = differ_one

    print(f'#{tc} {ans}')