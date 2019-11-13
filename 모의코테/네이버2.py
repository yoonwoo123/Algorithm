import sys
sys.stdin = open("네이버1_input.txt")

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            print(result)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    result.sort()
    # print(''.join(map(str, result[2])))
    return ''.join(map(str, result[K-1]))

arr = list(map(int, input().split()))
K = int(input())
print(permute(arr))