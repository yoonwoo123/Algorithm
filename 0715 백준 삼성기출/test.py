import collections

q = collections.deque([[2,3,4]])

q.append([1,2,3])
q.appendleft([2,3,3])
q.extend([[1,2,5]])
q.pop()
print(q)

a = ['5', '8']
b = ['7']
# a = [[1,2,3]]
# a.extend([[2,3,2]])
# a.appendleft([1,3,3])
# a.pop(1)
print(''.join(b))


print(a)

