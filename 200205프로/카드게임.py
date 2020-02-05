import sys
sys.stdin = open("카드게임_input.txt")

sys.setrecursionlimit(10**6)
def search(x, y, left, right, table):
    if x >= Len or y >= Len:
        return 0
    if table[x][y] != -1:
        return table[x][y]
    if left[x] > right[y]:
        v = search(x, y+1, left, right, table) + right[y]
        table[x][y] = v
        return v
    else:
        v = max(search(x+1, y+1, left, right, table), search(x+1, y, left, right, table))
        table[x][y] = v
        return v

left = list(map(int, input().split()))
right = list(map(int, input().split()))

Len = len(left)
table = [[-1] * Len for _ in range(Len)]

answer = search(0, 0, left, right, table)
for g in table:
    print(g)
print(answer)