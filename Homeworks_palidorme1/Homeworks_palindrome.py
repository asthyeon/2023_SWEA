import sys
sys.stdin = open('input.txt')

# 10 개의 테스트 케이스
for i in range(1, 11):
    # 찾아야 하는 회문의 길이
    N = int(input())

    # 글자판 형성
    arr = [input() for _ in range(8)]

    # 회문 수
    count = 0

    # 행 회문 찾기
    for x1 in range(8):
        for y1 in range(8 - N + 1):
            # 첫 항은 끝나는 인덱스 값이 -1이 성립이 되지 않으므로 따로 구현
            if y1 == 0:
                if arr[x1][y1:y1 + N] == arr[x1][y1 + N - 1::-1]:
                    count += 1
            # 그 외의 항은 거꾸로 만들었을 때 문자와 같으면 count += 1
            else:
                if arr[x1][y1:y1 + N] == arr[x1][y1 + N - 1:y1 - 1:-1]:
                    count += 1

    # 열 회문 찾기
    for y2 in range(8):
        for x2 in range(8 - N + 1):
            # string 이라는 문자열 변수를 구현하여 처음과 끝의 문자가 같으면 넣기
            string = ''
            for xx2 in range(x2, N + x2):
                if arr[xx2][y2] == arr[N - xx2 - 1 + (x2 * 2)][y2]:
                    string += arr[xx2][y2]
            # string 이 N 과 같다면 count + 1
            if len(string) == N:
                count += 1

    print(f'#{i} {count}')