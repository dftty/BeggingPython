"""
类
"""

class Student:
    
    # 这是类似C#的构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 前面加双下划线就是私有属性
        self.__hide = "private属性"

    def study(self, name):
        print("%s 正在学习 %s" % (self.name, name))
        print(self.__hide)

def main():
    stu1 = Student("lisi", 18)

    print("姓名：%s  \n年龄：%d" % (stu1.name, stu1.age))
    stu1.study(11)

    # 这样访问私有属性
    print(stu1._Student__hide)


if __name__ == "__main__":
    main()