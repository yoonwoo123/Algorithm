import sys
sys.stdin = open("마을위성사진_input.txt")

N = int(input())
table = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0 ]
max = 0
for i in range(N):
    table.append(list(map(int, list(input()))))
cnt = 1
for _ in range(N//2):
    for x in range(1, N-1):
        for y in range(1, N-1):
            around = 0
            if table[x][y] >= cnt:
                for t in range(4):
                    if table[x + dx[t]][y + dy[t]] >= cnt:
                        around += 1
                if around == 4: # 주변 언덕의 가장 낮은 언덕의 높이보다 1 높아진다.
                    table[x][y] += 1
    cnt += 1
    for x in range(N):
        for y in range(N):
            if max < table[x][y]:
                max = table[x][y]
print(max)
