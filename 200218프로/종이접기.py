n = int(input())
answer = [0]

for i in range(1, n): # n-1번
    tmp = [0]
    tot = 2**(i) - 1
    for cnt in range(1, tot+1):
        if answer[-cnt]:
            tmp.append(0)
        else:
            tmp.append(1)
    answer.extend(tmp)
print(answer)