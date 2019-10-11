#试图编写一个猜数字的游戏
#它需要有以下一些功能：
#接受用户输入的数字，判断用户输入的是否是数字类型
#要求机器的数字需要是随机的
#用户在输入完成之后，如果是正确需要给出正确提示，并提醒游戏结束
#用户如果输入错了的话也需要提示错误，并且提示是大了还是小了
import random
the_number = input("请输入整型数字：")
my_number = int(the_number)
print(type(my_number))
random_number = random.randint(1,1000)
if my_number == random_number:
    print("You are winner!")
else:
    if my_number < random_number:
        print("Small Small Small")
    else:
        print("Big Big Big")
    while my_number != random_number:
        print("再来一次吧:")
        the_number = input("请输入数字：")
        my_number = int(the_number)
        if my_number == random_number:
            print("You are winner!")
        else:
            if my_number < random_number:
                print("Small Small Small")
            else:
                print("Big Big Big")
print("游戏结束")
