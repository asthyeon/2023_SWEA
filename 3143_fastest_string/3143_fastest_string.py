import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 전체 문자 A, 타이핑할 문자 B
    A, B = input().split()
    
    # # 내장함수 사용하는 방법
    # # A 문자 내의 B 문자를 1 글자로 치환하기
    # replace_A = A.replace(B, 'A')
    # 
    # # 치환한 문자열의 길이 출력
    # print(f'#{tc} {len(replace_A)}')

    # A 문자 길이
    A_len = len(A)
    # B 문자 길이
    B_len = len(B)
    # 기존 타이핑해야하는 횟수
    count = A_len
    
    # while 문에 쓸 인덱스 0 값: i
    i = 0
    # A_len - B_len 만큼 반복
    while i <= A_len - B_len:
        # 만약 B 문자가 A 문자에 있다면
        if B[:B_len] == A[i:i + B_len]:
            # 같은 부분만큼 건너뛰고
            # 건너뛰지 않으면 같은 문자가 중복될 경우 중복 카운트 됨
            i += B_len
            # B 문자를 1 개의 글자로 취급하고 카운트를 빼주기
            count -= (B_len - 1)
        # 없다면 1 칸 이동
        else:
            i += 1

    # 치환한 문자열의 길이 출력
    print(f'#{tc} {count}')
