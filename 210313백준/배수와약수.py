import sys
sys.stdin = open("배수와약수_input.txt")

while True:
    answer = ''
    A, B = map(int, input().split())
    if A == 0 and B == 0: break
    if B % A == 0: answer = 'factor'
    elif A % B == 0: answer = 'multiple'
    else: answer = 'neither'
    print(answer)