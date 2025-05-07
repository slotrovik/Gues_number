from random import randint as rnd


def gues_number():
    comp_num = rnd(1, 10)
    while True:
        human_num = int(input("please enter your number"))
        if human_num > comp_num:
            print("Your number more")
        elif human_num < comp_num:
            print("your number litle")
        elif human_num == comp_num:
            break
    print("wonderfoul you won")


gues_number()

while True:
    user_right = input("You want again y/n ")
    if user_right == "y":
        gues_number()
    else:
        print("Thanks for game my friend")
        break