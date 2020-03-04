import sys
sys.stdin = open("뉴스클러스터링_input.txt")

str1 = input()
str2 = input()

L1, L2 = len(str1), len(str2)
dict1 = {}
dict2 = {}
set1 = set()
set2 = set()
for i in range(L1-1):
    if str1[i].isalpha() and str1[i+1].isalpha():
        chars = str1[i:i+2].lower()
        set1.add(chars)
        if chars in dict1:
            dict1[chars] += 1
        else:
            dict1[chars] = 0
for i in range(L2-1):
    if str2[i].isalpha() and str2[i+1].isalpha():
        chars = str2[i:i + 2].lower()
        set2.add(chars)
        if chars in dict2:
            dict2[chars] += 1
        else:
            dict2[chars] = 0
inter = set1 & set2
union = set1 | set2
J1 = len(inter)
J2 = len(union)
for chars in union:
    if chars in dict1 and chars in dict2:
        J1 += min(dict1[chars], dict2[chars])
        J2 += max(dict1[chars], dict2[chars])
    else:
        if chars in dict1:
            J2 += dict1[chars]
        if chars in dict2:
            J2 += dict2[chars]
if J1 == 0 and J2 == 0:
    answer = 65536
else:
    answer = int(J1/J2 * 65536)
print(answer)