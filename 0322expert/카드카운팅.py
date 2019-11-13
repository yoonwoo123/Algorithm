import sys
sys.stdin = open('카드카운팅_input.txt')

tc = int(input())
for T in range(1, tc+1):
    spade = []
    dia = []
    heart = []
    clover = []
    flag = 0
    cards = list(input())
    S = 13
    D = 13
    H = 13
    C = 13
    for i in range(0, len(cards), 3):
        if cards[i] == 'S':
            num = int(cards[i+1] + cards[i+2])
            if num in spade:
                print('#{} ERROR'.format(T))
                flag = 1
                break
            spade.append(num)
            S -= 1
        elif cards[i] == 'D':
            num = int(cards[i + 1] + cards[i + 2])
            if num in dia:
                print('#{} ERROR'.format(T))
                flag = 1
                break
            dia.append(num)
            D -= 1
        elif cards[i] == 'H':
            num = int(cards[i + 1] + cards[i + 2])
            if num in heart:
                print('#{} ERROR'.format(T))
                flag = 1
                break
            heart.append(num)
            H -= 1
        elif cards[i] == 'C':
            num = int(cards[i + 1] + cards[i + 2])
            if num in clover:
                print('#{} ERROR'.format(T))
                flag = 1
                break
            clover.append(num)
            C -= 1
    if flag == 0:
        print('#{} {} {} {} {}'.format(T, S, D, H, C))