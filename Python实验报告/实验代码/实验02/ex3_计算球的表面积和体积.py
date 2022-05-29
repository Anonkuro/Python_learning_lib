# 3. 编写程序，从键盘上输入球的半径，计算输出球的表面积和体积，要求输入和输出的数字结果之前都具有一定的文字提示。
# 球的表面积计算公式：area = 4πr^2， r为球半径.
# 球的体积计算公式：volume = (4/3)πr^3, r为球半径.

from math import *
r = eval(input("请输入球的半径："))
area = 4 * pi * r * r
volume = (4/3) * pi * r ** 3

print("半径为{}的球体，表面积 = {:.2f}, 体积 = {:.2f}".format(r, area, volume))
