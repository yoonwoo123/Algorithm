import sys
sys.stdin = open("사냥꾼_input.txt")

N = int(input())
table = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 8방향 12시부터 시계방향순
dy = [0, 1, 1, 1, 0, -1, -1, -1]
# 0돌 1 사냥꾼 2 토끼
# 잡은 토끼는 2로 놔두면 안되고 잡았다고 표시를 해줘야함
for i in range(N):
    table.append(list(map(int, list(input()))))
rabbit = 0
for x in range(N):
    for y in range(N):
        if table[x][y] == 1:
            for i in range(8):
                if x + dx[i] > N-1 or x + dx[i] < 0 or x + dx[i] > N-1 or x + dx[i] < 0:
                    continue
                if table[x + dx[i]][y + dy[i]] == 2 or table[x + dx[i]][y + dy[i]] == 3:
                    if table[x + dx[i]][y + dy[i]] == 2:
                        rabbit += 1
                    table[x + dx[i]][y + dy[i]] = 3 # 잡은토끼인것을 표시
                    nx = x + dx[i]
                    ny = y + dy[i]

                    while True:
                        if nx + dx[i] > N-1 or nx + dx[i] < 0 or ny + dy[i] > N-1 or ny + dy[i] < 0:
                            break
                        nx += dx[i]
                        ny += dy[i]
                        if table[nx][ny] == 2:
                            rabbit += 1
                            table[nx][ny] = 3
                        if table[nx][ny] == 3:
                            continue
                        if table[nx][ny] == 0 or table[nx][ny] == 1:
                            break
print(rabbit)


