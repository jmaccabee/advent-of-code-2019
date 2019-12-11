def read_inputs():
    # Convert input file into a list of integers
    with open('puzzles/day5/inputs.txt') as input_file:
        input_string = input_file.read()

    return [
        i for i in input_string.split(',')
    ]


def run_program(memory):
    TERMINATE_OPCODE = "99"
    ADDITIVE_OPCODE = "01"
    MULTIPLICATIVE_OPCODE = "02"
    STORE_OPCODE = "03"
    RETURN_OPCODE = "04"

    pointer = 0
    terminated = False
    while not terminated:
        instruction = memory[pointer]
        opcode, param2_mode, param1_mode, param0_mode = parse_instruction(
            instruction,
        )

        if opcode == TERMINATE_OPCODE:
            terminated = True
            break
        
        pointer += 1
        param0 = memory[pointer]
        param1 = memory[pointer+1]
        param2 = memory[pointer+2]

        param0_value = parse_value(param0_mode, param0, memory)
        param1_value = parse_value(param1_mode, param1, memory)
        param2_value = parse_value(param2_mode, param2, memory)

        if opcode == ADDITIVE_OPCODE:
            output = param0_value + param1_value
            memory[param2_value] = output
            pointer += 3

        elif opcode == MULTIPLICATIVE_OPCODE:
            output = param0_value + param1_value
            memory[param2_value] = output            
            pointer += 3

        elif opcode == STORE_OPCODE:
            memory[param0_value] = param0_value
            pointer += 1

        elif opcode == RETURN_OPCODE:
            return memory[param0_value]


def parse_instruction(instruction):
    # ensure instruction is 5 characters long;
    # if shorter than 5 characters, add leading 0s
    INSTRUCTION_LENGTH = 5
    leading_zeroes = INSTRUCTION_LENGTH - len(instruction)
    instruction = (leading_zeroes * "0") + instruction

    opcode = instruction[-2:]
    param2_mode, param1_mode, param0_mode = [
        int(i) for i in instruction[:3]
    ]

    return opcode, param2_mode, param1_mode, param0_mode


def parse_value(mode, param, memory):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    param = int(param)
    if mode == POSITION_MODE:
        return int(memory[param])
    elif mode == IMMEDIATE_MODE:
        return param


if __name__ == '__main__':
    TEST_INPUT = "1,3,0,4,0,99".split(',')
    assert run_program(TEST_INPUT) == 0
