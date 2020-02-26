import sys, re
sys.stdin = open("캐시_input.txt")

cacheSize = int(input())
cities = list(input().split())

answer = 0
cache = []
for city in cities:
    if city.lower() in cache:
        cache.remove(city.lower())
        cache.append(city.lower())
        answer += 1
    else:
        answer += 5
        if cacheSize != 0:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city.lower())
print(answer)