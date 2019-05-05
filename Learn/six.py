# 自定义函数

def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-1] + result[-2])
    return result

print(fibs(10))


# 可变参数
def print_params(*params):
    print(params)

print_params('hello')
print_params('hello', 'world')

# 两个*号可以收集关键字参数, 参数为字典

def print_params_1(**params):
    print(params)

print_params_1(x = 1, y = 2)

# 练习
def print_params_2(x, y = 1, *first, **second):
    print(x, y, first, second)

print_params_2(1, 2, 3, 4, z = 2, k = 3)

def a(x = 1, y = 2, *first):
    print(x, y, first)

a(123, 32, 42)

pair = {(1, 2)}
print((1, 2) in pair)


# 递归实现阶乘
def factorial(n):
    if(n == 1):
        return 1
    return n * factorial(n - 1)


print(factorial(10))