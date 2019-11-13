import sys
sys.stdin = open("카카오3_input.txt")

def DFS(dep):
    global answer

    if dep == LB:
        result = ''.join(map(str, chk))
        if result not in results:
            results.append(''.join(map(str, chk)))
            answer += 1
        return

    for num in ids[dep]:
        if chk[num]: continue # 체크가 되있으면
        chk[num] = 1
        DFS(dep + 1)
        chk[num] = 0


user_id = list(input().split())
banned_id = list(input().split())



answer = 0
LB = len(banned_id)
LU = len(user_id)
ids = [[] for _ in range(LB)]

for x in range(LB):
    for y in range(LU):
        l = len(user_id[y])
        if len(banned_id[x]) == l:
            flag = 1
            for i in range(l):
                if banned_id[x][i] == '*': continue
                if user_id[y][i] != banned_id[x][i]:
                    flag = 0 # 같지않다.
                    break
            if flag: # 제재될수있는 아이디라면
                ids[x].append(y) # 제재 아이디값 추가
# print(ids)
results = []
chk = [0] * LU
DFS(0)
print(answer)