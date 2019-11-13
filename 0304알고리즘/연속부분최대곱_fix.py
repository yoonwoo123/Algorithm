import sys
sys.stdin = open("연속부분최대곱_input.txt")

N = int(input())
line = []
pre = 0
res = []

for i in range(N):
    line.append(float(input()))
line += [-1]
for i in range(N):
    if line[i] == -1:
        break

    if line[i] > 1:
        pre = line[i]
        if line[i+1] == -1:
            break
        pre *= line[i+1]
        res.append(pre)
        cnt = 2
        while pre > 1 and line[i+cnt] != -1:
            pre *= line[i+cnt]
            res.append(pre)
            cnt += 1
if len(res) == 0:
    max = 0
    for i in range(N):
        if line[i] < 1 and line[i] > max:
           max = line[i]
    res = max
    print("%.3f" % res)
else:
    print("%.3f" % max(res))
