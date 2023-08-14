import sys
sys.stdin = open('input.txt')

'''
# 계산식을 후위 표기식으로 바꾸어 계산
'''

for tc in range(1, 11):
    # 문자열 계산식의 길이
    N = int(input())

    # 문자열 받기
    arr = input()

    # 합계
    arr_sum = 0

    for i in range(N):
        # 숫자라면
        if arr[i].isdigit():
            # 초항일 때는
            if i == 0:
                # 2번 째 숫자와 합치기
                numb = arr[0] + arr[2]
                arr_sum += int(numb)

            elif i >= 4:
                arr_sum += int(arr[i])

    print(f'#{tc} {arr_sum}')


