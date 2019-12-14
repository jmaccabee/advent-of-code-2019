TERMINATE_OPCODE = "99"
ADDITIVE_OPCODE = "01"
MULTIPLICATIVE_OPCODE = "02"
STORE_OPCODE = "03"
RETURN_OPCODE = "04"
POSITION_MODE = "0"
IMMEDIATE_MODE = "1"
OPCODE_NUM_PARAMETERS = {
    TERMINATE_OPCODE: 0,
    ADDITIVE_OPCODE: 3,
    MULTIPLICATIVE_OPCODE: 3,
    STORE_OPCODE: 1,
    RETURN_OPCODE: 1,
}


def read_inputs():
    # Convert input file into a list of integers
    # representing our diagnostic program sequence
    with open('puzzles/day5/input.txt') as input_file:
        input_string = input_file.read()

    return [
        i for i in input_string.split(',')
    ]


def run_diagnostic_program(input_value, memory):
    pointer = 0
    while True:
        # determine the opcode and parameter modes 
        # at the pointer location
        opcode_and_modes = memory[pointer]
        opcode, parameter_modes = parse_opcode_and_modes(opcode_and_modes)

        # if terminate opcode, break loop and return the return value
        if opcode == TERMINATE_OPCODE:
            print('Returned value:', return_value)
            return return_value

        values = []
        # iterate through parameter modes and get parameter values
        for mode in parameter_modes:
            # increment pointer
            pointer += 1
            
            if mode == POSITION_MODE:
                # get the position at the pointer
                position = memory[pointer]
                # and get the value at the position
                value = memory[int(position)]
            elif mode == IMMEDIATE_MODE:
                # get the value at the pointer
                value = memory[pointer]
            values.append(int(value))

        # handle the appropriate opcode operation
        if opcode == ADDITIVE_OPCODE:
            # additive opcodes have three parameters:
            # two values to add and a location to store them
            x, y, location = values
            memory[location] = str(x + y)
        elif opcode == MULTIPLICATIVE_OPCODE:
            # multiplicative opcodes have three parameters:
            # two values to multiply and a location to store them
            x, y, location = values
            memory[location] = str(x * y)
        elif opcode == STORE_OPCODE:
            # store opcodes have one parameter:
            # the location to store the input_value
            location = values[0]
            memory[location] = input_value
        elif opcode == RETURN_OPCODE:
            # return opcodes have one parameter:
            # the location to return the value of
            return_value = values[0]

        # increment pointer to go to the next opcode
        pointer += 1


def parse_opcode_and_modes(opcode_and_modes):
    # opcodes must be at least 2 characters with a leading 0
    OPCODE_LENGTH = 2
    opcode_and_modes = add_leading_zeroes(opcode_and_modes, OPCODE_LENGTH)

    # get the opcode so we know how many parameters there are
    opcode = opcode_and_modes[-OPCODE_LENGTH:]
    num_parameters = OPCODE_NUM_PARAMETERS[opcode]

    # determine how many leading zeroes to add based on num_parameters
    opcode_and_mode_min_length = len(opcode) + num_parameters
    opcode_and_modes = add_leading_zeroes(
        opcode_and_modes, 
        opcode_and_mode_min_length
    )

    # reverse opcode_and_modes since parameter modes are in reverse order
    # then get parameter modes from opcode_and_modes
    parameter_modes = opcode_and_modes[::-1][OPCODE_LENGTH:]

    return opcode, parameter_modes


def add_leading_zeroes(string, min_length):
    # if string is longer than min_length,
    # no leading zeroes will be added
    leading_zeroes = min_length - len(string)
    return ("0" * leading_zeroes) + string


if __name__ == '__main__':
    TEST_INPUT = 1
    TEST_DIAGNOSTIC_PROGRAM = "3,0,4,0,99".split(',')
    assert run_diagnostic_program(
        TEST_INPUT, 
        TEST_DIAGNOSTIC_PROGRAM
    ) == 0
