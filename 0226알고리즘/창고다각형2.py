import sys
sys.stdin = open('창고다각형_input.txt')

heights = []
loc = []
lh = []
my_max = 0
max_idx = 0
N = int(input())


for i in range(N): #높이와 위치값 배열 생성
    L, H = map(int, input().split())
    loc.append(L)
    heights.append(H)
maxh = sorted(heights)[::-1]
print(maxh)
for i in range(len(loc)): # 제일큰기둥의 인덱스값찾기
    if my_max < heights[i]:
        my_max = heights[i]
        max_idx = i

for x in range(len(loc)): # 위치,높이 2차배열
    tmp = []
    tmp.append(loc[x])
    tmp.append(heights[x])
    lh.append(tmp)


