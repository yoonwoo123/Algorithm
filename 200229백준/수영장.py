import sys
sys.stdin = open("수영장_input.txt")
input = sys.stdin.readline

def DFS(m, tot):
    global ans
    if tot >= ans: return # 가지치기
    if m >= 12:
        ans = min(ans, tot)
        return

    DFS(m + 1, tot + months[m] * bills[0])
    DFS(m + 1, tot + bills[1])
    DFS(m + 3, tot + bills[2])

tc = int(input())
for T in range(1, tc+1):
    bills = list(map(int, input().split()))
    months = list(map(int, input().split()))
    ans = 9999
    DFS(0, 0)
    print(f'#{T} {min(ans, bills[3])}')

## DP 방식
# T = int(input())
# for test_case in range(1, T+1):
#     day, m1, m3, year = list(map(int, input().split()))
#     List = [0] + list(map(int, input().split()))
#     day_arr = [0] * 13
#     for i in range(1, 13):
#         if i < 3:
#             day_arr[i] = day_arr[i-1] + min(day*List[i], m1)
#         else:
#             day_arr[i] = min((day_arr[i - 1] + min(day * List[i], m1)), day_arr[i-3] + m3)
#     res = day_arr[-1]
#     if year < day_arr[-1]:
#         res = year
#     print("#{} {}".format(test_case, res))