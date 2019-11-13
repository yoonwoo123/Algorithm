import sys
sys.stdin = open('연산_input.txt')

def BFS():
    global sol
    que = []
    que.append(N)
    cnt = 0
    while que:
        n = que.pop(0)
        cnt = chk[n]
        # cnt += 1
        if n == M:
            sol = chk[M]
            return
        fx[0] = n + 1
        fx[1] = n - 1
        fx[2] = n - 10
        fx[3] = n * 2
        for i in range(4):
            if 0 < fx[i] <= M+20 and chk[fx[i]] == 0:
                chk[fx[i]] = cnt + 1
                que.append(fx[i])

fx = [0] * 4

tc = int(input())
for T in range(1, tc+1):
    N, M = map(int, input().split())
    chk = [0] * (M+21)
    sol = 0
    BFS()
    print('#%d %d' %( T, sol))