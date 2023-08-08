import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(T):
    tc, n = input().split()
    words = input().split()
    numbers = ["ZRO", "ONE", "TWO", "THR",
               "FOR", "FIV", "SIX", "SVN",
               "EGT", "NIN"]

    result = ''

    # numbers 라는 리스트 순서대로 순회하면서,
    for number in numbers:
        for word in words:
            # 비교 값이 동일하다면,
            if word == number:
                result += word

    # 1. 문자 -> 숫자
    # 2. 숫자 정렬
    # 3. 숫자 -> 문자

    str_to_number = {"ZRO" : 0,}
    number_to_str = {0: "ZRO",}