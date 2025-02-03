import random

max_value = 6
min_value = 1

roll_dice = 'yes'

while roll_dice =='yes' or roll_dice =='Yes':
    print("")
    print('Rolling the Dices....')

    dice = random.randint(min_value,max_value)
    print('value of dice 1 is ', dice)

    dice2 = random.randint(min_value,max_value)
    print('value of dice 1 is ', dice2)

    roll_dice = input("press yes to roll again ")

    