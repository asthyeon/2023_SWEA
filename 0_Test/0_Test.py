structure = {
    0:'0',
        1:'╈',
        2:'┃',
        3:'━',
        4:'┗',
        5:'┏',
        6:'┐',
        7:'┛'
}
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        for j in range(M):
            print(structure[arr[i][j]],end=' ')
        print()