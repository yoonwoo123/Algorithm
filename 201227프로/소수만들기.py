import itertools

nums = [1,2,7,6,4]

def solution(nums):
    def isPrime(number):
        if number < 2: return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0: return False
        return True

    answer = 0
    for comb in itertools.combinations(nums, 3):
        if isPrime(sum(comb)): answer += 1

    return answer

print(solution(nums))