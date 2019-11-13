# print(list(range(4,9)))
#
# a = {2,4,6}
# b = {2,4,8}
# print(list(a))
# print(a-b)
#
# phone_book = {'서울': '02', '경기': '031', '인천': '032'}
#
# print(phone_book.values())
# def my_bin(x):
#     result = []
#     while x >= 1:
#         if x%2 == 1:
#             result.append(1)
#         if x%2 == 0:
#             result.append(0)
#         x //= 2
#     return '0b'+''.join(map(str, result[::-1]))
# print(my_bin(8))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Circle:
#     def __init__(self, center, r):
#         self.x = center.x
#         self.y = center.y
#         self.r = r
#
#     def get_area(self):
#         return 3.14*self.r*self.r
#     def get_perimeter(self):
#         return 2*3.14*self.r
#     def get_center(self):
#         return self.x, self.y
#     def print(self):
#         print(f'Circle: {self.x, self.y}, r: {self.r}')
#
# p1 = Point(0, 0)
# c1 = Circle(p1, 3)
# print(c1.get_area())
# print(c1.get_perimeter())
# print(c1.get_center())
# c1.print()
# p2 = Point(4, 5)
# c2 = Circle(p2, 1)
# print(c2.get_area())
# print(c2.get_perimeter())
# print(c2.get_center())
# c2.print()
#
# r = 3
# a = r**2 *3.14
# b = r*r*3.14
# print(a)
# print(b)

def create_dict(keys, values):
    new_dict = {}
    while len(keys) > len(values):
        if len(keys) > len(values):
            values.append(None)
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict
print(create_dict(['a', 'b', 'c', 'd'], [1, 2, 3]))

# def dict_invert(dic):
#     invert = {}
#     new_key = []
#     b = []
#     for key, value in dic.items():
#         #print(value)
#
#         new_key.append(value)
#     for i in range(len(new_key)):
#         if new_key.count(new_key[i]) > 1:
#             b.append(i+1)
#             return b
#         else:
#             b.append(i)
#             return b
#         invert[value] = b # key대신 리스트를 넣자
#     print(new_key)
    # print(b)
    # return invert

# def dict_invert(dictionary):
#    result = {}
#    for value in dictionary.values():
#        result[value] = []
#    for key, value in dictionary.items():
#        if bool(result[value]):
#            result[value].append(key)
#        else:
#            result[value]=[key]
#
#    return result

# print(dict_invert({1: 10, 2: 20, 3: 30}))
# print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
# print(dict_invert({1: True, 2: True, 3: True}))

# cubic = {x: x**3 for x in range(1, 10)}
# print(cubic)

# class Dictfind:
#     def __init__(self):
#         {}
#         # print(name)
# #         self.name = name
#     def getfemale(self, *name):
#         self.name = name
#         res = {}
#         # return self.name
#         for k, v in self.name[0].items():
#             if k == 'female':
#                 res[k] = v
#                 # print('female :', end='')
#                 return res
                # return name[]
#         girl = []
#         for i in name:
#             if i == 'female':
#                 girl.append(i)
# #         return girl
# p1 = Dictfind()
# print(p1.getfemale({'female':'지원', 'male':'창오', 'female':'민지', 'none':'하리보'}))
class Dictfind:
    def __init__(self, *names):
        self.names = names
        print(names)
        # print(name)
#         self.name = name
    def getfemale(self):

        res = {}
        for k, v in self.names[0].items():
            if k == 'female':
                res[k] = v
                # print('female :', end='')
                return res
p1 = Dictfind({'female':'지원', 'male':'창오', 'female':'민지', 'none':'하리보'})
print(p1.getfemale())