import random


def initial_roll(amount, max_value):
    dice_result = 0
    for i in range(amount):
        dice = random.randint(1, max_value)
        print(dice)
        dice_result = dice_result + dice
    print(dice_result)


def input_roll(line):
    modifier = 0
    line = line.split('+')
    print(line)
    for i in range(len(line)):
        sub_line = line[i]
        t = len(sub_line)
        Dice_Flag = 0
        for d in range(t):
            if str(sub_line[d]) == 'd':
                subb_line = sub_line.split('d')
                Dice_Flag = 1
                if str(subb_line[1]) == '':
                    modifier = modifier + int(subb_line[0])
                else:
                    print(subb_line[0], subb_line[1])
                pass
            elif d == t-1 and Dice_Flag == 0:
                modifier = modifier + int(sub_line[0])
    print(modifier)
    return


def roll_again(formula):
    print(formula)
    return


input_roll('12d8+15d4+4+3d6+2d4+12d+4')

# Up from here is Rolling part Line -> formula -> Rolls + modifiers
# Down from here is TXT working Part, it is working perfectly
# It might need some additional Settings part for later construction of main window


def prepare_input_line(line):
    FlagOperation = 0
    FlagDice = 0
    print(line)
    if len(str(line)) < 2:
        print('blank')
        return
    length = len(str(line))
    checked_length = ""
    for i in range(0, length):
        if str(line[i]) == ' ':
            pass
        elif str(line[i]) == 'к' and FlagDice == 1:
            checked_length = (str(checked_length) + 'd')
            FlagDice = 0
        elif str(line[i]) == 'd' and FlagDice == 1:
            checked_length = (str(checked_length) + str(line[i]))
            FlagOperation = 0
            FlagDice = 0
        elif str(line[i]) == '+' and FlagOperation == 1 or str(line[i]) == '-' and FlagOperation == 1:
            checked_length = (str(checked_length) + str(line[i]))
            FlagOperation = 0
        elif str(line[i]).isdigit() is True:
            checked_length = (str(checked_length) + str(line[i]))
            FlagOperation = 1
            FlagDice = 1
        else:
            pass
    line = checked_length
    print(line)
    return line


def rolls_history():
    read_history = open("roll_history.txt", "r")
    saved_history = read_history.read()
    saved_history = saved_history.split(',')
    print(saved_history)  # ToDo How to write it to output


def roll_add(added_roll, added_result):
    read_history = open("roll_history.txt", "r")
    saved_history = read_history.read()
    add_history = open("roll_history.txt", "w")
    add_history.write(f'{added_result}' f', {added_roll}' f', {saved_history}')
    print(saved_history)


# roll_add('3d8+1')
# roll_add('12d8 + 15d4 + 3d6', '81')
# rolls_history()
prepare_input_line('12d8 + 15d4 + 4 + 3d6 + 2d-4')
# initial_roll(3,10)
