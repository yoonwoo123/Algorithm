import sys
sys.stdin = open("상자포장_input.txt")

# A 는 큰상자에서 작은상자포장
# B 는 작은상자에서 큰상자 포장

def wrap(no, lastA, lastB, tot):
    global sol
    if no >= N:
        if tot > sol:
            sol = tot
        return

    else:
        if boxs[no] < lastA:
            # rec[no] = 1
            wrap(no + 1, boxs[no], lastB, tot + boxs[no])
        # 이렇게 삼중으로 짰을 때 elif를 쓰면 안된다 그러면 if문을 실행안하고 통과할수있기때문
        # 첫번째 if문의 wrap함수를 빠져나오고 밑에서 또 들어갈수도 있기때문
        if boxs[no] > lastB:
            # rec[no] = 2
            wrap(no + 1, lastA, boxs[no], tot + boxs[no])
        # 현재 상자를 포장하지 않기
        wrap(no+1, lastA, lastB, tot)



tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    # rec = [0] * N
    boxs = list(map(int, input().split()))
    sol = 0
    wrap(0, 1001, 0, 0) # 0번박스부터, A초기값2000, B초기값 0

    if sol:
        print(sol)