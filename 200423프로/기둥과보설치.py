
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
    answer = []
    table = [[[0, 0] for y in range(n+1)] for x in range(n+1)]
    for g in table:
        print(g)
    print(table[0][0])
    for y, x, a, b in build_frame:
        if b: # 설치
            if a == 0: # 기둥
                if x == 0 or table[x-1][y][0] or table[x][y][1] or (y - 1 >= 0 and table[x][y-1][1]):
                    table[x][y][a] = 1

            else: # 보
                if (x - 1 >= 0 and table[x-1][y][0]) or (x - 1 >= 0 and y + 1 < n + 1 and table[x-1][y+1]) or (y - 1 >= 0 and y + 1 < n + 1 and table[x][y-1][1] and table[x][y+1][1]):
                    table[x][y][a] = 1

        else: # 삭제
            if delete(x, y, a, table):
                table[x][y][a] = 0

    for g in table:
        print(g)
    print(table[0][0])
    for x in range(n+1):
        for y in range(n+1):
            for z in range(2):
                if table[x][y][z]:
                    answer.append([y, x, z])
    answer.sort()
    return answer

def delete(x, y, a, table):
    if a == 0:  # 기둥
        if table[x + 1][y][0] and table[x + 1][y][1] == 0 and (y - 1 >= 0 or table[x + 1][y-1][1] == 0): return False
        # 인덱스에러
        if table[x + 1][y][1] and table[x][y + 1][0] == 0 and (table[x + 1][y + 1][1] == 0 or table[x + 1][y - 1][1] == 0): return False
        if table[x + 1][y - 1][1] and table[x][y - 1][0] == 0 and (table[x + 1][y][1] == 0 or table[x + 1][y - 2][1] == 0): return False
        return True

    else:
        if table[x][y][0] and table[x - 1][y][0] == 0 and table[x][y - 1][1] == 0: return False
        if table[x][y + 1][0] and table[x - 1][y + 1][0] == 0 and table[x][y + 1][1] == 0: return False

        if table[x][y - 1][1] and table[x - 1][y][0] == 0 and table[x - 1][y - 1][0] == 0: return False
        if table[x][y + 1][1] and table[x][y + 1][0] == 0 and table[x][y + 2][0] == 0:return False
        return True

print(solution(n, build_frame))