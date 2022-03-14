class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

test(1,2)
print(test.get_a(1))
print(test.get_b(2))