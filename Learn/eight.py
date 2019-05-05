# 异常

# 抛出异常
# raise Exception
# raise Exception("Error Message")

# 自定义异常

class LearnException(ZeroDivisionError):
    pass


try :
    div = 1 / 0
except (LearnException):
    print("an error accur")
except Exception as e:
    print("Invalid input:", e)


for i in range(10):
    print(i)
else:
    print("Fiish")