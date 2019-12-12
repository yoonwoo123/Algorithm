import sys
sys.stdin = open("후보키_input.txt")

def DFS(dep):

    if dep == LenC:
        # print(A)
        if Search(A): # 유일성을 만족함.
            # print(A)
            tmp = set()
            for y in range(LenC):
                if A[y] == 1:
                    tmp.add(y)

            for s in id:
                if s - tmp == set():
                    return
            id.append(tmp)
            # print(id)
        return

    for i in range(2):
        A[dep] = i
        DFS(dep + 1)
        A[dep] = 0

def Search(A):

    tmp = {}
    for x in range(LenR):
        name = ''
        for y in range(LenC):
            if A[y] == 1:
                name += relation[x][y]
        if name != '' and name not in tmp:
            tmp[name] = 1
        else:
            return 0
        # print(tmp)
    return 1


relation = [list(input().split()) for _ in range(6)]

answer = 0
LenC = len(relation[0])
LenR = len(relation)

visit = [0] * LenC # 유일성과 최소성을 지킨 열은 체크하자.
id = []
# 모든 부분 집합의 경우의 수를 전부 탐색해야한다.
# 그 중 visit이 체크되면 그 부분은 continue

A = [0] * LenC
DFS(0)
answer = len(id)
print(answer)