import sys, itertools
sys.stdin = open("바이러스_input.txt")

def FF(no):
    # 현재 컴퓨터에서 연결되어 있고 감염안된 컴퓨터를 감염시키면서 카운트
    global sol
    for i in range(1, com+1):
        if arr[no][i] and chk[i] == 0:
            chk[i] = 1
            sol += 1
            FF(i)

com = int(input())
N = int(input())

sol = 0
arr = [[0 for _ in range(com+1)] for _ in range(com+1)] # 0부터 시작하므로 +1
chk = [0] * (com + 1) # 0부터 시작하므로 +1
for i in range(N):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

chk[1] = 1
FF(1)
print(sol)