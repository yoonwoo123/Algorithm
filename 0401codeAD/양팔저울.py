import sys
sys.stdin = open("양팔저울_input.txt")

def DFS(no, Lsum, Rsum):
    global sol
    # 현재 추를 사용(왼, 오른쪽저울) 하거나 사용하지 않는 경우의 수

    # if Lsum < Rsum:
    #     return
    if no >= CN:
        if Lsum == Rsum:
            sol = 1
        return
    if abs(Lsum - Rsum) > tot[no]: # 가지치기: 양쪽저울의 차보다 남은 추가 부족하면
        return
    else:
        rec[no] = 0
        DFS(no + 1, Lsum, Rsum)
        rec[no] = 1
        DFS(no +1, Lsum + choos[no], Rsum)
        rec[no] = 2
        DFS(no + 1, Lsum, Rsum + choos[no])

CN = int(input())
choos = list(map(int, input().split()))
# print(sum(choos[1:CN]))
BN = int(input())
balls = list(map(int, input().split()))
rec = [0] * CN
tot = [0] * CN
for i in range(CN):
    tot[i] = sum(choos[i:CN])
# print(tot)
# 추로 만들 수 있는 모든 경우의 수를 계산하자 그래서 구슬이 그만든 값안에 있으면 Y 아니면 N
for i in range(BN):
    sol = 0
    DFS(0, balls[i], 0) # 0번추부터 시작, 왼쪽저울에 구슬값으로, 오른쪽저울 0
    if sol: print('Y', end=" ")
    else: print('N', end=" ")
