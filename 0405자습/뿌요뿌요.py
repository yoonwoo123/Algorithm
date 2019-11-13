
def find(r, c, ch):
    dr =(-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    chk=[[0]*C for _ in range(R)]
    rec=[(r,c)]
    que=[(r, c)]
    chk[r][c]=1
    cnt=1
    while que:
        r, c = que.pop(0)
        for i in range(4):
            nr = r+ dr[i]
            nc = c+dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C: continue
            if arr[nr][nc]==ch and chk[nr][nc]==0:
                cnt+=1
                rec.append((nr, nc))
                que.append((nr, nc))
                chk[nr][nc]=1
    if cnt >= 4:
        for i in range(cnt):
            arr[rec[i][0]][rec[i][1]]='.'
        return 1
    else: return 0

def down():
    for j in range(C):
        tmp = []
        Pflag, Cflag= 0, 0
        for i in range(R-1, -1, -1):
            if arr[i][j]=='.' : continue
            else:
                tmp.append(arr[i][j])
                arr[i][j]='.'

        for i in range(len(tmp)):
            arr[R-1-i][j]=tmp[i]

def disp():
    for i in range(R):
        print(arr[i])
#main ----------------------------------
# T = int(input())
# for ti in range(T):
R, C = 12, 6
arr = []
for i in range(R):
    arr.append(list(input()))
sol = 0
while True:
    flag=0
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if arr[i][j] == '.': continue
            if find(i, j, arr[i][j]) : flag=1
    if flag:
        sol+=1
        down()
    else: break

print(sol)

