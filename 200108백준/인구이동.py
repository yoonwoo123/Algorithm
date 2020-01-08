import sys, collections
sys.stdin = open("인구이동_input.txt")
sys.setrecursionlimit(10000)

def DFS(x, y, tmp, visit):
    # global tot
    visit[x][y] = True
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)): # 시간복잡도 매우 줄여줌!!!
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        if L <= abs(table[x][y] - table[nx][ny]) <= R and visit[nx][ny] == 0:
            tmp.append((nx, ny))
            # tot += table[nx][ny]
            DFS(nx, ny, tmp, visit)

N, L, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
# for g in table:
#     print(g)
# print()

answer = 0 # 인구이동 횟수
# 여기서부터 반복 while
while True:
    visit = [[False] * N for q in range(N)]
    groups = False # 그룹의 개수 만약 0이라면 answer를 답으로 출력
    for idx in range(N):
        for idy in range(N):
            if visit[idx][idy] == 0:
                # tot = 0
                tmp = [(idx, idy)]  # 임시로 그룹별 좌표들 보관 만약 tmp 길이가 1이라면 groups에 저장x
                DFS(idx, idy, tmp, visit) # groups 를 인자에 넣어줘야할듯
                # print(tmp)
                if len(tmp) > 1:
                    groups = True
                    # print(tmp)
                    avg = sum([table[x][y] for x, y in tmp]) // len(tmp)
                    # avg = tot // Le
                    # print(avg)
                    for x, y in tmp:
                        table[x][y] = avg
    if groups == False: break
    answer += 1

    # for g in table:
    #     print(g)
    # print()
print(answer)