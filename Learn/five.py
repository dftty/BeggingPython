# 导入模块
from math import floor

print(floor(3.14))

# 赋值语句技巧
x, y, z = 1, 2, 3

# 可以交换多个变量的值 可以用于交换数组中的两个数
x, y = y, x
arr = [1, 2, 3, 4, 5]
arr[0], arr[1] = arr[1], arr[0]
print(x, y, arr)

x, y, *z = 1, 2, 3, 4, 5
print(x, y, z)

# 链式赋值
x = y = floor(3.15)
# 类似于
# y = floor(3.15)
# x = y

# if条件判断中，下列值都视为False
# False None 0 "" () [] {}

# 三目运算符
status = "friend" if x == 1 else "stranger"
print(status)

# == 用来检查两个对象是否相等， is用来检查两个对象是否相同
x = y = [1, 2]
z = [1, 2]
print(x == z, x == y, x is y, x is z)

# for循环迭代 range第三个参数代表每次递增的值
x = [1, 2, 3, 4, 5]
for i in range(0, len(x), 2):
    print(x[i])

# enumerate 返回索引-值对的方法
for i, value in enumerate(x):
    print(i, value)

# for else 语句，在没有break时执行else语句

for i in range(100):
    if i > 100:
        print("break")
        break
else :
    print("for loop finish")


# pass del exec
# pass 语句不执行任何操作