p = "()))((()"
def check(string): # 올바른 문자열인지 체크
    s = []
    for char in string:
        if char == '(':
            s.append(char)
        elif char == ')':
            if s != []:
                s.pop()
            else:
                return False # 올바르지 않다.
    return True # 올바른 문자다.

def solve(w):
    if w == '': return w
    tmp = ''
    cnts = [0] * 2
    for i in range(len(w)):
        tmp += w[i]
        if w[i] == '(':
            cnts[0] += 1
        else:
            cnts[1] += 1
        if cnts[0] == cnts[1]:
            u = tmp
            if i != len(w)-1:
                v = w[i+1:]
            else:
                v = ''

            if check(u):
                return u + solve(v)
            else:
                return '(' + solve(v) + ')' + reverse(u[1:-1])

def reverse(string):
    tmp = ''
    for char in string:
        if char == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp

def solution(p):
    if check(p): return p
    return solve(p)

print(solution(p))