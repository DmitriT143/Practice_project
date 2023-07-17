import random


def roll_again(formula):
    print(formula)
    return


def initial_roll(amount, max_value):
    def dice_roll(max_value):
        dice = random.randint(1, max_value)
        print(dice)
        return dice

    for i in range(amount):
        i = i + 1
        dice_roll(max_value)


initial_roll(2, 20)
