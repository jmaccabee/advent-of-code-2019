def read_inputs():
    # Convert input file into a list of integers
    with open('puzzles/day5/inputs.txt') as input_file:
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


def handle_opcode(opcode, pos_one, pos_two=None):
    # handle the opcode and positional arguments
    ADDITIVE_OPCODE = 1
    MULTIPLICATIVE_OPCODE = 2
    STORE_INPUT_OPCODE = 3
    OUTPUT_OPCODE = 4
    
    if opcode == ADDITIVE_OPCODE:
        return pos_one + pos_two
    elif opcode == MULTIPLICATIVE_OPCODE:
        return pos_one * pos_two
    elif opcode == STORE_INPUT_OPCODE:
        pass
    elif opcode == OUTPUT_OPCODE:
        pass
    else:
        # if we see an opcode we don't expect,
        # raise an error
        raise UnhandledOpcode()
