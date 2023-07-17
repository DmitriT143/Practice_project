import random

def Reroll(formula):
    se


def initial_roll(ammount, max_value):
    def dice_roll(max_value):
        dice = random.randint(1, max_value)
        print(dice)
        return dice
    for i in range(ammount):
        i = i + 1
        dice_roll(max_value)


initial_roll(2,20)
