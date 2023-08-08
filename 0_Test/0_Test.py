import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split()) # N: 문자판의 크기, M:회문의 길이
    string_arr = []
    for _ in range(N) :
        row = list(input())
        string_arr.append(row)
    # 가로 탐색
    for r in range(N) :
        for c in range(N-M+1) :
            tmp = string_arr[r][c:c+M]
            n = 0
            ans = 0
            while n <= len(tmp)//2 :
                start = n
                end = len(tmp)-1-n
                n += 1
                if tmp[start] != tmp[end] :
                    ans = 0
                    break
                else :
                    ans = 1
                    continue
            if ans == 1:
                print(f'#{tc}', end=' ')
                result = ''.join(t for t in tmp)
                print(result)
                break
        if ans == 1:
            break
    # 세로 탐색
    if ans != 1:
        for c in range(N) :
            for r in range(N-M+1) :
                tmp = []
                for tr in range(M) :
                    tmp.append(string_arr[tr][c])
                n = 0
                ans = 0
                while n <= len(tmp)//2 :
                    start = n
                    end = len(tmp)-1-n
                    n += 1
                    if tmp[start] != tmp[end] :
                        ans = 0
                        break
                    else :
                        ans = 1
                        continue
                if ans == 1:
                    print(f'#{tc}', end=' ')
                    result = ''.join(t for t in tmp)
                    print(result)
                    break
            if ans == 1:
                break
    else :
        continue