import sys
sys.stdin = open("도약_input.txt")

N = int(input())
leafs = []
for i in range(N):
    leafs.append(int(input()))
leafs = sorted(leafs)
cnt = 0
for pos in range(len(leafs)-2): # 첫번째 잎 위치
    for jmp in range(pos+1, len(leafs)-1): # 두번째 잎 위치
        term = leafs[jmp] - leafs[pos]
        for last in range(pos+2, len(leafs)): # 세번째 잎 위치
            if term <= leafs[last] - leafs[jmp] <= term * 2:
                cnt += 1
                continue
            else:
                continue
print(cnt)