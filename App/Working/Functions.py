import random


def input_to_response(line):
    def initial_roll(amount, max_value):
        dice_result = 0
        for i in range(int(amount)):
            dice = random.randint(1, int(max_value))
            dice_result = dice_result + dice
        return dice_result

    def input_roll(line):
        modifier = 0
        kept_result = 0
        line = line.split('+')
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
                        dice_result = initial_roll(subb_line[0], subb_line[1])
                        print(dice_result)
                        kept_result = dice_result + kept_result
                    pass
                elif d == t - 1 and Dice_Flag == 0:
                    modifier = modifier + int(sub_line)
        print(modifier)
        result = modifier + kept_result
        print(result)
        return result

    def roll_again(formula):
        print(formula)
        return

    # Up from here is Rolling part Line -> formula -> Rolls + modifiers
    # Down from here is TXT working Part, it is working perfectly
    # It might need some additional Settings part for later construction of main window

    def prepare_input_line(line):
        FlagOperation = 0
        FlagDice = 0
        print(line)
        if len(str(line)) < 2:
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

#    def rolls_history():
#        read_history = open("roll_history.txt", "r")
#        saved_history = read_history.read()
#        saved_history = saved_history.split(',')
#        print(saved_history)  # ToDo How to write it to output
#
    def roll_add(added_roll, added_result):
        read_history = open("roll_history.txt", "r")
        print(added_roll, added_result)
        print(read_history)
        saved_history = read_history.read()
        add_history = open("roll_history.txt", "w")
        add_history.write(f'{added_result}' f', {added_roll}' f', {saved_history}')
        print(saved_history)

    correct_formula = prepare_input_line(line)
    output = input_roll(correct_formula)
    return correct_formula, output

