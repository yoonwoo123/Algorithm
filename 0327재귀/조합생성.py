def comb(n, r): # n 개의 수중 r개의 조합을 뽑는다.
    if r == 0:
        print(T)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
T = [0] * 3 # r개의 조합을 담을 상자
A = [1, 2, 3, 4] # n 개의 구슬
comb(4, 3)