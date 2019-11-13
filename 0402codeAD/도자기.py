import sys, itertools
sys.stdin = open("도자기_input.txt")

def DFS(no, start): # 지역변수 backup 을 이용한 방법
    global sol
    if no >= M:
        for i in range(no):
            print(rec[i], end=" ")
        print()
        sol += 1
        return
    else:
        backup = 0
        for i in range(start, N):
            if backup == soil[i]: continue
            rec[no] = soil[i]
            backup = soil[i]
            DFS(no + 1, i+1) # start가 아닌 i+1

# count로 세서 하기

tc = int(input())
for T in range(1, tc+1):
    N, M = map(int, input().split())
    soil = list(map(int, input().split()))
    soil.sort()
    sol = 0
    rec = [0] * N # 기록을 위한 리스트
    DFS(0, 0)
    print(sol)