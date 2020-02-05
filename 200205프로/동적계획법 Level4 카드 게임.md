## 동적계획법 Level4 카드 게임

### deque를 이용한 popleft(), append() 방식

```python
# 정확성은 3개 틀리고, 효율성은 5개 중 1개 맞음

import sys, collections
sys.stdin = open("카드게임_input.txt")

left = list(map(int, input().split()))
right = list(map(int, input().split()))

answer = 0
LenL = len(left)
LenR = len(right)
table = [[-1] * LenR for _ in range(LenL)]
table[0][0] = 0 #시작값 0
arr = collections.deque()
arr.append([0, 0])

while arr:
    x, y = arr.popleft()
    if left[x] > right[y]:
        if y + 1 >= LenR:
            if table[x][y] + right[y] > answer:
                answer = table[x][y] + right[y]
            continue
        table[x][y+1] = table[x][y] + right[y]
        arr.append([x, y+1])
    else:
        if x + 1 >= LenL:
            if table[x][y] > answer:
                answer = table[x][y]
            continue
        if table[x+1][y] == -1: # 방문 안했다면
            table[x+1][y] = table[x][y]
            arr.append([x+1, y])
		else: # 이 부분의 수정을 통해 정확성이 약간 변경
            if table[x+1][y] < table[x][y]:
                table[x+1][y] = table[x][y]
                arr.append([x+1, y])
        if y + 1 >= LenR:
            if table[x][y] > answer:
                answer = table[x][y]
            continue
        table[x+1][y+1] = table[x][y]
        arr.append([x+1, y+1])

print(answer)
```



### 재귀를 이용한 방식 1

```python
# 정확성은 전부 맞으나, 효율성이 전부 틀림
def solution(left, right):
    global answer
    def search(x, y, left, right, table):
        global answer

        if left[x] > right[y]:
            if y + 1 >= Len:
                if table[x][y] + right[y] > answer:
                    answer = table[x][y] + right[y]
                return
            table[x][y+1] = table[x][y] + right[y]
            search(x, y+1, left, right, table)
        else:
            if x + 1 >= Len:
                if table[x][y] > answer:
                    answer = table[x][y]
                return
            if table[x+1][y] == -1: # 방문 안했다면
                table[x+1][y] = table[x][y]
                search(x+1, y, left, right, table)
            else:
                if table[x+1][y] < table[x][y]:
                    table[x+1][y] = table[x][y]
                    search(x+1, y, left, right, table)
            if y + 1 >= Len:
                if table[x][y] > answer:
                    answer = table[x][y]
                return
            table[x+1][y+1] = table[x][y]
            search(x+1, y+1, left, right, table)

    answer = 0
    Len = len(left)
    table = [[-1] * Len for _ in range(Len)]
    table[0][0] = 0 #시작값 0

    search(0, 0, left, right, table)
    return answer

# 재귀 방식을 더 깔끔하게 고쳐서 통과
import sys
sys.stdin = open("카드게임_input.txt")

sys.setrecursionlimit(10**6)
def search(x, y, left, right, table):
    if x >= Len or y >= Len:
        return 0
    if table[x][y] != -1:
        return table[x][y]
    if left[x] > right[y]:
        v = search(x, y+1, left, right, table) + right[y]
        table[x][y] = v
        return v
    else:
        v = max(search(x+1, y+1, left, right, table), search(x+1, y, left, right, table))
        table[x][y] = v
        return v

left = list(map(int, input().split()))
right = list(map(int, input().split()))

Len = len(left)
table = [[-1] * Len for _ in range(Len)]

answer = search(0, 0, left, right, table)
for g in table:
    print(g)
print(answer)
```

### 재귀를 이용한 방식2 - 다른 분 풀이 참조

```python
import sys
sys.setrecursionlimit(10**6) # 효율성 런타임에러 방지 깊이를 설정
def solution(left, right):
    def cal(leftIndex, rightIndex, left, right, arr):
        if leftIndex < 0 or rightIndex < 0: # 인덱스 에러 방지
            return 0
        if arr[leftIndex][rightIndex] != -1: # 중복 실행 방지
            return arr[leftIndex][rightIndex]
        if right[rightIndex] < left[leftIndex]:
            v = cal(leftIndex, rightIndex - 1, left, right, arr) + right[rightIndex]
            arr[leftIndex][rightIndex] = v
            return v
        else:
            v = max([cal(leftIndex - 1, rightIndex, left, right, arr),
                     cal(leftIndex - 1, rightIndex - 1, left, right, arr)])
            arr[leftIndex][rightIndex] = v
            return v
    num = len(left)
    arr = [[-1] * num for _ in range(num)]
    answer = cal(num - 1, num - 1, left, right, arr)
    return answer
```

### for 문을 두개로 메모이제이션 - 코드 짧,효율은 재귀에 비해별로

```python
import sys
sys.stdin = open("카드게임_input.txt")

left = list(map(int, input().split()))
right = list(map(int, input().split()))
Len = len(left)
dp = [[0 for x in range(len(left)+1)] for y in range(len(right)+1)]
for i in range(1, len(left)+1):
    for j in range(1, len(right)+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
        if right[j-1] < left[i-1]:
            dp[i][j] = dp[i][j-1] + right[j-1]

answer = dp[Len][Len]
for g in dp:
    print(g)
print(answer)
```

