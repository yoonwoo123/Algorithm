import sys, heapq
sys.stdin = open("드래곤커브_input.txt")

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
table = [[0] * 101 for _ in range(101)]

N = int(input())
for _ in range(N):
    y, x, d, g = map(int, input().split())
    nx, ny = x + dx[d], y + dy[d]
    tmp = [(x, y), (nx, ny)] # 드래곤커브를 만들며 좌표 저장
    table[x][y], table[nx][ny] = 1, 1 # table에 좌표들 전부 남기기
    for cnt in range(g): # 세대수 만큼 반복
        sx, sy = tmp[-1][0], tmp[-1][1] # 기준점은 tmp의 마지막좌표
        LT = len(tmp)
        for i in range(LT-2, -1, -1):
            x, y = tmp[i][0], tmp[i][1] # 바뀌기 전 좌표
            nx, ny = sx - (sy - y), sy + (sx - x) # 바뀐 후 90도 이동 좌표
            table[nx][ny] = 1
            tmp.append((nx, ny))

answer = 0
for x in range(100): # 찾을 때는 1칸 덜찾아야 index 에러 안뜸 주의!
    for y in range(100):
        if table[x][y] and table[x+1][y] and table[x][y+1] and table[x+1][y+1]:
            answer += 1
print(answer)