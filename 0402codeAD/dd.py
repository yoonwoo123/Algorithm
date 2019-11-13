import sys, itertools
sys.stdin = open("치킨배달2_input.txt")

def check():
    hap=0
    for i in range(HN):
        nmin=20*20
        for j in range(CN):
            if not chk[j]: continue
            nmin = min(nmin, dist[i][j])
        hap += nmin
    return hap

def DFS(no, cnt):
    global sol
    if cnt==M:
        hap = check()
        if hap<sol:sol=hap
        return
    if no>=CN: return
    chk[no]=1
    DFS(no+1, cnt+1)
    chk[no]=0
    DFS(no+1, cnt)

# main --------------------------------
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N) ]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            chicken.append((i,j))
        elif arr[i][j]==1:
            house.append((i, j))
CN = len(chicken)
HN = len(house)
dist =[[0]*CN for _ in range(HN)]
chk = [0] * CN

for i in range(HN):
    for j in range(CN):
        dist[i][j] = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
        #print(dist[i][j], end=' ')
    #print(min(dist[i]))

sol=0x7fffffff
DFS(0, 0)
print(sol)