import itertools
numbers = "011"

def solution(numbers):
    def isPrime(number):
        if number < 2: return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0: return False
        return True

    answer = 0
    arr = list(numbers)
    candidates = set()

    for i in range(1, len(numbers)+1):
        for comb in itertools.permutations(arr, i):
            candidates.add(int(''.join(comb)))

    for candidate in candidates:
        if isPrime(candidate): answer += 1

    return answer

print(solution(numbers))