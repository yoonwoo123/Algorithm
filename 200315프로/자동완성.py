import sys, re
sys.stdin = open("자동완성_input.txt")

words = list(input().split())

answer = 0
words.sort()
L = len(words)
words.append('')
for i in range(L):
    bword, word, aword = words[i-1], words[i], words[i+1]
    WL = len(word)
    cnt = 0
    for j in range(1, WL+1):
        cnt += 1
        if word[:j] == bword[:j]: continue
        if word[:j] != aword[:j]: break
    answer += cnt
print(answer)