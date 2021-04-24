import copy

a = [[0, 1], [1, 0], [1, 1], [1, 2]]
b = [[1, 2], [2, 3]]

n = 2

def rotate90(a, cnt):
    newA = copy.deepcopy(a)

    for i in range(cnt):
        for poses in newA:
            poses[0], poses[1] = poses[1], n - 1 - poses[0]

        minusX = minusY = 0
        for posX, posY in newA:
            if posX < 0:
                minusX = min(minusX, posX)
            if posY < 0:
                minusY = min(minusY, posY)

        for i in range(len(newA)):
            newA[i][0] -= minusX
            newA[i][1] -= minusY

        print(newA)

    return newA

print(a)
newA = rotate90(a, 3)