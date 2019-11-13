import sys
sys.stdin = open("퍼펙트셔플_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    cards = list(input().split())
    if N % 2 == 0:
        print('#{}'.format(T), end=" ")
        for i in range(N//2):
            print(cards[i], end=" ")
            print(cards[N//2 + i], end=" ")
        print()
    else:
        print('#{}'.format(T), end=" ")
        for i in range(N//2):
            print(cards[i], end=" ")
            print(cards[N//2 + 1+i], end=" ")
        print(cards[N//2])