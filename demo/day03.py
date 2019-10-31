"""
用户身份验证
"""

# name = str(input("请输入登录名："))
# password = str(input("请输入密码："))
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')
# if name == "admin" and password == "123456" :
#     print("验证通过")
# else:
#     print("验证不通过")

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

# x = int(input("请输入一个正整数："))
# if x > 1:
#     y = 3*x - 5
#     print(y)
# elif -1 <= x <= 1:
#     y = x + 2
#     print(y)
# else:
#     y = 5 * x + 3
#     print(y)

"""
英制单位英寸和公制单位厘米互换
厘米 = 2.54*英寸
"""
# changdu = float(input("请输入长度："))
# danwei = input("请输入单位")
#
# if danwei == 'in' or danwei == '英尺':
#     print("%f英尺 = %f 厘米" % (changdu, changdu*2.54))
# elif danwei == 'cm' or danwei == '厘米':
#     print("%f厘米 = %f英尺" % (changdu, changdu/2.54))
# else:
#     print("输入单位有误")

"""
掷骰子决定做什么事情
"""
import random
# 获取1-6的随机整数
# value = random.randint(1,6)
# if value == 1:
#     print("唱歌")
# elif value == 2:
#     print("跳舞")
# elif value == 3:
#     print("爬山")
# elif value == 4:
#     print("滑雪")
# elif value == 5:
#     print("看书")
# elif value == 6:
#     print("学习")
# else:
#     print("数值有误")

"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E
"""
# chengji = float(input("请输入分数："))
# if chengji >= 90:
#     print("你的成绩是：A")
# elif 80 <= chengji <= 89:
#     print("你的成绩是：B")
# elif 70 <= chengji <= 79:
#     print("你的成绩是：C")
# elif 60 <= chengji <= 69:
#     print("你的成绩是：D")
# else:
#     print("你的成绩是：E")








