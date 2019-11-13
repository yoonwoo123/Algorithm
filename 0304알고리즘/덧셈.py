import sys
sys.stdin = open("덧셈_input.txt")

S, X = map(int, input().split())

numbers = list(str(S))
res = []
for i in range(1, len(numbers)):
    SA = numbers[0:i]
    SB = numbers[i:len(numbers)]
    res.append(int(''.join(SA))+int(''.join(SB)))
    if X in res:
        print(f'{int("".join(SA))}+{int("".join(SB))}={X}')
        break
if X not in res:
    print('NONE')


print(SA)
print(SB)
print(f'#1{SA}')
# print(numbers[0:1])