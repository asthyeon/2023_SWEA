import sys
sys.stdin = open('input.txt')

def check():
    count = 0 # 몇 군데 들어갈 수 있냐?
    for r in range(N):
        s_list = ''.join(data[r]).split('0')
        print(s_list)
        count += sum([len(s) == K for s in s_list])

        # for s in s_list:
        #     if len(s) == K:
        #         count += 1

        for c in range(N):
            s_list = ''.join([data[r][c] for r in range(N)].split('0')
            count += sum([len(s) == K for s in s_list])

    return count

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().rstrip().split())
    data = [input().rstrip().split() for _ in range(N)]
    print(f'#{tc} {check()}')