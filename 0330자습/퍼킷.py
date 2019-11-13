import sys, collections
sys.stdin = open("퍼킷_input.txt")
# 부분집합의 합 변형
def powerset(n, k): # N의 갯수, k는 깊이 보통0시작
    global my_min
    # if my_min <= abs(stot - btot):
    #     return
    # 가지 쳐줄라면 함수인자로 sum을 넘겨주자.
    if n == k:
        stot = 1
        btot = 0
        flag = 0
        for i in range(N):
            if A[i] == 1:
                s, b = mat[i][0], mat[i][1]
                stot *= s
                btot += b
                flag = 1
                res = abs(stot - btot)
                if my_min > res:
                    my_min = res
        if flag == 0:
            return
        # elif my_min > abs(stot - btot):
        #     my_min = abs(stot - btot)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

N = int(input())
A = [0 for _ in range(N)]
mat = []
my_min = 999999999999
for i in range(N):
    S, B = map(int, input().split())
    mat.append([S, B])
# print(mat)

powerset(N, 0)
print(my_min)