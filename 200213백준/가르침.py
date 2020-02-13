import sys, itertools
sys.stdin = open("가르침_input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0
if K < 5:
    print(0)
else:
    words = [list(input().strip()) for _ in range(N)]
    chars = {'a':1, 'c':1, 'i':1, 'n':1, 't':1}
    alphas = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
    K -= 5 # 필수5개 가르침
    combs = list(itertools.combinations(alphas, K))

    for comb in combs:
        my_dict = {}
        for char in comb:
            my_dict[char] = 1
        cnt = 0
        for word in words:
            LW = len(word)
            flag = 0
            for i in range(4, LW-4):
                if word[i] not in chars and word[i] not in my_dict:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1
        answer = max(cnt, answer)
    print(answer)