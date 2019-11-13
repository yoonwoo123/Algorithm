import sys
sys.stdin = open('은행업무_input.txt')

tc = int(input())
ott = ['0', '1', '2']

for T in range(1, tc+1):
    dec = list(input())
    tri = list(input())

    debranch = []
    trbranch = []

    origind = dec[:]
    origint = tri[:]
    for i in range(len(dec)):
        if dec[i] == '0':
            dec[i] = '1'
        else:
            dec[i] = '0'
        n = 0
        for j in range(len(dec)):
            n = n * 2 + int(dec[j])
        debranch.append(n)
        dec = origind[:]
    # print(debranch)

    for i in range(len(tri)):
        for num in ott:
            if num != tri[i]:
                tri[i] = num
                k = 0
                for j in range(len(tri)):
                    k = k * 3 + int(tri[j])
                trbranch.append(k)
                tri = origint[:]
    # print(trbranch)
    for num in debranch:
        if num in trbranch:
            print('#%d %d' % (T, num))
            break