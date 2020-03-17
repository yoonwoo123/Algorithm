import sys
sys.stdin = open("쇠막대기_input.txt")
input = sys.stdin.readline

ans = 0
arr = input()
L = len(arr)
pipe = 0
i = 0
while i < L:
    if arr[i:i+2] == '()':
        ans += pipe
        i += 2
    else:
        if arr[i] == '(':
            pipe += 1
        elif arr[i] == ')':
            ans += 1
            pipe -= 1
        i += 1
print(ans)
