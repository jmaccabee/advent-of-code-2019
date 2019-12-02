def run_test(
        input_value, 
        expected_value,
        function_to_test, 
        expand_inputs=False
    ):
    if expand_inputs:
        transformed_value = function_to_test(*input_value)
    else:
        transformed_value = function_to_test(input_value)
    assert transformed_value == expected_value
    print(f'Test passed: {transformed_value} == {expected_value}')
