n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

def solution(n, k, cmd):
    def moveCursor(command, k):
        direction, cnt = command.split(" ")
        cnt = int(cnt)

        if direction == "U":
            for _ in range(cnt):
                k = linkedList[k][0]

        elif direction == "D":
            for _ in range(cnt):
                k = linkedList[k][1]

        return k

    linkedList = {"head": ["-", 0], "tail": [n-1, "-"]}
    deletedList = []

    for i in range(n):
        prev, next = i - 1, i + 1

        if i == 0:
            prev = "head"

        elif i == n-1:
            next = "tail"

        linkedList[i] = [prev, next]

    for command in cmd:
        if len(command) != 1:
            k = moveCursor(command, k)

        else:
            if command == "C":
                deletedList.append(k)
                left, right = linkedList[k]
                linkedList[left][1] = right
                linkedList[right][0] = left

                if right == "tail":
                    k = left
                else:
                    k = right

            elif command == "Z":
                lastDeletedIndex = deletedList.pop()
                left, right = linkedList[lastDeletedIndex]
                linkedList[left][1] = lastDeletedIndex
                linkedList[right][0] = lastDeletedIndex

    answer = ["O" for _ in range(n)]

    for index in deletedList:
        answer[index] = "X"

    return ''.join(answer)

print(solution(n, k, cmd))