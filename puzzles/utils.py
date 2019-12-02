def run_test(input_value, expected_value, function_to_test):
    transformed_value = function_to_test(input_value)
    assert transformed_value == expected_value
    print(f'Test passed: {transformed_value} == {expected_value}')
