def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d " % (T[q]), end = "")
    print()
def comb(n, r):
    if r == 0:
        while q != 0:
            q = q - 1
            print(" %d " % (T[q]), end="")
        print()
        return
    elif n < r:
        return 0
    else:
        # T[r-1] = A[n-1]
        return comb(n-1, r-1) + comb(n-1, r)

print(comb(6, 4))
# print(12**2 * 48 * 49 * 50)