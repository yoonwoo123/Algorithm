import sys
sys.stdin = open("동전0_input.txt")

N, K = map(int, input().split())
bills = [int(input()) for _ in range(N)]
ans = 0
while K:
    bill = bills.pop()
    ans += K // bill
    K %= bill
print(ans)