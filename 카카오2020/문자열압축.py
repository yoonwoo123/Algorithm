import sys
sys.stdin = open("문자열압축_input.txt")

s = input()

answer = 0
LS = len(s)
mymin = 99999999
if LS == 1:
    answer = 1
else:
    for cnt in range(1, LS//2 + 1):
        char = s[0:cnt]
        n = 0 # 반복된 횟수
        res = ''
        for i in range(0, LS, cnt):
            # print(s[i:i+cnt])
            nchar = s[i:i+cnt]
            if char == nchar:
                n += 1
            else:
                if n == 1:
                    res += char
                else:
                    res += str(n) + char
                n = 1
                char = nchar

        if n == 1:
            res += char
        else:
            res += str(n) + char
        L = len(res)
        if mymin > L:
            mymin = L
    answer = mymin
print(answer)

