#！/usr/bin/env python
# time: 2018/12/12 13:39
# author: fangzy
# file name: 基础.py

# True 非0的数或非空都是True
print(bool(1))
# False
print(bool(0))
# True
print(bool(-1))
# True
print(bool("abc"))
# False
print(bool(""))
# True
print(bool([1,2,3]))
# False
print(bool([]))
# True
print(bool({1,2,3}))
# False
print(bool({}))

#测试控制台输出
print("123")
# print("123","456" + str(10+2))

# 测试输入
# name = input("请输入你的姓名:")
# # 这种方式输出是输出两个字符串 中间空格隔开
# print("你输入的姓名：",name)
# # 输出拼接之后的字符串
# print("你输入的姓名："+name)



# 测试字符串的格式化

# 字符串的格式化方式有两种
# 方式一 %s:字符串   %d:数字   %f:浮点数  %x:16进制整数
# %% 显示%，%.1f  小数点后保留一位小数
# str1 = "你好 %s ,你的收益是 %.1f%%" % ("张三", 12.123)
# print(str1)
# str = "你好 %s ,欢迎加入我们 %s 大家庭" % ("张三", "睿歆")
# print(str)

# 方式二 format() 函数
# 用format函数的参数依次替换字符串中的占位符 {0}、{1}。。。
# {1:.1f} : 第二个参数小数点后保留一位小数
# str2 = "{0} 你好，你本次成绩提升了 {1:.1f}%".format("张三", 12.123)
# print(str2)

nameList = ["张三", "卡卡", "里斯", "凯莉", "娟娟", "卡克斯"]
# 输出集合的长度
print(len(nameList))
print(nameList.__len__())
# 输出集合的内容
print(nameList)
# 输出集合的元素
print(nameList[0])
# 向集合最后追加一个元素
nameList.append("aaa")
# 获取最后一个元素可以用元素的下标或者-1依次类推访问倒数第二个、倒数第三个可用-2、-3
print(nameList[len(nameList)-1], nameList[-1])



# 字符串前加r不转义
print(r"hello \n world")


# 集合
print(type({1, 2, 3}))
# 定义一个空集合
set()
# 输出集合的长度
print(len({1, 2, 3, 4}))
# 1 在不在这个集合中
print(1 in {1, 2, 3})
# 4 在不在这个集合中
print(4 not in {1, 2, 3})
# 集合的差集，前面集合排除后面集合后的集合
print({1, 2, 3, 4} - {2, 3})
# 集合的交集,两个集合都用的元素
print({1, 2, 3, 4} & {2, 3})
# 集合的并集
print({1, 2, 3, 4} | {2, 3, 5})


# 字典
# 定义一个字典,key不能重复，重复的后面的覆盖前面的
{"key1": "val1", "key2": "val2"}

# 类型判断
# 1、type（1）
print(type(1))
# 2、isinstance(1,int)
print(isinstance(1, int))
# 1的类型是后面元素中的任何一个都返回True

print(isinstance(1, (int, str, tuple)))

