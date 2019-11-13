import sys
sys.stdin = open("괄호_input.txt")

N = int(input())
arr = list(input())
print(arr)
my_max = int(arr[0])
for i in range(1, len(arr)-1, 2):
    if arr[i] == '+':
        my_max += int(arr[i+1])

    elif arr[i] == '*':
        my_max *= int(arr[i+1])

    elif arr[i] == '-':
        my_max -= int(arr[i+1])

print(my_max)
ori = arr.copy()
if N >= 5:
    for i in range(3, N, 4):
        if arr[i] == '+':
            tmp = int(arr[i - 1]) + int(arr[i + 1])
            arr[i-1] = tmp
            arr.pop(i)
            arr.pop(i)

        elif arr[i] == '*':
            tmp = int(arr[i - 1]) * int(arr[i + 1])
            arr[i - 1] = tmp
            arr.pop(i)
            arr.pop(i)

        elif arr[i] == '-':
            tmp = int(arr[i - 1]) - int(arr[i + 1])
            arr[i - 1] = tmp
            arr.pop(i)
            arr.pop(i)
        tot = arr[0]
        fx = ''
        tmpint = []
        for x in range(1, len(arr)):
            if arr[x] == '+':
                if tmpint:
                    if fx == '+':
                        tot += int(''.join(tmpint))
                        tmpint = []
                    elif fx == '*':
                        tot *= int(''.join(tmpint))
                        tmpint = []
                    elif fx == '-':
                        tot -= int(''.join(tmpint))
                        tmpint = []
                fx = '+'

            elif arr[x] == '*':
                if tmpint:
                    if fx == '+':
                        tot += int(''.join(tmpint))
                        tmpint = []
                    elif fx == '*':
                        tot *= int(''.join(tmpint))
                        tmpint = []
                    elif fx == '-':
                        tot -= int(''.join(tmpint))
                        tmpint = []
                fx = '*'

            elif arr[x] == '-':
                if tmpint:
                    if fx == '+':
                        tot += int(''.join(tmpint))
                        tmpint = []

                    elif fx == '*':
                        tot *= int(''.join(tmpint))
                        tmpint = []

                    elif fx == '-':
                        tot -= int(''.join(tmpint))
                        tmpint = []
                fx = '-'
            else:
                tmpint.append(arr[x])
        if fx == '+':
            tot += int(''.join(tmpint))

        elif fx == '*':
            tot *= int(''.join(tmpint))

        elif fx == '-':
            tot -= int(''.join(tmpint))
        if tot > my_max:
            my_max = tot
        arr = ori.copy()

