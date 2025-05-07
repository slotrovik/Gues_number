from random import randint as rnd

computer_number = rnd(1,10)
def gues_number(comp_num):
    while True:
        human_num = int(input("please enter your number"))
        if human_num > comp_num:
            print ("Your number more")
        elif human_num < comp_num:
            print ("your number litle")
        elif human_num == computer_number:
            break
    print ("wonderfoul you won")
gues_number(computer_number)