# flag = True
# if flag:
#     print("为真的时候输出")
# else:
#     print("为假的时候输出")


# name = "fangzy"
# if name == "fangzy":
#     print("name是fnagzy")
# elif name == "xiaofang":
#     print("name是小方")
# else:
#     print("名字不是fangzy")
#
# account = ""
# password = ""
# account = input("请输入账号：")
# 接收用户控制台输入
# password = input("请输入密码：")
# if name == account and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败")

# while
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1
#
# while counter <= 10:
#     print(counter)
#     counter += 1
# else:
#     print("达到了最大值")

# for循环/遍历 序列、集合、字典
# nameList = ["haha", "张三", "里斯", "lisa"]
# for name in nameList:
#     if name == "张三":
#         continue
#     if name == "里斯":
#         break
#     print(name)

# nameList1 = [["张三", "里斯", "lisa"], ("a", "s", "d")]
# for name in nameList:
#     for a in name:
#         print(a)
# else:
#     print("循环结束了")

# 范围循环 遍历0-10
# for x in range(0, 10):
#     print(x)
# 输出0-10的偶数,用|隔开
for x in range(0, 10, 2):
    print(x, end=" | ")
