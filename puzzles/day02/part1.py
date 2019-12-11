from puzzles.utils import run_test


def recreate_gravity_assist_program_alarm():
    # read in the inputs
    inputs = read_inputs()

    # modify the inputs at position 1 and 2
    # to recreate the 1202 program alarm conditions
    inputs[1] = 12
    inputs[2] = 2

    # run Intcode program
    inputs = run_intcode_program(inputs)

    return inputs[0]


def read_inputs():
    # Convert input file into a list of integers
    with open('puzzles/day2/input.txt') as input_file:
        input_string = input_file.read()

    return [
        int(i) for i in input_string.split(',')
    ]


class UnhandledOpcode(Exception):
    """
    This exception should never be raised, 
    but we implement it here just in case.
    """
    pass


def run_intcode_program(inputs):
    TERMINATE_OPCODE = 99

    i = 0
    while True:
        opcode = inputs[i]
        
        # if we see a termination opcode,
        # break out of the while loop
        # and terminate the program
        if opcode == TERMINATE_OPCODE:
            break

        pos_one = inputs[i+1]
        pos_two = inputs[i+2]
        replacement_pos = inputs[i+3]

        # handle the opcode instruction
        replacement_value = handle_opcode(
            opcode, 
            inputs[pos_one], 
            inputs[pos_two],
        )

        # replace the specified value based on the
        # opcode and positional arguments
        inputs[replacement_pos] = replacement_value
        
        # increment the index by 4 and repeat
        i += 4

    return inputs


def handle_opcode(opcode, pos_one, pos_two):
    # handle the opcode and positional arguments
    # based on the specification in day2/puzzle.txt
    ADDITIVE_OPCODE = 1
    MULTIPLICATIVE_OPCODE = 2
    
    if opcode == ADDITIVE_OPCODE:
        return pos_one + pos_two
    elif opcode == MULTIPLICATIVE_OPCODE:
        return pos_one * pos_two
    else:
        # if we see an opcode we don't expect,
        # raise an error
        raise UnhandledOpcode()


if __name__ == '__main__':
    # test handle_opcode
    run_test((1, 1, 1), 2, handle_opcode, expand_inputs=True)
    run_test((2, 3, 2), 6, handle_opcode, expand_inputs=True)
    run_test((2, 99, 99), 9801, handle_opcode, expand_inputs=True)

    # test run_intcode_program with test inputs
    test_inputs = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    run_test(
        test_inputs, 
        [30, 1, 1, 4, 2, 5, 6, 0, 99], 
        run_intcode_program
    )

    first_position_value = recreate_gravity_assist_program_alarm()
    print('Position 0 value:', first_position_value)
