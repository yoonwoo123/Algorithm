n = int(input())
answer = 0
f = []
f.append(1)
f.append(2)
for i in range(2, n):
    f.append((f[-1] + f[-2]) % 1000000007)
answer = f[-1]
print(answer)