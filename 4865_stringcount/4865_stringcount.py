import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # str1 문자열
    str1 = input()
    # str2 문자열
    str2 = input()

    # 첫 문자열이 두 번째에 존재하는지 확인
    if str1 in str2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')