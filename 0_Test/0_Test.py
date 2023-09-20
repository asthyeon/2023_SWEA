import sys
sys.stdin = open('input.txt')

func = [lambda x: x + 1, lambda x: x - 1, lambda x: x * 2, lambda x: x - 10]

for t in range(int(input())):
    begin, end = map(int, input().split())
    cnt, stack, found, checked = 0, [begin], False, [True] * 1000001
    while stack:
        cnt += 1
        field = {}
        for begin in stack:
            for f in func:
                temp = f(begin)
                if temp > 10 ** 6 or temp < 1:
                    continue
                elif temp == end:
                    found = True
                    break
                else:
                    if field.get(temp) is None and checked[temp]:
                        field[temp] = True
                        checked[temp] = False
        if found:
            break
        else:
            stack = list(field.keys())
    print("#{} {}".format(t + 1, cnt))
