import sys
sys.stdin = open("알파벳_input.txt")

def BFS():
    s = [(0, 0, board[0][0])]
    cnt = 0
    while s:
        x, y, path = s.pop()
        flag = True
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            if board[nx][ny] in path: continue
            if visited[nx][ny] != path + board[nx][ny]:
                flag = False
                visited[nx][ny] = path + board[nx][ny]
                s.append((nx, ny, path + board[nx][ny]))
        if flag:
            cnt = max(cnt, len(path))
    return cnt

R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [[''] * C for _ in range(R)]
cnt = 0
print(BFS())

# def DFS(x, y, dep):
#     global res
#     res = max(res, dep)
#
#     for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
#         nx, ny = x + dx, y + dy
#         if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
#         i = ord(table[nx][ny]) - 65
#         if not visit[i]:
#             visit[i] = 1
#             DFS(nx, ny, dep + 1)
#             visit[i] = 0
#
# R, C = map(int, input().split())
# res = -1
#
# table = [input() for _ in range(R)]
# visit = [0] * 26
# visit[ord(table[0][0]) - 65] = 1
# DFS(0, 0, 1)
# print(res)