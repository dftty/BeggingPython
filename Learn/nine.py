# 构造函数

class FooBar:
    def __init__(self):
        super().__init__()
        self.solver = 42

class First:
    def __init__(self):
        super().__init__()
        self.fir = "fir"

class Child(FooBar, First):
    def __init__(self):
        super().__init__()
        print(self.solver, self.fir)

f = Child()
