from heapq import heappop, heappush, heapify, _heappop_max

operations = ["I 7", "I 5", "I -5", "D -1", "I 13", "I 6", "D 1"]

answer = [0, 0]
que = []
for operation in operations:
    command, integer = operation.split()
    integer = int(integer)
    if command == "I":
        heappush(que, integer)
    else:
        if que == []: continue
        if integer == -1:
            heappop(que)
        else:
            que.pop()
if que != []:
    answer = [max(que), heappop(que)]
print(answer)
