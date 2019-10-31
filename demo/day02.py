"""
使用变量保存数据并进行算术运算
"""

# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


"""
使用input()函数获取键盘输入
使用int()进行类型转换
用占位符格式化输出的字符串
"""

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

"""
使用type()检查变量的类型
"""

# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
"""


"""
运算符的使用
"""
# a = 5
# b = 10
# c = 3
# d = 4
# e = 5
# a += b
# a -= c
# a *= d
# a /= e
# print("a = ", a)

# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print(flag1 is True)
# print(flag2 is not False)

"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

# f = float(input("请输入华氏温度："))
# c = (f - 32) / 1.8
# print("%.1f 华氏温度 = %.1f 摄氏温度" % (f, c))


"""
输入半径计算圆的周长和面积
周长=2Πr
面积=Πr**2
"""
# import math
# r = float(input("请输入圆半径："))
# zc = 2*math.pi*r
# mj = math.pi * r ** 2
# print("圆半径：%.1f 的圆周长：%.1f" % (r, zc))
# print("圆半径：%.1f 的圆面积：%.1f" % (r, mj))

"""
输入年份 如果是闰年输出True 否则输出False
公历闰年的简单计算方法（符合以下条件之一的年份即为闰年，反之则是平年）
1。能被4整除而不能被100整除。
2。能被100整除也能被400整除。
"""
year = int(input("请输入年份"))
isRunYear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(year, "是闰年：", isRunYear, end="!")