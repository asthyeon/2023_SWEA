# 재귀함수

list = []

def fibo(n):
    if n < 2:
        list.append(n)
        return n
    else:
        list.append(n)
        return fibo(n - 1) + fibo(n - 2)

fibo(5)
print(list)