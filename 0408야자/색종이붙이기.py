import sys, copy
sys.stdin = open("색종이붙이기_input.txt")

arr = []
N = 10

for i in range(N):
    arr.append(list(map(int, input().split())))

ori = copy.deepcopy(arr)

# for g in arr:
#     print(g)
# print()

a = 0
my_min = 99999999999
for u in range(4, 0, -1): # 4, 3, 2, 1
    for l in range(N):
        for p in range(N):
            arr[l][p] = ori[l][p] # 바뀐배열을 원본으로 복사
    cnt = [0] * 5 # 세어준 갯수 초기화

    for o in range(u, -1, -1): # 4, 3, 2, 1, 0
        for x in range(N - o):
            for y in range(N - o):
                flag = 0
                for i in range(x, x + o + 1):
                    if flag == 1: break
                    for j in range(y, y + o + 1):
                        if arr[i][j] == 0:
                            flag = 1
                            break
                if flag == 0:
                    cnt[o] += 1
                    for k in range(x, x + o + 1):
                        for t in range(y, y + o + 1):
                            arr[k][t] = 0
    # print(cnt)
    if sum(cnt) < my_min:
        for i in range(5):
            if cnt[i] > 5:
                # print(-1)
                a = 1
                break
        if a == 0:
            my_min = sum(cnt)
if my_min == 99999999999:
    print(-1)
else:
    print(my_min)
