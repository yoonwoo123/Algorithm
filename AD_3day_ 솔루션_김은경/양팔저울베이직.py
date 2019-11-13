import sys
sys.stdin = open("input.txt")


def DFS(no, lsum, rsum):
    global flag
    if no >= CN:
        if lsum == rsum: flag = 1
        return
    if flag: return
    temp = abs(lsum - rsum)
    if temp > tot[no]: return # 가지치기 : 양쪽저울의 차보다 남은 추가 부족하면
    DFS(no + 1, lsum + Carr[no], rsum)
    DFS(no + 1, lsum, rsum + Carr[no])
    DFS(no + 1, lsum, rsum)
# main ===============================
flag = 0
CN = int(input())
Carr = list(map(int, input().split()))
BN = int(input())
Barr = list(map(int, input().split()))
tot = [0] * (CN)
for i in range(CN): # 내 뒤로 모든 추 합계(잔량)
    tot[i] = sum( Carr[i:CN])

for i in range(BN):
    flag = 0
    DFS(0, Barr[i], 0)
    if flag:
        print("Y", end=' ')
    else:
        print("N", end=' ')
