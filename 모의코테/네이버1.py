import sys
sys.stdin = open("네이버1_input.txt")

M, C = map(int, input().strip().split(' '))
times = []

for _ in range(M):
    times.append(int(input()))
print(times)
table = [0] * C # 컨슈머 개수만큼

# print(times.index(min(times)))
for t in times:
    table[table.index(min(table))] += t
print(max(table))

# table = [[0 for _ in range(1001)] for q in range(C)] # 테이블생성
# for g in table:
#     print(g)
# print()