import sys
sys.stdin = open("폭죽쇼_input.txt")

# n, c = map(int,input().split())
# t = [0] * c
# x = {int(input()) for _ in range(n)}
# if 1 in x:
#     print(c)
#     quit()
# for i in x:
#     t[i-1::i] = [1] * (c//i)
# print(sum(t))

def sol():
    dic = set()
    for i in range(N):
        btime = int(input())
        if btime == 1:
            print(C)
            return
        cnt = 1
        while btime * cnt <= C:
            dic.add(btime * cnt)
            cnt += 1
    print(len(dic))

N, C = map(int, input().split())
sol()