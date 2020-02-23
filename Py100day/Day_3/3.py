"""
前20个斐波那契数
"""

arr = [0] * 20
arr[0] = arr[1] = 1

for i in range(2, 20):
    arr[i] = arr[i - 1] + arr[i - 2]

for i in range(len(arr)):
    print("第%d个斐波那契数是%d" % (i + 1, arr[i]))

