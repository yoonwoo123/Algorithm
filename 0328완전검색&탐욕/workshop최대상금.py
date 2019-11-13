import sys
sys.stdin = open("최대상금_input.txt")

def win(numbers, dep):
    global max_num

    if dep != ex+1:
        if ''.join(map(str, numbers)) in depmemo:
            return
        depmemo.append(''.join(map(str, numbers)))

        for i in range(N):
            for j in range(i+1, N):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                win(numbers, dep + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]
    else:
        numbers = ''.join(map(str, numbers))

        if int(numbers) > max_num:
            max_num = int(numbers)
            return

tc = int(input())
for T in range(1, tc+1):
    numbers, ex = input().split()
    numbers = list(map(int, list(numbers)))
    N = len(numbers)
    max_num = 0
    ex = int(ex) # 횟수
    depmemo = []
    win(numbers, 1)
    depmemo = list(map(int, depmemo))
    print('#%d %d' % (T, max_num))
