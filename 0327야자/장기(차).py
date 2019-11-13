

# N개의 줄에 걸쳐, 게임판에서 각 줄의 몇 번째 칸에 차를 배치했는지를
# 나타내는 칸의 번호를 순서대로 출력한다. 조건을 만족시키는 배치가 둘 이상이면
# 아무 것이나 출력한다. 배치가 불가능한 경우 첫째 줄에 -1만을 출력한다.
import sys
sys.stdin = open("장기(차)_input.txt")

N = int(input())
r = []
arr = [0 for _ in range(N)]
# cnt = 0
flag = 0
if N == 3:
    print(-1)
    flag = 1
if flag == 0:
    for x in range(N):
        for y in range(N):
            if x == y or y == N-1-x:
                continue
            if arr[y] == 1:
                continue
            arr[y] = 1
            r.append(y+1)
            # print(y+1)
            break
    print('\n'.join(map(str, r)))
# print(cnt)
# for g in arr:
#     print(g)
# print()
# for num in res:
#     print(num+1)