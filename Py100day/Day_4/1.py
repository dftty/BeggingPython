"""
生成器
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    a = fib(20)
    print(a)
    # for val in fib(20):
    #     print(val)

if __name__ == "__main__":
    main()