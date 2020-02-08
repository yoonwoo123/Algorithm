import sys
sys.stdin = open("체스판다시칠하기_input.txt")

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
answer = 99

for x in range(N-8+1):
    for y in range(M-8+1):
        cnt = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i + j) % 2 == 0 and table[i][j] == 'W': # 더해서 짝수면 B
                    cnt += 1
                elif (i + j) % 2 == 1 and table[i][j] == 'B':
                    cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        answer = min(answer, cnt)
print(answer)