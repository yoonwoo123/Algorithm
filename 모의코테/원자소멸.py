import sys
sys.stdin = open("원자소멸_input.txt")

tc = int(input())

dx = [0,0,-0.5,0.5]
dy = [0.5,-0.5,0,0]
for T in range(1, tc+1):
    N = int(input())
    apos = [list(map(int, input().split())) for _ in range(N)]

    tot = 0

    while apos:
        i = 0
        while True:
            x = apos[i][0]
            y = apos[i][1]
            d = apos[i][2]

            nx, ny = x + dx[d], y + dy[d]

            if nx < -1000 or ny < -1000 or nx > 1000 or ny > 1000:
                del apos[i]
                i -= 1
            else:
                apos[i][0] = nx
                apos[i][1] = ny
            i += 1
            if i == len(apos): break
        if len(apos) > 1:
            i = 0
            apos.sort()
            while (i < len(apos)-1):
                if [apos[i][0], apos[i][1]] == [apos[i+1][0], apos[i+1][1]]:
                    tot += apos[i][3]
                    tot += apos[i+1][3]
                    apos[i][3] = 0
                    apos[i+1][3] = 0
                i += 1
                # if i == len(apos) - 1: break
            i = 0
            while True:
                if apos[i][3] == 0:
                    del apos[i]
                    i -= 1
                i += 1
                if i == len(apos): break
        else:
            break

    print(f'#{T} {tot}')
