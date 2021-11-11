#Program to print Right RightAngled Triangle
# *
# **
# ***
# ****
# #
def rt_rightAngledTriangle():
    for i in range(5):
        for j in range(i):
            print('*',end='')
        print()


rt_rightAngledTriangle()