import sys
sys.stdin = open("프린터_input.txt")

priorities = list(map(int, input().split()))
location = int(input())

answer = 0
N = len(priorities)
sorteds = sorted(priorities)
cnt = -1
while True:
    # i = 0
    for j in range(N):
        # print(cnt)
        if priorities[j] == sorteds[cnt]:
            if j == location:
                answer = -1 * cnt
                break
            priorities[j] = cnt
            cnt -= 1
        # i += 1
    if answer != 0:
        break
print(answer)