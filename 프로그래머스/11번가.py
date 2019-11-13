import itertools

a = [x for x in range(8)]
perm = list(itertools.permutations(a, 8))
print(perm)
print(len(perm))