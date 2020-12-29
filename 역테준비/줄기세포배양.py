import sys
sys.stdin = open("줄기세포배양_input.txt")

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
tc = int(input())
for T in range(1, tc+1):
    N, M, K = map(int, input().split())
    states = [list(map(int, input().split())) for _ in range(N)]

    tLen = max(N, M) + 2 * K
    # 생명력, cnt, state (0 죽음 1 활성 2 비활성)
    table = [[[0 for _ in range(3)] for _ in range(tLen)] for _ in range(tLen)]
    cellPos = {}

    for x in range(tLen // 2, tLen // 2 + len(states)):
        for y in range(tLen // 2, tLen //2 + len(states[0])):
            if states[x - tLen // 2][y - tLen // 2]:
                cellPos[(x, y)] = states[x - tLen // 2][y - tLen // 2]

            table[x][y][0] = states[x - tLen // 2][y - tLen // 2]
            table[x][y][2] = 2

    for _ in range(K):
        deadCell = []
        extendPos = {}
        for pos, life in cellPos.items():
            x, y = pos
            # 0 : life, 1 : cnt, 2 : state
            if table[x][y][2] == 2:
                table[x][y][1] += 1
                if table[x][y][0] == table[x][y][1]:
                    table[x][y][2] -= 1
                    table[x][y][1] = 0

            elif table[x][y][2] == 1:
                # 4방향 복제
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= N or ny >= M or table[nx][ny][0]: continue
                    if (nx, ny) not in extendPos:
                        extendPos[(nx, ny)] = table[x][y][0]

                    else:
                        extendPos[(nx, ny)] = max(extendPos[(nx, ny)], table[x][y][0])
                print('ext', extendPos)

                table[x][y][1] += 1
                if table[x][y][0] == table[x][y][1]:
                    table[x][y][2] -= 1
                    # 죽었는 지 life와 비교해서 체크
                    # 체크해서 죽었다면 deadCell 에 좌표 넣어서 나중에 일괄 pop
                    if table[x][y][2] == 0:
                        deadCell.append((x, y))
                    table[x][y][1] = 0

        for pos, life in extendPos.items():
            x, y = pos
            table[x][y] = [life, 0, 2]
            cellPos[(x, y)] = life

        for pos in deadCell:
            cellPos.pop(pos)

        for g in table:
            print(g)
        print()
        print(cellPos)

    print(len(cellPos))
    # for g in table:
    #     print(g)
    # print()

    print({cellPos}.format())
