import sys
sys.stdin = open("네이버5_input.txt")

C, R = map(int, input().split()) # 가로 세로
ty, tx = map(int, input().split()) # 가로 세로

if tx < 0 or ty < 0 or tx >= R or ty >= C:
    print('fail')
else:
    print(tx + ty)
    table = [[0 for _ in range(ty+1)] for q in range(tx+1)]
    table[0][0] = 1
    # for g in table:
    #     print(g)
    # print()
    for x in range(tx+1):
        for y in range(ty+1):
            if y + 1 < ty+1:
                table[x][y+1] += table[x][y]
            if x + 1 < tx+1:
                table[x+1][y] += table[x][y]
    # for g in table:
    #     print(g)
    # print()
    print(table[tx][ty])
