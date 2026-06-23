class calculator:
    def __init__(self, a, b):   # fixed here
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)

s = calculator(10, 20)
s.add()
s.sub()
s.mul()
s.div()