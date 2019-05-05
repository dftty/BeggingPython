# 字典

# 初始化方法
d = dict([('name', 'Gumby'), ('age', 42)])
print(d)

del d["name"]
print(d)

# 将字符串的格式设置功能用于字典,该方法常用于模板系统

phonebook = {'Beth' : '9102', 'Alice' : '2341', 'Cecil' : '3258'}
print("'Cecil' 's phone number is {Cecil}".format_map(phonebook))

# fromkeys 创建一个新字典，其中包含指定的键，每个键对应的值是None

phonebook = dict.fromkeys(['name', 'age'])
print(phonebook)

phonebook = {'name' : 'Alice', 'Age' : '2341', 'Address' : '3258'}
# get 获取指定键的值，如果没有则返回None，也可以指定默认值
print(phonebook.get('name'))

it = phonebook.items()

for k in it :
    print(k[0], k[1])

# keys 方法返回键的列表
keys = phonebook.keys()
print(keys)
for k in keys:
    print(k)

# pop 获取指定键的值，并从字典中删除
print(phonebook.pop('name') + '\n')

# setdefault 和get类似，但是如果不存在指定键时，还会向字典中添加该键，默认值为None，也可以指定值
phonebook.setdefault('name', 16)
print(phonebook)

# update 

phonebook.update({'name' : 'Bob', 'phonenumber': '12124124'})
print(phonebook)

# values 返回字典的值的字典视图，可能包含重复的值
print(phonebook.values())