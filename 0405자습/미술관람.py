import sys
sys.stdin = open("미술관람_input.txt")
# R = 1, G = 2, B = 3
def BFS(x, y, color):
    global sol
    que = []
    que.append([x, y, color])
    arr[x][y] = 'V'
    while que:
        x, y, color = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] == color:
                arr[nx][ny] = 'V'
                que.append([nx, ny, color])
    sol += 1

def BFS2(x, y, color):
    global sol2
    que = []
    que.append([x, y, color])
    arr2[x][y] = 'V'
    while que:
        x, y, color = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr2[nx][ny] == color:
                arr2[nx][ny] = 'V'
                que.append([nx, ny, color])
    sol2 += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
arr = []
arr2 = [[0 for _ in range(N)] for _ in range(N)]

sol = 0
sol2 = 0
for i in range(N):
    arr.append(list(input()))
# print(arr[1][1])

for x in range(N):
    for y in range(N):
        if arr[x][y] == 'G':
            arr2[x][y] = 'R'
            continue
        arr2[x][y] = arr[x][y]
trash = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] == 'V': continue
        BFS(x, y, arr[x][y])

for x in range(N):
    for y in range(N):
        if arr2[x][y] == 'V': continue
        BFS2(x, y, arr2[x][y])
print(sol, end=" ")
print(sol2)
# for g in arr:
#     print(g)
# print()