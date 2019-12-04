from puzzles.utils import run_test


PUZZLE_INPUT = "372304-847060"


def parse_password_int_range():
    password_int_range = tuple(
        int(int_string) for int_string in 
        PUZZLE_INPUT.split()
    )
    return range(*password_int_range)


def is_valid_password(password):
    REQUIRED_LENGTH = 6
    password_int_range = parse_password_int_range()

    correct_length = (len(str(password)) == REQUIRED_LENGTH)
    within_correct_window = (
        (password >= password_int_range[0]) & 
        (password <= password_int_range[-1])
    )
    not_decreasing = is_never_decreasing(password)
    has_repeat_integer = has_repeated_integer(password)

    return (
        correct_length & 
        within_correct_window & 
        increasing & 
        has_double
    )


def is_never_decreasing(password):
    password = str(password)
    is_increasing = True
    i = 0
    for i in range(len(password)):
        first = password[i]
        second = password[i+1]
        if second < first:
            is_increasing = False
    return is_increasing


def has_repeated_integer(password):
    password = str(password)
    has_repeat = False
    for i in range(len(password)):
        first = password[i]
        second = password[i+1]
        if first == second:
            has_repeat = True
    return has_repeat    


if __name__ == '__main__':
    run_test(111111, True, is_never_decreasing)
    run_test(111111, True, has_repeated_integer)
    run_test(111111, True, is_valid_password)
    run_test(223450, False, is_never_decreasing)
    run_test(223450, True, has_repeated_integer)
    run_test(223450, False, is_valid_password)    
    run_test(123789, True, is_never_decreasing)
    run_test(123789, False, has_repeated_integer)
    run_test(123789, False, is_valid_password)

    password_int_range = parse_password_int_range()
    valid_passwords = [
        i for i in password_int_range
        if is_valid_password(i)
    ]
    print('Number of valid passwords:', len(valid_passwords))
