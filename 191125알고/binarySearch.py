import sys
sys.stdin = open("binarySearch_input.txt")

def binarySearch(arr, target):
    global cnt
    left = 0
    right = len(arr) - 1

    while left <= right:
        cnt += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = list(map(int, input().split()))
target = int(input())

cnt = 0
res = binarySearch(arr, target)
print('cnt :', cnt)
print('idx :', res)
print('target :', arr[res])