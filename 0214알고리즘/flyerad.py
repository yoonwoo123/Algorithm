import sys
sys.stdin = open("flyerad_input.txt")
testcases = input()
for T in range(int(testcases)):
    N, M = map(int, input().split())
    data =[]
    result = 0
    for q in range(N):
        data.append(list(map(int, input().split())))
    for a in range(N-M+1):#  반복
        for b in range(N-M+1):
            total = 0
            for i in range(M):
                for x in range(M):
                    total += data[i+a][x+b]
            if total > result:
                result = total
    print(f'#{T+1} {result}')