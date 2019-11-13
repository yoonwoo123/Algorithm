import sys
sys.stdin = open('창고다각형_input.txt')

heights = []
loc = []
lh = []

max_idx = 0
N = int(input())
my_max = 0
res = 0

table = []
for i in range(1001): # 1000 X 1000 테이블
    table.append([0]*1001)

for i in range(N): #높이와 위치값 배열 생성
    L, H = map(int, input().split())
    loc.append(L)
    heights.append(H)

for i in range(len(loc)): # 제일큰기둥의 인덱스값찾기
    if my_max < heights[i]:
        my_max = heights[i]
        max_idx = i

for x in range(heights[max_idx]): # 큰기둥을 테이블에 찍어줌
    table[x][loc[max_idx]] = 1

# for i in range(len(loc)): # 기둥왼쪽오른쪽
#     if loc[i] < loc[max_idx]:
#         left.append(loc[i])
#     if loc[i] > loc[max_idx]:
#         right.append(loc[i])
# l = sorted(left)[::-1]
# r = sorted(right)[::-1]

for x in range(len(loc)): # 위치,높이 2차배열
    tmp = []
    tmp.append(loc[x])
    tmp.append(heights[x])
    lh.append(tmp)

maxh = sorted(heights)[::-1]
cnt = 0
maxcnt = 1
mi = 0
for tt in range(len(loc)):
    if min(loc) == lh[tt][0]:
        mi = tt
while len(lh) > 1:
    # for i in range(1, len(loc)):
    # for x in range(len(loc)):
    # if lh[mi][1] >= lh[cnt][1]:
    #     continue

    if maxh[maxcnt] == lh[cnt][1]:
        maxcnt += 1
        if loc[max_idx] > lh[cnt][0]:
            for yh in range(lh[cnt][0], loc[max_idx]):
                for xl in range(lh[cnt][1]):
                  # 테이블에 찍어줌 왼쪽으로
                    if table[xl][yh] == 0:
                        table[xl][yh] = 1
                    else:
                        break
            lh.pop(cnt)
            cnt = 0
            continue
        if loc[max_idx] < lh[cnt][0]:
            for yh in range(loc[max_idx] + 1, lh[cnt][0] +1):
                for xl in range(lh[cnt][1]):
                  # 테이블에 찍어줌 왼쪽으로
                  if table[xl][yh] == 0:
                      table[xl][yh] = 1
                  else:
                      break
            lh.pop(cnt)
            cnt = 0
    else:
        cnt += 1

for x in range(1000): # 1000 X 1000 테이블
    for y in range(1000):
        if table[x][y] == 1:
            res += 1
print(res)
    # 창고의 최소 총면적을 구해야한다.
    # 테이블에 1로 표시해서 합으로 구해보자
    # 물이 고이지 않아야 하기 때문에 크고 작고 크고는 나올수 없다. 즉
    # 최대점을 한번 찍으면 그것보다 높은건 나오지않고 내려오기만한다.
    # 최종기둥을 빼고 양옆만 생각해보자.
