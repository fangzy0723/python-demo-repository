"""
用for循环实现1~100求和
"""

"""
需要说明的是上面代码中的range类型，range可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的，例如：
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
"""
# count = 0
# for i in range(101):
#     count += i
# print("1-100的和：%d" % count)

"""
用for循环实现1~100之间的偶数求和
"""
# count = 0
# for i in range(101):
#     if i % 2 == 0:
#         count += i
# print("1-100的偶数和：%d" % count)

"""
用for循环实现1~100之间的偶数求和
"""
# count = 0
# for i in range(0, 101, 2):
#     count += i
# print("1-100的偶数和：%d" % count)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
# # 生成一个1-100的随机数
# random_num = random.randint(1, 100)
# print("产生的随机数：",random_num)
# while True:
#     value = int(input("请输入一个数字："))
#     if value > random_num:
#         print("大了！")
#     elif value < random_num:
#         print("小了！")
#     else:
#         print("猜对了")

"""
输出乘法口诀表(九九表)
"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (i, j, i*j), end="\t")
#     print()

