import sys, collections
sys.stdin = open("force2048_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    arr = list(map(int, input().split()))
    chk = [0] * 12 # 2의 11승 = 2048
    nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

    if 2048 in arr:
        print('YES')
    else:
        for num in arr:
            if num <= 2048:
                # print(nums.index(num))
                chk[nums.index(num)] += 1 # 몇승인지 그 값을 올려주자.
        # print(chk)
        for i in range(11):
            chk[i + 1] += chk[i] // 2
        if chk[-1] > 0:
            print('YES')
        else:
            print('NO')