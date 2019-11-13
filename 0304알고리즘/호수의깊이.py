import sys
sys.stdin = open("호수의깊이_input.txt")

N = int(input())
res = 0
table = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    line = list(map(int, list(input().split())))
    table.append(line)

for x in range(1, N-1):
    for y in range(1, N-1):
        if table[x][y] == 1: # 물이라면 들어가자
            depth = []

            for i in range(4):
                nx = x # x의 좌표값을 nx에 저장
                ny = y # y의 좌표값을 ny에 저장
                num = 0
                if table[x + dx[i]][y + dy[i]] == 0: # 1 번 검색만에 0이 나오면 1넣고 브레이크
                    depth.append(1)
                    break
                for n in range(N):
                    nx += dx[i]
                    ny += dy[i]

                    if table[nx][ny] != 0:
                        num += 1
                    else:
                        break
                depth.append(num + 1)
            table[x][y] = min(depth)
for x in range(1, N-1):
    for y in range(1, N-1):
        res += table[x][y]
print(res)
# for i in range(N):
#     print(table[i])