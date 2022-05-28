import math

r = eval(input("请输入圆柱体的半径："))
h = eval(input("请输入圆柱体的高度："))
volume = math.pi * r * r * h
print("半径为{}高为{}的圆柱体体积为：{:.2f}".format(r, h, volume))