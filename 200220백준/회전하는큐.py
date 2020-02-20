import sys, collections
sys.stdin = open("회전하는큐_input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
chooses = list(map(int, input().split()))

arr = collections.deque([x for x in range(N)])
# 1. popleft() 해서 원하는 것을 뽑는 수행
# 2. 왼쪽으로 한칸 즉, arr.append(arr.popleft())
# 3. 오른쪽으로 한칸 즉, arr.appendleft(arr.pop())

ans = 0
for choose in chooses:
    choose -= 1
    t = arr.index(choose)
    while True:
        if t == 0:
            arr.popleft()
            N -= 1
            break
        if t <= N - t:
            arr.append(arr.popleft())
            t -= 1
            if t < 0:
                t = N - 1
        else:
            arr.appendleft(arr.pop())
            t += 1
            if t >= N:
                t = 0
        ans += 1
print(ans)
