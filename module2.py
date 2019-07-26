import module1
# def bb():
#     print("bb....")


# bb()
# module1.aa()
##########################################################
# def foo():
#     b = 'hello'
#
#     def bar():  # Python中可以在函数内部再定义函数
#         c = True
#         print(a)
#         print(b)
#         print(c)
#
#     bar()
#     # print(c)  # NameError: name 'c' is not defined
#
#
# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

##############################################################
# def foo():
#     global a
#     a = 200
#     print(a)  # 200
#
# # 该文件作为入口文件时  __name__ 为 __main__，否则为文件名
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200
