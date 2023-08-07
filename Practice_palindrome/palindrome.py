import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N x N 글자판, 길이가 M 인 회문 찾기
    N, M = map(int, input().split())

    # 빈 리스트 형성
    arr = []
    # 문자열 형성
    for i in range(N):
        arr.append(input().split())

    # 회문 찾기
    # 행 우선 순회
    for r1 in range(N):
        for c1 in range(N - M + 1):
            # 맞는 글자 수 집어넣기
            string = ''
            # 글자 길이 수 만큼 반복
            for cc1 in range(c1, M + c1):
                # 맨 앞 글자와 맨 뒷 글자가 같다면
                if arr[r1][0][cc1] == arr[r1][0][M + (c1 * 2) - 1 - cc1]:
                    string += arr[r1][0][cc1]
            # 글자를 넣은 길이가 M과 같다면
            if len(string) == M:
                print(f'#{tc} {string}')
    # 열 우선 순회
    for c2 in range(N):
        for r2 in range(N - M + 1):
            # 맞는 글자 수 집어넣기
            string = ''
            for rr2 in range(r2, M + r2):
                if arr[rr2][0][c2] == arr[M + (r2 * 2) - 1 - rr2][0][c2]:
                    string += arr[rr2][0][c2]
            if len(string) == M:
                print(f'#{tc} {string}')