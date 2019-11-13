import sys
sys.stdin = open("네이버6_input.txt")

N, type = input().split()
N = int(N)

table = [input().split() for _ in range(N)]
print(table)
mymax = -1
for i in range(N):
    table[i][0] = int(table[i][0])
    if mymax < table[i][0]:
        mymax = table[i][0]
H = 2 * mymax - 1 # 출력할 높이
# mymax는 가로길이 최대
# print(H)

if type == 'TOP':
    for i in range(H): # 높이만큼 출력할것이기 때문에
        for j in range(N):
            # print(table[j])
            if table[j][0] == mymax: # 정렬 신경안써도 됨
                # print(table[j][1][0])
                for k in range(len(table[j][1])):
                    if table[j][1][k] == '0':
                        if i == 0 or i == H-1:
                            print('#' * table[j][0], end=" ")
                        else:
                            print('#', end="")
                            print('.' * (table[j][0] - 2), end="")
                            print('#', end=" ")

                    elif table[j][1][k] == '1':
                        print('.' * (table[j][0] - 1), end="")
                        print('#', end=" ")
                    elif table[j][1][k] == '2':
                        if i == 0 or i == H // 2 or i == H-1:
                            print('#' * table[j][0], end=" ")

                        elif 0 < i < H // 2:
                            print('.' * (table[j][0] - 1), end="")
                            print('#', end=" ")
                        elif H // 2 < i < H-1:
                            print('#', end=" ")
                            print('.' * (table[j][0] - 1), end="")
                    elif table[j][1][k] == '3':
                        if i == 0 or i == H // 2 or i == H - 1:
                            print('#' * table[j][0], end=" ")

                        else:
                            print('.' * (table[j][0] - 1), end="")
                            print('#', end=" ")

                    elif table[j][1][k] == '4':
                        if i == 0 or i == H // 2 or i == H - 1:
                            print('#' * table[j][0], end=" ")

                        elif 0 < i < H // 2:
                            print('.' * (table[j][0] - 1), end="")
                            print('#', end=" ")
                        elif H // 2 < i < H - 1:
                            print('#', end=" ")
                            print('.' * (table[j][0] - 1), end="")



# 시간 부족..
elif type == 'MIDDLE':
    pass

else:
    pass