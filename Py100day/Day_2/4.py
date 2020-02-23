def div(a, b):
    if a % b == 0:
        return b
    return div(b, a % b)

a = int(input("a = "))
b = int(input("b = "))

x = div(a, b)
print("最大公约数是：%d" % x)
