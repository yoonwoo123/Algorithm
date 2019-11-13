import sys
sys.stdin = open("electricbus_input.txt")
testcases = input()
for T in range(int(testcases)):#{T+1}
    KNM = input()
    K_N_M = list(map(int, KNM.split()))
    K = K_N_M[0]
    N = K_N_M[1]
    M = K_N_M[2]
    charge = [0]*(N+1)
    present = K
    chtime = 0
    cnt = 0
    data = list(map(int, input().split()))
    for a in range(len(data)):
        charge[data[a]] += 1
    for i in range(N):
        if charge[present] == 1:
            present += K
            chtime += 1
            cnt = 0
        else:
            present -= 1
            cnt += 1
        if K-cnt == 0:
            print(f'#{T + 1} 0')
            break
        if present >= N:
            print(f'#{T + 1} {chtime}')
            break