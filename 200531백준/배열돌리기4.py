import sys, itertools, copy
sys.stdin = open("배열돌리기4_input.txt")
input = sys.stdin.readline

def rotate(sx, sy, ex, ey):

    x, y = sx, sy
    tmp = table[x][y]

    while y + 1 < ey: # right
        table[x][y + 1], tmp = tmp, table[x][y + 1]
        y += 1

    # down
    while x + 1 < ex:
        table[x + 1][y], tmp = tmp, table[x + 1][y]
        x += 1

    # left
    while y - 1 >= sy:
        table[x][y - 1], tmp = tmp, table[x][y - 1]
        y -= 1

    # up
    while x - 1 >= sx:
        table[x - 1][y], tmp = tmp, table[x - 1][y]
        x -= 1


N, M, K = map(int, input().split())
table = [list(map(int, input().strip().split())) for _ in range(N)]
ori = copy.deepcopy(table)
cmds = [list(map(int, input().strip().split())) for _ in range(K)]

ans = 10000
for perm in itertools.permutations(cmds, K):
    # print(perm)
    for r, c, s in perm:
        # 배열돌리는 함수는 s번만 실행하면 된다.
        sx, sy = r-s-1, c-s-1
        ex, ey = r+s, c+s
        for i in range(s):
            rotate(sx+i, sy+i, ex-i, ey-i)
    for row in table:
        # print(row)
        ans = min(ans, sum(row))
    # print()
    table = copy.deepcopy(ori)
print(ans)