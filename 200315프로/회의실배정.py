import sys
sys.stdin = open("회의실배정_input.txt")
input = sys.stdin.readline

N = int(input())
meetings = [(*map(int, input().split()),) for _ in range(N)]
meetings.sort()
ans = 1
stime = meetings[-1][0]
for i in range(len(meetings)-2, -1, -1):
    if stime >= meetings[i][1]:
        ans += 1
        stime = meetings[i][0]
print(ans)