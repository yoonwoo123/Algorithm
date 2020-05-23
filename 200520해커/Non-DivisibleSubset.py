import itertools

n, k = 4, 3
s = [1, 7, 2, 4]
# 두 개를 합한 수를 k로 나눴을 때 0이 아닌 수들을 set에 중복되지 않게 모으자.
knums = {}
for i in range(k):
    knums[i] = 0

for num in s:
    knums[num%k] += 1
    
ans = 0
for key, val in knums.items():
    if key == 0:
        if val:
            ans += 1
    else:
        if key == k - key:
            ans += 1
            knums[k - key] = knums[key] = 0
        else:
            ans += max(knums[k - key], knums[key])
            knums[k - key] = knums[key] = 0
print(ans)