from puzzles.day05.intcode import Day5IntcodeComputer


def read_test_program():
    return list(map(int, "3,0,4,0,99".split(',')))

def read_program():
    # Convert input file into a list of integers
    # representing our diagnostic program sequence
    with open('puzzles/day05/input.txt') as input_file:
        program_string = input_file.read()

    return [
        int(i) for i in program_string.split(',')
    ]



if __name__ == '__main__':
    input_ = 1
    computer = Day5IntcodeComputer(
        read_test_program(), 
        input_=input_, 
        debug=True,
    )   
    print('###########################')
    print('Running tests with debug mode on...')
    computer.run_diagnostic()
    print('Tests passed!')
    print('###########################')
    computer.memory = read_program()
    return_value = computer.run_diagnostic()
    print('Diagnostic return value:', return_value)
