import sys
sys.stdin = open("좋은단어_input.txt")
# input = sys.stdin.readline
#
# N = int(input())
# ans = 0
# for _ in range(N):
#     word = input().strip()
#     s = []
#     for char in word:
#         if s and s[-1] == char:
#             s.pop()
#         else:
#             s.append(char)
#     if not s: ans += 1
# print(ans)

num_of_good_words = 0

for _ in range(int(input())):
	word, temp = input(), ""
	while word != temp:
		temp, word = word, word.replace("AA", "").replace("BB", "")
	if not word:
		num_of_good_words += 1

print(num_of_good_words)