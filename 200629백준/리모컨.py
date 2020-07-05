import sys, itertools
sys.stdin = open("리모컨_input.txt")

# 답과 가장 근접한 수를 고장나지 않은 숫자들로 조합하여 만들어내고
# 만든수의 길이 + 만든 수와 답의 차이를 더해주면 답

target = int(input())
TN = len(str(target))
remocon = set(x for x in range(10))
N = int(input())
if N == 10: # 전부 고장났으면 무조건 target - 100 이 답
    print(abs(target - 100))
else:
    if N == 0:
        print(min(abs(target - 100), TN))
    else:
        remocon = remocon - set(map(int, input().split()))
        # 순열로 만든 모든 수 중 target과 차이가 가장 적은 수 찾기
        ans = 999999
        # 답이 틀릴 수 있는 반례의 경우 생각해보면 자릿수가 바뀔 때
        # 못잡아준다. 그래서 4자릿수라 가정 시 만들 수 있는
        # 가장 큰 3자릿 수 만들수 있는 가장 작은 5자릿수를 염두하자.
        for perm in itertools.product(remocon, repeat= len(str(target))):
            if ans == len(str(target)): break
            num = int(''.join(map(str, perm)))
            ans = min(ans, abs(target - num) + len(str(num)))
        con_small = str(max(remocon)) * (len(str(target)) - 1)
        con_big = str(min(remocon)) * (len(str(target)) + 1)
        if con_big[0] == '0' and len(remocon) > 1:
            con_big = con_big.replace('0', str(sorted(remocon)[1]), 1)
        con1 = 9999999
        if con_small != '':
            con1 = abs(target - int(con_small))
        con2 = abs(target - int(con_big))
        print(min(abs(target - 100), ans, len(str(con_small)) + con1, len(str(con_big)) + con2))