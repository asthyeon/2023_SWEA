import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 정수의 개수: N
    N = int(input())
    # N 개의 정수: arr
    arr = list(map(int, input().split()))

    # 특별한 정렬을 할 리스트 생성
    special_list = [0] * N

    # 오름차순으로 선정렬
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 인덱스에 숫자 넣기
    # 인덱스는 0부터 시작
    idx = -1
    while idx < (N - 1):
        idx += 1
        # 만약 인덱스가 짝수라면
        if idx % 2 == 0:
            # 뒤에서부터 가운데까지 넣기
            special_list[idx] = arr[N - 1 - (idx // 2)]
        # 만약 인덱스가 홀수라면
        else:
            # 앞에서부터 가운데까지 넣기
            special_list[idx] = arr[idx // 2]

    print(f'#{tc}', *(special_list[:10]))
