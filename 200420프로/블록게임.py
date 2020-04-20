
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]

def up(x, y, board):
    for i in range(x, -1, -1):
        if board[i][y]: return False
    return True

def solution(board):
    answer = 0
    N = len(board)
    block = {}
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                if board[x][y] not in block:
                    block[board[x][y]] = [(x, y)]
                else:
                    block[board[x][y]].append((x, y))
    # print(block)
    blank = {}
    for k, v in block.items():
        r, c = set(), set()
        for x, y in v:
            r.add(x)
            c.add(y)
        for i in r:
            for j in c:
                if (i, j) not in v:
                    if k not in blank:
                        blank[k] = [(i, j)]
                    else:
                        blank[k].append((i, j))
    # print(blank)
    # 열이 중요하다, 세로로 열마다 두 검은블록을 떨어트려 빈좌표 둘다 채울수있냐
    # 둘 다 채운다면 ans += 1 하고 그 좌표를 blank_dict에서 삭제한 후 다시 첨부터 돌림
    flag = True
    while flag:
        flag = False
        for k, v in blank.items():
            cnt = 0
            for x, y in v:
                if not up(x, y, board): # False면
                    break
                cnt += 1
            if cnt == 2:
                flag = True
                answer += 1
                for i, j in block[k]:
                    board[i][j] = 0
                blank.pop(k)
                break
    return answer
print(solution(board))