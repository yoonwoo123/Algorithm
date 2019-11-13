import sys, collections
sys.stdin = open("컨테이너_input.txt")

# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# 화물을 싣지 못한 트럭이 있을 수도 있고,
# 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
# 컨테이너를 한개도 못옮기는 경우는 max(containers) 가 min(weights) 보다 작을 때이다.
tc = int(input())
for T in range(1, tc+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split())) # 1, 5, 3
    containers = list(map(int, input().split())) # 8, 3
    weights.sort() # 1, 3, 5
    containers.sort() # 3, 8
    tot = 0
    for j in range(M):
        tmp = 0
        i = 0
        while True:
            if containers[j] >= weights[i]:
                if i == len(weights)-1:
                    tmp = weights[i]
                    tot += tmp
                    weights.pop(i)
                    break

                tmp = weights[i]
                i += 1
                continue
            elif tmp == 0:
                break
            tot += tmp
            weights.pop(i-1)
            break
    print('#%d %d' % (T, tot))