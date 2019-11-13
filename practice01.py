# 01
# word = 'python'
# indexing = word[-2:-5:-1]
# print(indexing)

# 02
#my_int = 3
# print(isinstance(my_int, int))
#print(type(my_int) == int)

# 04
# fruits = {'apple' : '사과', 'banana' : '바나나'}
#
# a = fruits.get('apple')
# b = fruits.get('cherry')
# c = fruits.get('melon', True)
# d = {a : b}
#
# if c :
#     print(d)

# 08
# result = 4 + True + False + 5
# print(result)

# 13
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(4))

# 15
# name = 'hong'
#
# class Person:
#     name = 'choi'
#
#     def greeting(self):
#         print(name)
#
# p1 = Person()
# p1.name = 'kim'
# p1.greeting()

# 16
# def func(a, b = 1, c = 2, *args, **kwargs):
#
#     d = sum([n*2 for n in args if n >=2])
#     e = sum([v*v for k, v in kwargs.items()])
#
#     return a + b + c + d + e
# print(func(9, 4, 2, 3, 1, 7, d = 3, e = 6))

# 20
# my_complex = 3 + 4j
# my_list = [1, 2, 3]
# my_dict = {1:1, 2:2}
#
# my_complex.real
# print(my_complex.real)
# my_list.sort()
# print(my_list.pop())
# print(my_dict.keys())

# 22
# d = {'a' : 1, 'b' : 2}
# a1 = d.update({'c' : 3})
# a2 = a1
# print(len(d))

# 24
# d1 = {'d' : dict()}
# d2 = dict(d={})
#
# print(d1 == d2)
# print(len(d1))
# print(len(d2))
# print(id(d1))
# print(id(d2))
a = 6
b = 7
c = a
print(c)