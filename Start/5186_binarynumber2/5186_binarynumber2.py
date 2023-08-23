import sys
sys.stdin = open("sample_input.txt")

"""
# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸기
1. 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 출력
2. 13자리 이상이 필요한 경우 'overflow' 출력
"""

T = int(input())
for tc in range(1, T + 1):
    # 소수 입력받기
    number = float(input())

    # 이진 수
    bi = []

    # 나눈 값
    divide = 1 / 2
    # 비교할 값
    total = 0
    
    while True:
        # 소수에서 비교할 값이 나눈 값보다 크거나 같다면 토탈에 디바이드를 넣고 이진 수에 1 푸쉬 
        if number - total >= divide:
            total += divide
            bi.append(1)
        # 더 작다면 이진 수에 0 푸쉬
        else:
            bi.append(0)
        
        # 두 수가 같아진다면 이진 수 출력
        if total == number:
            print(f'#{tc} ', *bi, sep='')
            break
        # 두 수가 다르고
        else:
            # 길이가 13자리 이상이 되면 overflow 출력
            if len(bi) > 12:
                print(f'#{tc} overflow')
                break
            # 아니라면 나눈 값을 또 나누기
            else:
                divide = divide / 2








