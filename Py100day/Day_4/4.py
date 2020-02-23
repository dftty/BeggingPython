"""
类
"""

class Hero:

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    # 静态方法
    @staticmethod
    def move():
        print("Hero")

def main():
    h1 = Hero("霹雳", 100)
    print(h1.name)
    h1.name = 1

    # 调用静态方法的两种方式
    Hero.move()
    h1.move()
    
    # age相当于动态绑定的属性
    h1.age = 10
    print(h1.name)
    print(h1.age)
    # print(h1.mp) 没有绑定直接访问会报错



if __name__ == "__main__":
    main()