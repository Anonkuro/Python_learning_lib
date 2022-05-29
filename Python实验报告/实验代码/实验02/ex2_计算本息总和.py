# 2. 通过下面的步骤可以计算出储蓄账户中以100元人民币为本金，每年5%为复利，三年后的本息总和。请把下面的文字描述转变为Python代码，然后调试并运行。
# （1）创建变量balance，并赋值为100；
# （2）balance增长5%，并赋值给balance；
# （3）balance增长5%，并赋值给balance；
# （4）balance增长5%，并赋值给balance；
# （5）输出balance的值。
# 完成后再思考，是否可以将（2）-（4）的三步对balance计算合成一步完成，如果可以，请再给出你的代码。

balance = 100
balance = balance * 1.05
balance = balance * 1.05
balance = balance * 1.05
print("balance的值为：", balance)

# 优化后
balance = 100
balance = balance * (1.05**3)
print("balance的值为：", balance)