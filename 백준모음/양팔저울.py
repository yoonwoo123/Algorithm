import sys
sys.stdin = open("양팔저울_input.txt")

# def DFS(dep, tot):
#     # global tot
#     if chk[abs(tot)] == 1: return
#     chk[abs(tot)] = 1 # 방문체크
#
#     if dep >= CN:
#         return
#
#     for i in range(2):
#         if i == 0:
#             DFS(dep + 1, tot + chus[dep])
#         else:
#             DFS(dep + 1, tot - chus[dep])
#
# CN = int(input()) # CN <= 30
# chus = list(map(int, input().split()))
# chk = [0] * sum(chus) + 1 # chk 해두자
# # tot = 0
# BN = int(input()) # BN <= 7
# balls = list(map(int, input().split()))
#
# # for ball in balls:
# DFS(0, 0)
# print(chk)
# def DFS(no, Lsum, Rsum):
#     global sol
#     # 현재 추를 사용(왼, 오른쪽저울) 하거나 사용하지 않는 경우의 수
#
#     # if Lsum < Rsum:
#     #     return
#     if no >= CN:
#         if Lsum == Rsum:
#             sol = 1
#         return
#     if abs(Lsum - Rsum) > tot[no]: # 가지치기: 양쪽저울의 차보다 남은 추가 부족하면
#         return
#     else:
#         rec[no] = 0
#         DFS(no + 1, Lsum, Rsum)
#         rec[no] = 1
#         DFS(no +1, Lsum + choos[no], Rsum)
#         rec[no] = 2
#         DFS(no + 1, Lsum, Rsum + choos[no])
#
# CN = int(input())
# choos = list(map(int, input().split()))
# # print(sum(choos[1:CN]))
# BN = int(input())
# balls = list(map(int, input().split()))
# rec = [0] * CN
# tot = [0] * CN
# for i in range(CN):
#     tot[i] = sum(choos[i:CN])
# # print(tot)
# # 추로 만들 수 있는 모든 경우의 수를 계산하자 그래서 구슬이 그만든 값안에 있으면 Y 아니면 N
# for i in range(BN):
#     sol = 0
#     DFS(0, balls[i], 0) # 0번추부터 시작, 왼쪽저울에 구슬값으로, 오른쪽저울 0
#     if sol: print('Y', end=" ")
#     else: print('N', end=" ")

N = int(input())
choo = list(map(int, input().split()))
# print(sum(choos[1:CN]))
N1 = int(input())
check = list(map(int, input().split()))

visited = [False] * (sum(choo) + 1)
visited[0] = True
for s in choo:
    for i, e in enumerate(visited[:]):
        print(f'{i}, {e}')
        if e:
            if not (visited[i + s]):
                visited[i + s] = True
                print(visited)
for s in choo:
    for i, e in enumerate(visited[:]):
        print(f'{i}, {e}')
        if e:
            if i-s >= 0:
                if not (visited[i - s]):
                    visited[i - s] = True
                    print(visited)
for c in check:
    if c > len(visited) - 1:
        print("N", end=" ")
    else:
        if visited[c]:
            print("Y", end=" ")
        else:
            print("N", end=" ")