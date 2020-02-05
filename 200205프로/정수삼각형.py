triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

LT = len(triangle)
arr = [[0] * a for a in range(1, LT+1)]
arr[0][0] = triangle[0][0]
for i in range(LT-1):
    for j in range(i+1):
        left = arr[i][j] + triangle[i+1][j]
        right = arr[i][j] + triangle[i+1][j+1]
        if arr[i+1][j] < left:
            arr[i+1][j] = left
        if arr[i+1][j+1] < right:
            arr[i+1][j+1] = right
print(max(arr[LT-1]))
