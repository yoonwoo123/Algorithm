import sys
sys.stdin = open("늘어지는소리_input.txt")

tc = int(input())
for T in range(1, tc+1):
    word = list(input())
    H = int(input())
    hypon = list(map(int, input().split()))
    hypon = sorted(hypon)[::-1]
    # print(hypon)
    for num in hypon:
        word.insert(num, '-')
    print("#%d %s" % (T, ''.join(word)))