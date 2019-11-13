import sys
sys.stdin = open("다이아몬드_input.txt")

tc = int(input())

for T in range(1, tc+1):
    char = list(input())
    if len(char) == 1:
        print('..#..')
        print('.#.#.')
        print("#.%s.#" % (char[0]))
        print('.#.#.')
        print('..#..')
    else:
        for i in range(len(char)):
            print('..#.', end="")
        print('.')
        for i in range(len(char)*2):
            print('.#', end="")
        print('.')
        for i in range(len(char)):
            print('#.%s.' % (char[i]), end="")
        print('#')
        for i in range(len(char)*2):
            print('.#', end="")
        print('.')
        for i in range(len(char)):
            print('..#.', end="")
        print('.')