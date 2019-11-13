T = int(input())
R, C = map(int, input().split())

arr = [list(map(int, input())) for _ in range(R)]

print(T)
print(R, C)
for i in range(0, R):
    for j in range(0, C):
        print(arr[i][j], end="")
    print()