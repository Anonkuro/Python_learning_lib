import random as rd

target = rd.randint(1, 100)
print("已产生一个1~100之间的随机整数，猜猜该数的数值.")
count = 0

while True:
    guess = eval(input("请输入猜测的数值："))
    count = 1
    if guess > target:
        print("猜的太大了！")
    elif guess < target:
        print("猜的太小了！")
    else:
        print("好棒，{}次就猜中了！".format(count))
        break