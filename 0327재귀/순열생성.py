def perm(n, k):
    global cnt, to
    if n-1 == k:
        print(a)
        cnt += 1
    else:
        for i in range(k, n): # k = depth, n = 찾고자 하는 갯수
            to += 1
            a[i], a[k] = a[k], a[i]
            perm(n, k+1) # depth =  k+1
            a[i], a[k] = a[k], a[i] # 원래 값으로 복귀

def pperm(n, r): # n= 3, r = 0 # n은 구하고자하는 수 , r = 0 부터 올라감
    global final, result, cnt

    if r == n-1:
        print(spos)
        cnt += 1
    else:
        for i in range(r, n): # 0,1,2
            spos[i], spos[r] = spos[r], spos[i]
            pperm(n , r + 1)
            spos[i], spos[r] = spos[r], spos[i]

to = 0
cnt = 0
flag = 0
a = [1, 2, 3, 4, 5, 6, 7]
perm(7, 0)
print(cnt)
print(to)