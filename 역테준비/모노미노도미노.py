import sys
sys.stdin = open("모노미노도미노_input.txt")
input = sys.stdin.readline

N = int(input())

score = 0
table = [[0 for _ in range(10)] for _ in range(10)]

for time in range(N):
    t, x, y = map(int, input().split())
    print(time+1, t, x, y, score)

    # down
    if t == 1:
        table[x][y] = 1
        sx, sy = x, y

    elif t == 2:
        table[x][y] = 2
        table[x][y+1] = 2
        sx = x
        sy = [y, y + 1]

    else:
        table[x][y] = 3
        table[x+1][y] = 3
        sx, sy = x+1, y

    while True:
        nx = sx + 1
        if nx >= 10: break

        if t == 1:
            if table[nx][sy]: break

            table[sx][sy] = 0
            table[nx][sy] = 1

        elif t == 2:
            if table[nx][sy[0]] or table[nx][sy[1]]: break

            table[sx][sy[0]] = 0
            table[sx][sy[1]] = 0

            table[nx][sy[0]] = 2
            table[nx][sy[1]] = 2

        else:
            if table[nx][sy]: break

            table[sx-1][sy] = 0
            table[nx][sy] = 3

        sx = nx

    while True:
        for g in table:
            print(g)
        print()
        # 4칸 겹치는지 체크
        deleteRows = []
        for i in range(4, 10):
            cnt = 0
            for j in range(4):
                if table[i][j]: cnt += 1

            if cnt == 4:
                deleteRows.append(i)
        # 겹치는 행 터트리기
        if deleteRows == []: break
        for row in deleteRows:
            score += 1

            # 몇 칸을 내려갈지가 아닌 블록이나 바닥에
            # 닿을 때까지로 코드 수정 후
            # 22 블록은 두블록이 한 덩어리로 같이 행동해야 한다.

            ## 수정필요
            j = 0

            while j < 4:
                # 몇 칸을 내려갈지 세 주자
                cnt = 1
                for i in range(row + 1, 10):
                    if table[i][j]: break
                    cnt += 1
                # print(j, cnt)
                # for g in table:
                #     print(g)
                # print()

                flag = False
                for i in range(row + cnt - 1, 3, -1):
                    if table[i - cnt][j] == 2:
                        table[i]

                    table[i][j] = table[i - cnt][j]
                    if table[i][j] == 2:
                        table[i][j+1] = table[i - cnt][j+1]
                        flag = True

                if flag:
                    j += 2
                else:
                    j += 1

    # 0행 1행에 블록이 있으면 맨밑행을 삭제
    cnt = 0
    for i in range(4, 6):
        for j in range(4):
            if table[i][j]:
                cnt += 1
                break

    if cnt:
        for i in range(9, 3, -1):
            for j in range(4):
                table[i][j] = table[i-cnt][j]





    # right
    if t == 1:
        table[x][y] = 1
        sx, sy = x, y

    elif t == 2: # down의 3와 로직 비슷
        table[x][y] = 2
        table[x][y+1] = 2
        sx, sy = x, y+1

    else: # down의 2와 로직 비슷
        table[x][y] = 3
        table[x+1][y] = 3
        sy = y
        sx = [x, x+1]

    while True:
        ny = sy + 1
        if ny >= 10: break

        if t == 1:
            if table[sx][ny]: break

            table[sx][sy] = 0
            table[sx][ny] = 1

        elif t == 2:
            if table[sx][ny]: break

            table[sx][sy-1] = 0
            table[sx][ny] = 2

        else:
            if table[sx[0]][ny] or table[sx[1]][ny]: break

            table[sx[0]][sy] = 0
            table[sx[1]][sy] = 0

            table[sx[0]][ny] = 3
            table[sx[1]][ny] = 3

        sy = ny
        # for g in table:
        #     print(g)
        # print()

    while True:
        # 4칸 겹치는지 체크
        deleteCols = []
        for j in range(4, 10):
            cnt = 0
            for i in range(4):
                if table[i][j]: cnt += 1

            if cnt == 4:
                deleteCols.append(j)

        # 겹치는 행 터트리기
        if deleteCols == []: break
        for col in deleteCols:
            score += 1
            i = 0
            while i < 4:
                # 몇 칸을 내려갈지 세 주자
                cnt = 1
                for j in range(col + 1, 10):
                    if table[i][j]: break
                    cnt += 1

                flag = False
                for j in range(col + cnt - 1, 3, -1):
                    table[i][j] = table[i][j - cnt]
                    if table[i][j] == 2:
                        table[i + 1][j] = table[i + 1][j - cnt]
                        flag = True

                if flag:
                    i += 2
                else:
                    i += 1


    # 0행 1행에 블록이 있으면 맨밑행을 삭제
    cnt = 0
    for j in range(4, 6):
        for i in range(4):
            if table[i][j]:
                cnt += 1
                break

    if cnt:
        for j in range(9, 3, -1):
            for i in range(4):
                table[i][j] = table[i][j-cnt]

    for g in table:
        print(g)
    print()

totBlock = 0
for i in range(10):
    for j in range(10):
        if table[i][j]: totBlock += 1

for g in table:
    print(g)
print()

print(score)
print(totBlock)