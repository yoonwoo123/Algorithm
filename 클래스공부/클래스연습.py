class FourCal:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def sub(self):
        return self.num1 - self.num2

    def div(self):
        return self.num1 / self.num2

class MoreFourCal(FourCal):
    def pow(self):
        return self.num1 ** self.num2

class SafeFourCal(FourCal):
    def div(self):
        try:
            return self.num1 / self.num2
        except:
            return 0

a = FourCal(4, 2)
b = MoreFourCal(3, 4)
c = SafeFourCal(4, 0)
print(b.pow())
print(a.num1)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(c.div())