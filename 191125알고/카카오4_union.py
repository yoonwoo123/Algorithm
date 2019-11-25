import sys
sys.stdin = open("카카오4_input.txt")

def parent_find(x):
    if x == parent[x]: # x의 부모가 자기 자신이라면 말단
        return x
    p = parent_find(parent[x]) # x의 최상위 부모 p 를 찾아주자
    parent[x] = p # x의 최상위 부모값을 p로 바꿔준다.
    return p

def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y # x의 부모는 y로

k = int(input())
room_number = list(map(int, input().split()))

answer = []
parent = {i:i for i in range(k+1)}
# print(parent)

cnt = 0
for room in room_number:
    x = parent_find(room) # 그 방의 최상위 부모가 나올것 > 그 방에서 연속한 가장 끝방
    if x == k: break # 방의 크기보다 넘어선다면 break
    answer.append(x)
    union(x, x+1) # x의 부모를 x+1 즉 다음방으로 설정함
print(answer)