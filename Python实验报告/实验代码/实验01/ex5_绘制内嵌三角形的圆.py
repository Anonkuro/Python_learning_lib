import turtle as t
import math

t.pensize(2)            #设置画笔宽度
t.right(90)             #画笔方向向右旋转90°，从向右转为向下
t.penup()               #抬起画笔，下移时不绘制线条
t.forward(200)          #画笔下移200像素
t.pendown()             #放下画笔，准备绘制线条
t.left(90)              #画笔方向向左旋转90°， 从向下转为向右

#绘制圆形
r = 200
t.circle(r)

#绘制内嵌正三角形
len = r * math.sqrt(3)
t.left(60)
t.forward(len)
t.left(120)
t.forward(len)
t.left(120)
t.forward(len)

t.done()