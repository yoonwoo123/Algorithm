def perm(n, r, q): # n = 주사위라면 전체경우의수 6, r = 뽑으려는 개수, q = r이랑같은 출력용
    if r== 0:
        while q != 0:
            q = q - 1
            print(t[q], end=" ")
        print()
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1] , a[i]
            t[r-1] = a[n-1]
            perm(n-1, r-1, q)
            a[i], a[n-1] = a[n-1], a[i]
N = 6
a = [n for n in range(1, N+1)]
# print(a)
t = [0] * 3


perm(N, 3, 3)

