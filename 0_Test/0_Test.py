# 거듭제곱(분할정복 알고리즘 활용)

def f1(b, e) : # base, exponent
    global cnt1
    if b == 0 :
        return 1
    r = 1
    for i in range(e) :
        r *= b
        cnt1 += 1
    return r

def f2(b, e) :
    global cnt2
    if b == 0 or e == 0 :
        return 1
    if e % 2 :  # 홀수라면
        r = f2(b, (e-1)//2)
        cnt2 += 1
        return r * r* b #(자기자신끼리 곱한 것 * base)
    else :
        cnt2 += 1
        r = f2(b, e//2)
        return r*r
cnt1 = cnt2= 0
print(f1(2, 20), cnt1)
print(f2(2, 20), cnt2)