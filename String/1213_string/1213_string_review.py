import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for _ in range(10):
    tc = int(input())
    fs = input()
    s = input()
    cnt = 0
    for i in range(len(fs), len(s)):
        if s[i-len(fs):i] == fs:
            cnt += 1

    print(f'#{tc}', cnt)