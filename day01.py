#！/usr/bin/env python
# time: 2018/12/12 13:39
# author: fangzy
# file name: day01.py

#测试控制台输出
# print("123")
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

