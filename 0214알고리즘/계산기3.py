import sys
sys.stdin = open("계산기3_input.txt")

tc = 10
isp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, "(" : 0}
icp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, "(" : 3}
f_x = ['+', '-', '*', '/', '.']
for T in range(tc):
    N = int(input())
    data = input()
    s = []
    pri = []
    for i in range(len(data)):
        if data[i] in f_x and len(s) == 0:
            s.append(data[i])
            continue
        if data[i] == '(':
            s.append(data[i])
            continue
        if data[i].isdecimal():
            pri.append(data[i])
            continue
        if data[i] == ')':
            while s[-1] != '(':
                pri.append(s.pop())
            s.pop()
            continue
            # if len(s)==0:
            #     break
        if icp[data[i]] > isp[s[-1]]:
            s.append(data[i])
        else:
            pri.append(s.pop())
            s.append(data[i])
    while len(s) > 0:
        if s[-1] != '(' or s[-1] != ')':
            pri.append(s.pop())
    st = []
    for i in range(len(pri)):
        # if data[i] != '+' and data[i] != '-' and data[i] != '*' and data[i] != '/' and data[i] != '.':
        if pri[i] not in f_x:
            st.append(pri[i])
        if pri[i] == '+':
            if len(st) < 2:
                print(f'#{T + 1} error')
                break
            a = int(st.pop())
            b = int(st.pop())
            st.append(b + a)
        if pri[i] == '-':
            if len(st) < 2:
                print(f'#{T + 1} error')
                break
            a = int(st.pop())
            b = int(st.pop())
            st.append(b - a)
        if pri[i] == '*':
            if len(st) < 2:
                print(f'#{T + 1} error')
                break
            a = int(st.pop())
            b = int(st.pop())
            st.append(b * a)
        if pri[i] == '/':
            if len(st) < 2:
                print(f'#{T + 1} error')
                break
            a = int(st.pop())
            b = int(st.pop())
            st.append(b // a)
        if i == len(pri)-1:
            # if len(st) != 1:
            #     print(f'#{T + 1} error')
            #     break
            # else:
            print(f'#{T + 1} {st.pop()}')
