import sys
sys.stdin = open("스파이조직_input.txt")

N, S = input().split()
N = int(N)

s = []
degarr = []
deg = 0

for i in range(50):
    degarr.append([0])
for i in S:
    if i == 0:
        s.append(0)

    elif i == '<':
        s.append(i)
        deg += 1
    elif i == '>':
        s.pop()
        deg -= 1
    elif i != '<' and i != '>':
        degarr[deg].append(i)


print(degarr[N])
# for i in range(1, len(degarr[N])):
#     print(degarr[N][i], end=" ")
# print()