from puzzles.utils import run_test
from puzzles.day4.part1 import (
    parse_password_int_range,
    is_never_decreasing,
)
from puzzles.day4.constants import PUZZLE_INPUT, REQUIRED_LENGTH


def is_valid_password(password):
    password_int_range = parse_password_int_range()

    correct_length = (len(str(password)) == REQUIRED_LENGTH)
    within_correct_window = (
        (password >= password_int_range[0]) & 
        (password <= password_int_range[-1])
    )
    not_decreasing = is_never_decreasing(password)
    has_repeat_adjacent_integer, repeated_ints = has_repeated_adjacent_ints(
        password
    )
    repeated_adjacent_integer_is_unique = has_unique_adjacent_integer(
        password,
        repeated_ints,
    )

    return (
        correct_length & 
        within_correct_window & 
        not_decreasing & 
        has_repeat_adjacent_integer &
        repeated_adjacent_integer_is_unique
    )


def has_unique_adjacent_integer(password, repeated_ints):
    for repeat in repeated_ints:
        count = 0
        for i in range(len(password)-1):
            if repeat == f"{password[i]}{password[i+1]}":
                count += 1
        if count == 1:
            return True
    return False


def has_repeated_adjacent_ints(password):
    repeated_ints = []
    password = str(password)
    has_repeat = False
    for i in range(len(password)-1):
        first = password[i]
        second = password[i+1]
        if first == second:
            has_repeat = True
            repeated_ints.append(first)
    return has_repeat, repeated_ints


if __name__ == '__main__':
    run_test(111333, False, has_unique_adjacent_integer)
    run_test(111233, False, has_unique_adjacent_integer)

    password_int_range = parse_password_int_range()
    valid_passwords = [
        i for i in password_int_range
        if is_valid_password(i)
    ]
    print('Number of valid passwords:', len(valid_passwords))

