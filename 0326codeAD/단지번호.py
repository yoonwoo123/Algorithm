import sys
sys.stdin = open("단지번호_input.txt")

def BFS(x, y):
    global N
    que = []
    que.append([x, y]) # 큐에 저장
    arr[x][y] = 0 # 방문처리
    house = 1 # 집의 개수
    while que: # 큐가 빌때까지 반복
        x, y = que.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] == 0:
                continue
            que.append([nx, ny])
            arr[nx][ny] = 0
            house += 1
    houses.append(house)
    return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

houses = []
BFScnt = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            BFS(x, y)
            BFScnt += 1 # 총 단지개수
print(BFScnt)
houses.sort()
for h in houses:
    print(h)