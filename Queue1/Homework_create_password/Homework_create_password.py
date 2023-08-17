import sys
sys.stdin = open('input.txt')

'''
# 주어진 조건에 따라 n 개의 수를 처리하면 8자리의 암호 생성
1. 8개의 숫자를 입력받기
2. 첫 번째 숫자를 1 감소한 뒤 맨 뒤로 보내기
3. 다음 첫 번째 수는 2 감소한 뒤 맨뒤로 보내기
4. 다음 첫 번째 수가 5가 감소할 때까지 반복하는 것이 한 사이클
* 숫자가 감소할 때 0 보다 작아지는 경우 0으로 유지되며 프로그램 종료, 이 때의 8자리 숫자 값이 암호가 됨
'''

for tc in range(1, 11):
    T = int(input())

    # 8개의 데이터
    numbers = list(map(int, input().split()))

    # 감소할 숫자
    i = 0
    
    # 암호 생성기
    while True:
        # 감소할 숫자를 1씩 늘려주기
        i += 1
        # 첫 항에 1 감소
        numbers[0] -= i
        # 만일 그 숫자가 0보다 작거나 같으면 0으로 만들고 뒤로 보낸 후 반복 종료
        if numbers[0] <= 0:
            numbers[0] = 0
            numbers.append(numbers.pop(0))
            break
        # 감소한 숫자를 뒤로 보내기
        numbers.append(numbers.pop(0))
        # 숫자가 5가 될 경우 초기화
        if i == 5:
            i = 0

    print(f'#{tc}', *numbers)