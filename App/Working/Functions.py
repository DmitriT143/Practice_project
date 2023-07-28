import random


def input_to_response(line):
    def initial_roll(amount, max_value):
        dice_result = 0
        for i in range(int(amount)):
            dice = random.randint(1, int(max_value))
            dice_result = dice_result + dice
        return dice_result

    def input_roll(to_output):
        Prev_function = 0
        Function_output = 0
        pre_dice_number = 0
        post_dice_number = 0
        next_in_line = 0
        Flag_operation = 1
        Flag_dice_roll = 0
        for i in range(len(to_output)):
            if str(to_output[i]).isdigit():
                Flag_operation = 0
                if pre_dice_number == 0:
                    pre_dice_number = str(to_output[i])
                else:
                    pre_dice_number = str(pre_dice_number) + str(to_output[i])
                print(pre_dice_number)
            if Flag_dice_roll == 0 and str(to_output[i]) == 'd':
                Flag_dice_roll = 1
                Flag_operation = 1
                if pre_dice_number == 0:
                    pre_dice_number = 1
                post_dice_number = pre_dice_number
                pre_dice_number = 0
            if Flag_operation == 0 and str(to_output[i]) == '+' or Flag_operation == 0 and str(to_output[i]) == '-':
                if Flag_dice_roll == 1:
                    next_in_line = initial_roll(post_dice_number, pre_dice_number)
                pre_dice_number = 0
                if Prev_function == 0:
                    Function_output = Function_output + next_in_line
                if Prev_function == 1:
                    Function_output = Function_output + next_in_line
                if Prev_function == 2:
                    Function_output = Function_output - next_in_line
                Flag_operation = 1
                Flag_dice_roll = 0
                next_in_line = 0
                if str(to_output[i]) == '-':
                    Prev_function = 2
                if str(to_output[i]) == '+':
                    Prev_function = 1
            if i == len(to_output) - 1:
                if Flag_dice_roll == 1:
                    next_in_line = initial_roll(post_dice_number, pre_dice_number)
                if Prev_function == 0:
                    Function_output = Function_output + next_in_line
                if Prev_function == 1:
                    Function_output = Function_output + next_in_line
                if Prev_function == 2:
                    Function_output = Function_output - next_in_line
        return Function_output

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
    #        print(saved_history)
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
