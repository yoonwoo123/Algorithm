def dfs(v):
    global G, visited, V
    s = []
    result = []
    s.append(v) # while문을 충족시키기 위해 첫번째 값을 넣고 시작
    while len(s) != 0:
        v = s.pop()
        if not visited[v] :# visited[v]==0: 방문안했으면
            visited[v] = 1 # 방문체크
            # print(v, end=" ")
            result.append(v)
            for w in range(1, V+1): # 인접한것중 방문안한걸 push
                if G[v][w] == 1 and visited[w] == 0: # 인접해있고 and 방문안했으면
                    s.append(w) # push
    if last in result:
        return 1
    else:
        return 0

import sys
sys.stdin = open("0214_Stack1_input.txt")
testcases = int(input())
for T in range(testcases):
    temp = []
    V, E = map(int, input().split()) # V = 6, E = 5
    for _ in range(E):
        two = list(map(int, input().split()))  # [1 4]
        for n in two:
            temp.append(n)
    # print(temp) # [1, 4, 1, 3, 2, 3, 2, 5, 4, 6]
    G = [[0 for i in range(V+1)] for j in range(V+1)] # 2차원 초기화 0, 0 ~ 6, 6
    visited = [0 for i in range(V+1)] # [0, 0, 0, 0, 0, 0, 0]
    #
    for i in range(E): # 인접한 노드들을 1로 표시
        G[temp[i*2]][temp[i*2+1]] = 1 # 위에서 아래로만 갈수있게 하나만

    first, last = map(int, input().split()) # 1, 6

    for i in range(1, V+1):
        print("{} {}".format(i, G[i]))
    print(f'#{T+1} {dfs(first)}')