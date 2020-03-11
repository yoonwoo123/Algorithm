import sys
sys.stdin = open("압축_input.txt")

msg = input()

answer = []
my_dict = {chr(64 + x) : x for x in range(1, 27)}

L = len(msg)
val = 27
i = 0
while i < L:
    j = 1
    while i + j < L+1:
        w = msg[i:i+j]
        if w not in my_dict:
            answer.append(my_dict[msg[i:i+j-1]])
            my_dict[w] = val
            val += 1
            break
        j += 1
        if i + j >= L+1:
            w = msg[i:i+j]
            if w not in my_dict:
                answer.append(my_dict[msg[i:i+j-1]])
                my_dict[w] = val
                val += 1
            else:
                answer.append(my_dict[w])
            break
    i += j - 1
print(my_dict)
print(answer)