arr = [1, 4, 2, 7, 3, 6]
N = 6

# 버블 정렬
for i in range(N - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)