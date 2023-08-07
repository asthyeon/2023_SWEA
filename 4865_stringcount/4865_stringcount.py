import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # str1 문자열
    str1 = input()
    # str2 문자열
    str2 = input()

    # 빈 딕셔너리 형성
    str_dict = {}

    # 문자를 하나씩 쪼개서 딕셔너리에 넣기
    for i in str1:
        str_dict[i] = 0

    # str2 문자에 str1 글자 하나씩이 있을 경우
    for j in str2:
        if j in str_dict:
            str_dict[j] += 1

    # 제일 큰 수 출력하기
    max_str = 0
    for k in str_dict:
        if max_str < str_dict[k]:
            max_str = str_dict[k]

    print(f'#{tc} {max_str}')