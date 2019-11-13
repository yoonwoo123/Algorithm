def dfs(v):
    global G, visited, V
    s = []
    s.append(v) # while문을 충족시키기 위해 첫번째 값을 넣고 시작

    while len(s) != 0:
        v = s.pop()
        if not visited[v] :# visited[v]==0: 방문안했으면
            visited[v] = 1 # 방문체크
            print(v, end=" ")
            for w in range(1, V + 1):  # 인접한것중 방문안한걸 push
                if G[v][w] == 1 and visited[w] == 0 and degree[w] != 0:  # 인접해있고 and 방문안했으면
                    degree[w] -= 1 # 인접한 디그리 1빼줌
                if degree[w] == 0:
                    s.append(w)

import sys
sys.stdin = open('0214workshop_input.txt')

testcases = 10
for T in range(testcases):
    V, E = list(map(int, input().split()))
    temp = list(map(int, input().split())) # [4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9]
    # print(temp)
    G = [[0 for i in range(V + 1)] for j in range(V + 1)]  # 2차원 초기화 0, 0 ~ 9, 9
    visited = [0 for i in range(V + 1)]  # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    degree = [0 for i in range(V+1)]
    # print(degree)
    for i in range(E): # 인접한 노드들을 1로 표시
        G[temp[i*2]][temp[i*2+1]] = 1 # 위에서 아래로만 갈수있게 하나만
    # for i in range(len(G[i][1:])):
    #     degree[i] + G[i]
    for i in range(1, V+1):
        # print("{} {}".format(i, G[i])) # 찍혀있는 개수를 전부 더한게 그 수의 degree
        for x in range(len(G[i])):
            degree[x] += G[i][x]
    # print(degree)
    first = 0
    for f in range(1 ,len(degree)):
        if degree[f] == 0:
            first = f
    print(f'#{T+1}', end =' ')
    dfs(first)
    print()