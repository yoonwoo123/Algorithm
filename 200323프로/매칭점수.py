import sys, re
sys.stdin = open("매칭점수_input.txt")

word, pages = input(), [input() for _ in range(2)]

answer = 0
p = re.split('\W', pages[0])
print(p)
