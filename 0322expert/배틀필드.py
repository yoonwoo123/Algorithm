import sys
sys.stdin = open("배틀필드_input.txt")

dx = [0, 0, -1, 1] # 좌우상하
dy = [-1, 1, 0, 0]

tc = int(input())
for T in range(1, tc+1):
    table = []
    H, W = map(int, input().split())
    for i in range(H):
        tmp = list(input())
        table.append(tmp)
        # print(tmp)
    # print()
    N = int(input())
    command = list(input())
    look = 0
    for x in range(H):
        for y in range(W):
            if table[x][y] == '<': # 0
                look = 0
                t_x = x
                t_y = y
                break
            elif table[x][y] == '>': # 1
                look = 1
                t_x = x
                t_y = y
                break
            elif table[x][y] == '^': # 2
                look = 2
                t_x = x
                t_y = y
                break
            elif table[x][y] == 'v': # 3
                look = 3
                t_x = x
                t_y = y
                break
    for i in range(N):
        if command[i] == 'L':
            look = 0
            table[t_x][t_y] = '<'
            if 0 <= t_x+dx[look] < H and 0 <= t_y+dy[look] < W:
                if table[t_x+dx[look]][t_y+dy[look]] == '.':
                    table[t_x + dx[look]][t_y + dy[look]] = '<'
                    table[t_x][t_y] = '.'
                    t_x = t_x + dx[look]
                    t_y = t_y + dy[look]
        elif command[i] == 'R':
            look = 1
            table[t_x][t_y] = '>'
            if 0 <= t_x + dx[look] < H and 0 <= t_y + dy[look] < W:
                if table[t_x + dx[look]][t_y + dy[look]] == '.':
                    table[t_x + dx[look]][t_y + dy[look]] = '>'
                    table[t_x][t_y] = '.'
                    t_x = t_x + dx[look]
                    t_y = t_y + dy[look]
        elif command[i] == 'U':
            look = 2
            table[t_x][t_y] = '^'
            if 0 <= t_x + dx[look] < H and 0 <= t_y + dy[look] < W:
                if table[t_x + dx[look]][t_y + dy[look]] == '.':
                    table[t_x + dx[look]][t_y + dy[look]] = '^'
                    table[t_x][t_y] = '.'
                    t_x = t_x + dx[look]
                    t_y = t_y + dy[look]
        elif command[i] == 'D':
            look = 3
            table[t_x][t_y] = 'v'
            if 0 <= t_x + dx[look] < H and 0 <= t_y + dy[look] < W:
                if table[t_x + dx[look]][t_y + dy[look]] == '.':
                    table[t_x + dx[look]][t_y + dy[look]] = 'v'
                    table[t_x][t_y] = '.'
                    t_x = t_x + dx[look]
                    t_y = t_y + dy[look]


        elif command[i] == 'S':
            b_x = t_x
            b_y = t_y
            while 0 <= b_x + dx[look] < H and 0 <= b_y + dy[look] < W:
                b_x = b_x + dx[look]
                b_y = b_y + dy[look]
                if table[b_x][b_y] == '*':
                    table[b_x][b_y] = '.'
                    break
                elif table[b_x][b_y] == '#':
                    break
    print('#%d' % T, end=" ")
    for line in table:
        print(''.join(line))