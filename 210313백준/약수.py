import sys
sys.stdin = open("약수_input.txt")

cnt = int(input())
measure = sorted(list(map(int, input().split())))

print(measure[0] * measure[-1])
