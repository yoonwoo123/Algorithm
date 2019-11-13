import sys, collections
sys.stdin = open("테이프_input.txt")
# 조합을 써야함.

def comb(n, r): # n 개의 수중 r개의 조합을 뽑는다.
    global my_min
    if r == 0:
        res = abs(sum(T) * 2 - sum(A))
        if my_min > res:
            my_min = res
        # print(abs(sum(T) * 2 - sum(A)))
        # print(T)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1] # 빈상자에 바꿀것을 채움
        comb(n-1, r-1) # n-1, r-1
        comb(n-1, r) # n-1, r
# T = [0] * 2 # r개의 조합을 담을 상자
# A = [1, 2, 3] # n 개의 구슬
# comb(3, 2)

N = int(input())
A = list(map(int, input().split()))
T = [0] * int(N//2)
my_min = 99999999999999
comb(N, N//2)
print(my_min)




