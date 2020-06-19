from a import Person

b = Person(2, 7)
print(b.plus())

class Person2(Person):

    def __init__(self, c):
        self.c = c

    def minus(self):
        return self.a + self.b - self.c

c = Person2(4, 1, 3)

print(c.plus(), c.minus())