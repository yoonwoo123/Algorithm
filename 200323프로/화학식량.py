import sys
sys.stdin = open("화학식량_input.txt")
sys.setrecursionlimit(10**6)

W = {'H': 1, 'C': 12, 'O': 16}
stk =[]
push, pop = stk.append, stk.pop

for c in f'({input()})':
    print(c)
    if c == '(':
        push('(')
    elif c == ')':
        w = 0
        t = pop()
        while t != '(':
            w += t
            t = pop()
        push(w)
    elif c.isdigit():
        push(pop() * int(c))
    else:
        push(W[c])

print(pop())
