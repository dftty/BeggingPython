"""
正数的反转
"""

a = int(input("请输入一个正整数："))
res = 0
if a > 0:
    while a > 0:
        tmp = a % 10
        a = a // 10
        res = res * 10 + tmp
    print(res)
else:
    print("输入格式错误")
