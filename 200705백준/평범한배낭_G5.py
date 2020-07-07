import sys, itertools
sys.stdin = open("평범한배낭_input.txt")
input = sys.stdin.readline

# 스탠다드한 DP 문제로써 이차원으로 배열을 만든다면 N * K 만큼의 시간복잡도를 가진다.
# 그러나 DP 배열을 일차원으로 만든다면 엄청나게 시간을 단축 시킬 수 있다.
# 현재 문제는 이차원으로 풀었으나 이 문제는 일차원으로 바꿀 수 있다.

N, K = map(int, input().split())
objs = [[0, 0]]
for i in range(N):
    objs.append(list(map(int, input().split())))
ans = 0
dp = [[0 for q in range(K+1)] for w in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        if objs[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - objs[i][0]] + objs[i][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])