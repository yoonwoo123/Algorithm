import sys
sys.stdin = open("세로로말해요_input.txt")

tc = int(input())
for T in range(1, tc+1):
    words = []
    res = []
    flag = 0
    for i in range(5):
        words.append(list(input()))
    while flag != 5:
        flag = 0
        for x in range(5):
            if len(words[x]) != 0:
                res.append(words[x].pop(0))
            else:
                flag += 1
    print("#%d %s" % (T, ''.join(res)))
