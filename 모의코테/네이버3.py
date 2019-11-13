import sys
sys.stdin = open("네이버3_input.txt")

N = int(input())

times = [list(map(int, input().split())) for _ in range(N)]
times.sort()
# print(times)
table = [times[0][1]]
for i in range(1, N):
    mi = min(table)
    if mi > times[i][0]:
        table.append(times[i][1])
    else:
        table[table.index(mi)] = times[i][1]
print(len(table))