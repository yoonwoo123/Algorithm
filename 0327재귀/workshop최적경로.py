# 파이썬에서 걸리는 시간 구하는 방법
# import time
# from time import strftime

# start_time = time.time()

#------main----------
# sum = 0
# for i in range(1000000):
#     sum += i
#--------------------
# print(time.time()- start_time, 'sec')
import sys
sys.stdin = open("최적경로_input.txt")
# 거리 계산을 미리 계산해놓고 그 값을 가져와서 가지치기
def perm(n, k, tot): # 구하고자 하는 순열의 갯수, k는 무조건 0부터 커짐
    global res
    if res <= tot: return # 가지치기
    # tot = 0
    if n == k:
        tot += abs(com[0] - cli[0][0]) + abs(com[1] - cli[0][1]) # 회사와 첫고객과 거리
        tot += abs(house[0] - cli[-1][0]) + abs(house[1] - cli[-1][1])
        for i in range(N-1):
            tot += abs(cli[i][0] - cli[i+1][0]) + abs(cli[i][1] - cli[i+1][1]) # 첫고객과 둘째고객거리
            if res <= tot: return # 가지치기
        if res > tot:
            res = tot

    else:
        tot_t = abs(com[0] - cli[0][0]) + abs(com[1] - cli[0][1])  # 회사와 첫고객과 거리

        for i in range(k):
            tot_t += abs(cli[i][0] - cli[i + 1][0]) + abs(cli[i][1] - cli[i + 1][1])  # 첫고객과 둘째고객거리
            if res <= tot_t: return  # 가지치기
        tot_t += abs(house[0] - cli[-1][0]) + abs(house[1] - cli[-1][1])

        for i in range(k, n): # 0 ~ N 고객수만큼 돌아감
            cli[i], cli[k] = cli[k], cli[i]
            perm(n, k+1, tot)
            cli[i], cli[k] = cli[k], cli[i] # 원본으로 돌리기 위함
# a = [1, 2, 4, 7, 8, 3]
# perm(4, 0)

# # 좌표값을 하나의 값이라고 생각하고 순열로 좌표값을 나열해보자
tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    cli = [0] * (N+2)
    res = 1000000000
    arr = list(map(int, input().split()))
    for i in range(N+2):
        x = arr[i*2]
        y = arr[i*2+1]
        cli[i] = [x, y] # cli.append 보다 cli[i]에 값을 대입하는게 훨 빠르다!

    com = cli.pop(0)
    house = cli.pop(0)
    # print(cli)
    perm(N, 0, 0)
    print('#%d %d' % (T, res))





