from abc import ABC, abstractmethod

"""

"""

class Person:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        self.__inaccess()
        print("Hello, world! I'm {}".format(self.name))
    
    # 私有方法定义
    def __inaccess(self):
        print("you can't see me")

foo = Person()

# 私有方法名前加下划线类名可以访问私有方法
foo._Person__inaccess()

bar = Person()
foo.set_name("Luke Skywalker")
bar.set_name("Anakin Skywalker")

foo.greet()
bar.greet()

# 继承
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ["SPAM"]

f = SPAMFilter()
f.init()
print(f.filter(["SPAM", "SSSS", "SPAM", "egg"]))

# 判断是否子类
print(issubclass(SPAMFilter, Filter))

# 该属性可以知道基类
print(SPAMFilter.__bases__)