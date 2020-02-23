import math

# ** 是幂运算符
print(2 ** 3)

"""
这是多行注释
"""

# 这里需要引入math包才可以调用该方法 // 是整除运算符
print(math.ceil(3 // 2))



x = "Hello, "
y = "world"
print(x + y)

# repr将转义符也输出为字符串
print(repr("Hello, \nworld!"))
print(str("Hello, \nworld!"))


# 长字符串可以使用三个引号, 下面字符串输出时会换行
print("""Hello
 World
 , Yes
""")

# 如果想要在多行中表示一行字符串, 在每行末尾加反斜杠
print("Hello\
 World!")

# 在字符串前加r表示每个字符都保持原样
print(r"c:\nowhere")