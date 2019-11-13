import sys, itertools
sys.stdin = open("치킨배달2_input.txt")

def comb(no, tot): # 현재 치킨집(행) 에서 모든 집을 가는 경우
    global my_min
    if tot >= my_min:
        return
    if no >= M:
        if tot < my_min:
            my_min = tot
        return
    for i in range(len(house)): # 집 (열)
        if chk[i] == 1: continue
        chk[i] = 1
        comb(no + 1, tot + A[no][i])
        chk[i] = 0


N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
# 로봇-스낵 문제처럼 치킨집-집 문제이다. 치킨집 좌표는 뽑아두고
# 치킨집을 어떻게 고를지 조합으로 뽑아낸다.

# 집좌표를 순열로 바꿔가면서 최소값을 찾는다.
# 치킨집 = 2, 집 = 1

# 2. 토마토 응용 x
# 어차피 모든집까지의 거리를 계산해야하므로 치킨집을 토마토로 생각
# 각 집까지의 거리를 BFS로 찍어서 각 집까지 걸리는 시간을 저장한후
# 각집에 저장된 시간값을 더해서 그중 최소를 찾는다.

house = []
chicken = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            house.append([x, y])
        if arr[x][y] == 2:
            chicken.append([x, y])
print(house)
print(chicken)
my_min = 999999999999999
A = [[0 for _ in range(len(house))] for _ in range(len(chicken))] # 각 치킨집 [x] 에서 가정집 [y] 까지의 거리를 계산
chk = [0] * len(house)
# print(A)

for x in range(len(chicken)): # 치킨 집을 행으로
    for y in range(len(house)): # 열을 스택으로
        dist = abs(house[y][0] - chicken[x][0]) + abs(house[y][1] - chicken[x][1])
        A[x][y] = dist
print(A)
res = 0
for i in A:
    res += min(i)
print(res)
comb(0, 0)
print(my_min)
# itercomb = itertools.combinations(chicken, M)
# for i in itercomb:
#     print(i)

