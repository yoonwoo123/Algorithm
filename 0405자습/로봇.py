import sys
sys.stdin = open("in.txt")
def BFS():
    que=[]
    dr=(0, 0, 0, 1, -1) # 동서남북 1234
    dc=(0, 1, -1, 0, 0)
    turn =[(0, 0), (4,3), (3,4), (1,2), (2,1)] # 동서남북별 왼쪽턴, 오른쪽턴
    que.append((sr, sc, sdir, 0)) #1] 시작점 큐에저장(방문표시)
    chk[sdir][sr][sc]=1
    while que:
        r, c, dir, cnt=que.pop(0) #2] 큐에서 데이타 꺼내기
        if r==er and c==ec and dir==edir: return cnt
        for i in range(1, 4):# go 1,2,3별 시도하여 큐에저장(방문표시)
            nr = r+dr[ dir ]*i
            nc = c + dc[dir] * i
            if nr<0 or nr>=R or nc<0 or nc>=C: break
            if arr[nr][nc]: break # 벽이면 중단
            if chk[dir][nr][nc]: continue # 방문했으면 스킵
            que.append((nr, nc, dir, cnt+1))
            chk[dir][nr][nc]=1

        for i in range(2):# turn left, right 변 시도
            ndir = turn[dir][i]
            if chk[ndir][r][c]: continue
            que.append((r, c, ndir, cnt+1))
            chk[ndir][r][c]=1

#main--------------------------------------
R, C = map(int, input().split())
chk =[ [[0]*C for _ in range(R)] for _ in range(5)] # 동서남북1234면에 방문표시
arr = [list(map(int, input().split())) for _ in range(R)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr, sc = sr-1, sc-1
er, ec = er-1, ec-1
print(BFS())
