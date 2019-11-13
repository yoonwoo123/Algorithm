import sys
sys.stdin = open("in.txt")

from collections import deque

def DFS():
    que = deque()
    dr = [0, 0, 0, 1, -1]
    dc = [0, 1, -1, 0, 0]
    turn = [[0, 0], [4, 3], [3, 4], [1, 2], [2, 1]] # 동서남북 별 왼쪽 턴, 오른쪽 턴
    que.append([sr, sc, sdir, 0]) # 시작점 큐에 저장(방문 표시)
    chk[sdir][sr][sc] = 1
    # 면, 행, 열
    while que:
        r, c, dir, cnt = que.popleft() # 큐에서 데이터 꺼내기
        if r == er and c == ec and dir == edir: return cnt
        for i in range(1, 4): # go1, go2, go3별 시도하여 큐에 저장(방문 표시)
            nr = r + dr[dir]*i
            nc = c + dc[dir]*i
            # 조건 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C: break
            if arr[nr][nc] == 1: break # 벽이면 중단
            if chk[dir][nr][nc]: continue
            # go1을 방문 했어도 go2, go3은 실행해야하니까 continue
            que.append([nr, nc, dir, cnt+1])
            chk[dir][nr][nc] = 1


        for i in range(2): # turn left, right
            ndir = turn[dir][i]
            if chk[ndir][r][c]: continue
            # 가 볼 방향과 내 자리 확인
            que.append([r, c, ndir, cnt+1])
            chk[ndir][r][c] = 1



R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
chk = [[[0]*C for _ in range(R)]for _ in range(5)]
print(DFS())