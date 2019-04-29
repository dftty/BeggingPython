# TODO 字符串格式化

# 字符串方法

# center方法在字符串两边填充字符,第一个参数为字符串填充的结果长度，第二个参数为填充字符串，默认左右填充空格
s = "aa".center(9, "*")
print(s)

# find 寻找指定字符串的第一个字符索引, 没有找到返回-1
print("with a".find("ithi"))

# join合并序列的元素
dirs = '', 'user', 'bin', 'env'
print('\\'.join(dirs))

# lower upper
print("AAA".lower())
print("bbb".upper())

# replace 第三个参数是替换多少个
a = "Hello world world".replace("world", "dftty", 1)
print(a)

# strip 去掉左右指定字符串，默认空格
print("  asdf  ".strip())


# 字典
book = {"Alice" : 100, "Bob" : 200}
print(book)
print("ss" in book)