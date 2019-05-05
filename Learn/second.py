
# 序列和嵌套序列
Mary = ["First", 24]
Jhon = ["Second", 26]

database = [Mary, Jhon]
print(database)
print(database[0])

# 支持负数索引， -1为最后一个元素
print(database[-1])

# 切片 切片取的元素是左包右闭的 数组下标从0开始
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[3:6]

# 这样表示从第三个到最后一个元素
numbers[3:]

# 还可以添加一个参数表示步长, 步长可以是负数，表示从右向左提取
numbers[3::2]
numbers[10:0:-2]

# 列表乘法 表示序列重复x次
numbers = [0] * 10
print(numbers)
numbers[9] = 678

# 运算符in用于检查特定的值是否包含在序列中
permission = ["first", "second"]
print("first" in permission)

# 长度最大值和最小值
print(len(numbers))
print(max(numbers))
print(min(numbers))

# 使用字符串来创建一个列表，因为字符串是不可修改的，创建列表后就可以修改
names = list("helloworld")
print(names)

# 列表删除和给切片赋值
names = ["Alice", "beth", "Cecil", "Earl"]
# del names[1]
del names[1:3]
print(names)

names = list("hellomary")
names[5:] = list("world")
print(names)

# 列表方法

numbers = [1, 2, 3]
numbers.append(4)
numbers.insert(1, 5)
print(numbers)
numbers.clear()
print(numbers)

# 这里append进去的是这个数组本身
numbers.append([1, 2, 3, 4])
print(numbers)

numbers = [1, 2, 3, 3, 4]
# 下面这句话右边也可以写成 numbers[:] 或 list(numbers),相当于复制一个新的数组
n = numbers.copy()
print(n)

# count函数用于计算指定的元素在列表中出现的次数
print(numbers.count(3))

# extend 可以将多个值附加到列表末尾
numbers.extend([5, 6, 7])
print(numbers)

# index 查找在列表中出现的第一次的索引,没有找到会报异常
print(numbers.index(3))

# pop pop还可以指定下标
print(numbers.pop())
# numbers.pop(3)

# remove 删除指定的值,这个值是列表中找到的第一个
numbers.remove(3)
print(numbers)
numbers[2:3] = []
print(numbers)

# reverse 反转数组
numbers.reverse()
print(numbers)

# sort 就地排序, 没有返回值
numbers.sort()
print(numbers)

# sorted 函数，返回一个排序后的副本
n = sorted(numbers)
n.reverse()
print(n)
print(numbers)

# 指定关键字排序
numbers = [[1, 2], [4, 6], [2, 3], [8, 1], [3, 4]]
numbers.sort(key = lambda numbers:numbers[0], reverse = True)
print(numbers)

# 元组 表示不可修改的列表
n = (1, 2, 3)
print(n)

# 一个元素的元组必须加一个逗号
n = (42,)
print(n)

# tuple 将序列转换为元组
n = tuple(numbers)
n[0][1] = 3
print(n)