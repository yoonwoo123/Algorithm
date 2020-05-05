import sys
sys.setrecursionlimit(10**6)
k = 10
room_number = [1,3,4,1,3,1]

def solution(k, room_number):

    def parent_find(x):
        if x not in parent:
            return x
        p = parent_find(parent[x])
        parent[x] = p
        return parent[x]

    def union(x, y):
        x = parent_find(x)
        y = parent_find(y)
        parent[x] = y

    answer = []
    parent = {}
    for room in room_number:
        if room not in parent:
            parent[room] = room + 1
            answer.append(room)
        else:
            x = parent_find(room)
            parent[x] = x + 1
            answer.append(x)
        print(parent)
    return answer

print(solution(k, room_number))