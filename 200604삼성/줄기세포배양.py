import sys
sys.stdin = open("줄기세포배양_input.txt")

# 줄기세포는 K시간동안 분열한다면 최소값인 1인 경우 2시간후면 2칸 확장한다.
# 따라서 최악의 경우 K시간동안 K칸 확장한다.
# 초기상태 N + K 칸의 정사각배열안에 다 들어간다.
# 맵을 다 탐색하기엔 너무 크므로 세포들만의 좌표를 cells라는 배열에 저장후
# 2는 비활성 1은 활성 0은 죽은 세포로 상태를 나타내자. 그래야 세기편하다
# cell은 각각 좌표값 x y와 con(2, 1, 0) 그리고 time(1~life)으로 구성
# time이 table[x][y]=life와 같아지면 con을 1 빼고 time을 0으로 만들게 구현하자.

# for 문을 돌다 시간 t가 K시간이 되면 바로 return하자
def solution():
    for t in range(K+1):
        if t == K:
            return
        die = [] # 죽은 세포의 인덱스값
        news = [] # 번식할 세포들의 좌표값들
        for i in range(len(cells)):
            # cells[i][2] = con
            # cells[i][3] = time
            if cells[i][2] == 2: # 비활성
                cells[i][3] += 1
                if table[cells[i][0]][cells[i][1]] == cells[i][3]:
                    cells[i][2] -= 1
                    cells[i][3] = 0
            elif cells[i][2] == 1: # 활성
                # 4방향으로 증식하는데 바로 하지 말고 좌표 저장후 비교
                # print(news)
                news.extend(expend(cells[i][0], cells[i][1]))

                cells[i][3] += 1
                if table[cells[i][0]][cells[i][1]] == cells[i][3]:
                    cells[i][2] -= 1
                    cells[i][3] = 0
                    die.append(i) # con이 1에서 0이 되면 죽은세포

        for i in range(len(die)): # 죽은세포 좌표들 pop
            cells.pop(die[i] - i)

        final = {}
        # news에 있는 좌표들 번식하기
        for i in range(len(news)):
            x, y, life = news[i]
            if table[x][y] == 0:
                table[x][y] = life
                final[(x, y)] = life
            else:
                if life > table[x][y]:
                    table[x][y] = life
                    final[(x, y)] = life # 더 큰걸로 최신화
        # cells에 좌표 넣어줘야 한다.
        for x, y in final.keys():
            cells.append([x, y, 2, 0])

def expend(x, y):
    arr = []
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        nx, ny = x + dx, y + dy
        if table[nx][ny] == 0: # 이미 있지만 않으면 번식가능
            arr.append([nx, ny, table[x][y]]) # x, y, life
    return arr

tc = int(input())
for T in range(1, tc+1):
    N, M, K = map(int, input().split())
    cells = []
    table = [[0 for _ in range(K+M)] for q in range(K+N)]
    # print(N, M, K)
    if N % 2 == 0:
        for i in range((N+K)//2 - N // 2, (N+K)//2 + N // 2):
            tmp = list(map(int, input().split()))
            if M % 2 == 0:
                for j in range((M+K)//2 - M // 2, (M+K)//2 + M // 2):
                    if tmp[j-((M+K)//2 - M // 2)]:
                        cells.append([i, j, 2, 0]) # x, y, con, time
                        table[i][j] = tmp[j-((M+K)//2 - M // 2)]
            else:
                for j in range((M + K) // 2 - M // 2, (M + K) // 2 + M // 2 + 1):
                    if tmp[j - ((M + K) // 2 - M // 2)]:
                        cells.append([i, j, 2, 0])  # x, y, con, time
                        table[i][j] = tmp[j - ((M + K) // 2 - M // 2)]
    else:
        for i in range((N+K)//2 - N // 2, (N+K)//2 + N // 2 + 1):
            tmp = list(map(int, input().split()))
            if M % 2 == 0:
                for j in range((M+K)//2 - M // 2, (M+K)//2 + M // 2):
                    if tmp[j-((M+K)//2 - M // 2)]:
                        cells.append([i, j, 2, 0]) # x, y, con, time
                        table[i][j] = tmp[j-((M+K)//2 - M // 2)]
            else:
                for j in range((M + K) // 2 - M // 2, (M + K) // 2 + M // 2 + 1):
                    if tmp[j - ((M + K) // 2 - M // 2)]:
                        cells.append([i, j, 2, 0])  # x, y, con, time
                        table[i][j] = tmp[j - ((M + K) // 2 - M // 2)]

    solution()
    print(f'#{T} {len(cells)}')