from puzzles.day2.part1 import (
    read_inputs,
    run_intcode_program,
)


class TerminateIntcodeException(Exception):
    """
    We'll raise an exception to easily exit
    both for loops when we find the noun
    and verb values that produce the expected output
    """
    pass


def goal_seek_output(expected_output):
    # we'll use brute force to try and 
    # find the noun and verb that produces
    # the desired expected ouput value
    try:
        for noun in range(99):
            for verb in range(99):
                # read in the initial inputs each time
                inputs = read_inputs()

                # change positions one and two 
                # to be the new noun and verb values
                inputs[1] = noun
                inputs[2] = verb

                inputs = run_intcode_program(inputs)

                if inputs[0] == expected_output:
                    print('Noun:', noun, 'Verb:', verb)
                    raise TerminateIntcodeException()
    except TerminateIntcodeException:
        pass

    # make sure we didn't just exhaust the 
    # potential options and we really did
    # find the appropriate values
    assert inputs[0] == expected_output

    return ((noun * 100) + verb)


if __name__ == '__main__':
    # goal seek the expected output
    expected_output = 19690720
    input_value_combination = goal_seek_output(expected_output)
    
    # then, test again using these inputs just to be sure
    noun = input_value_combination // 100
    verb = input_value_combination % 100
    inputs = read_inputs()
    inputs[1] = noun
    inputs[2] = verb
    inputs = run_intcode_program(inputs)
    assert inputs[0] == expected_output

    # if the test passes, print the inputs
    print('Input value combination:', input_value_combination)
