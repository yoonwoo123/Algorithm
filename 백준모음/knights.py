import sys
sys.stdin = open("knights_input.txt")

def DFS(dep, tot):
    global res


    for x in range(N):
        for y in range(N):
            if table[x][y] == 0:
                table[x][y] = -1
                sx, sy = x, y
                cnt = 0
                tmp = []
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
                    if table[nx][ny] == -1: continue
                    else:
                        table[nx][ny] += 1 # 복구해야함
                        tmp.append([nx, ny])
                        cnt += 1
                if x != N and y != N:
                    DFS(dep + 1, tot + cnt)
                    for t in tmp:
                        table[t[0]][t[1]] -= 1 # 복구해줌
                else:
                    if res < tot:
                        res = tot
                    return




dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

N = int(input())
table = [[0 for _ in range(N)] for q in range(N)]
res = -1

DFS(0, 0)
print(res)