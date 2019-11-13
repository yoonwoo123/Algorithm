import sys
sys.stdin = open("최소의합_input.txt")

def DFS(no, nsum):
    global sol
    if nsum > sol: # 가지치기
        return
    if no >= N:
        # for i in range(N):
        #     print(rec[i], end=" ")
        #     print(nsum)
        if nsum < sol:
            sol = nsum
        return

        # 현재 행에 모든 열의 수를 고르는 경우의 수 시도
        for i in range(N): # 열요소
            if chk[i] == 1: # 체크가 되어있으면 생략하고 다음숫자로 넘어감 ex) 1이 체크되어있으면 2로 넘어감
                continue
            chk[i] = 1 # 체크해줌
            rec[no] = arr[no][i]
            DFS(no + 1, nsum + arr[no][i])
            chk[i] = 0 # 체크 품

N = int(input())
arr = []
chk = [0] * 11 # 열의 중복을 체크할 배열
rec = [0] * 11 # 조합된 결과를 기록할 배열

for i in range(N):
    arr.append(list(map(int, input().split())))
# 1] 첫번째 방법: 열의 중복허용한 순열
sol = 100000









# #------------------- 한욱쌤 스타일---------------
# def perm(n, r, q): # sum을 넘겨줘야함.
#     # 가지치기 조건 들어가야함
#     if r== 0:
#         while q != 0:
#             q = q - 1
#             p.append(t[q])
#     else:
#         for i in range(n-1, -1, -1):
#             a[i], a[n-1] = a[n-1] , a[i]
#             t[r-1] = a[n-1]
#             perm(n-1, r-1, q)
#             a[i], a[n-1] = a[n-1], a[i]
#
# N = int(input())
# table = []
# total = []
#
# for i in range(N): # 세로 : x , 가로 : y  테이블 생성
#     tmp =list(map(int, input().split()))
#     table.append(tmp)
#
# a = [n for n in range(1, N+1)]
# # print(a)
# t = [0] * N
# p = []
# tot = 0
# for g in table:
#     tot += min(g)
#
# perm(N, N, N)
#
# total = []
# l = len(p)
# for _ in range(int(l//N)):
#     my_sum = 0
#     for i in range(N):
#         my_sum += table[i][p.pop(0)-1]
#     total.append(my_sum)
# print(tot)
# print(min(total))