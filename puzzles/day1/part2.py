from puzzles.utils import run_test


def calculate_total_fuel_requirements():
    module_masses = []
    with open('puzzles/day1/inputs.txt') as module_mass_strings:
        for module_mass_string in module_mass_strings:
            module_mass = int(module_mass_string.strip())
            module_masses.append(module_mass)

    return sum([
        calculate_module_fuel_requirement(mass_amount)
        for mass_amount in module_masses
    ])


def calculate_module_fuel_requirement(module_amount):
    # create list to hold intermediate fuel requirements
    total_fuel_required_for_module = 0
    
    # initial fuel required is equal to module_amount
    incremental_mass = module_amount

    # begin loop to calculate total fuel requirement.
    # loop is finished once incremental_mass is <= 0.
    while not process_is_finished(incremental_mass):
        # calculate fuel required for the fuel mass
        incremental_mass = calculate_mass_fuel_requirement(
            incremental_mass
        )
        # add that amount to total_fuel_required_for_module
        total_fuel_required_for_module += incremental_mass

    # once process_is_finished(incremental_mass) evaluates to True,
    # return the total_fuel_required_for_module amount
    return total_fuel_required_for_module


def process_is_finished(mass):
    # process is finished once 
    # mass is less than or equal to 0
    STOP_MAXIMUM = 0
    return (mass <= STOP_MAXIMUM)


def calculate_mass_fuel_requirement(mass):
    # calculate fuel amount required
    fuel_required = (mass // 3) - 2

    # prohibit negative fuel amounts
    fuel_required = max(0, fuel_required)
    
    return fuel_required


if __name__ == '__main__':
    # run tests to confirm everything works as expected
    run_test(1969, 654, calculate_module_fuel_requirement)
    run_test(100756, 50346, calculate_module_fuel_requirement)
    print('Tests passed!\n')

    # if tests pass, run main program
    fuel_requirement = calculate_total_fuel_requirements()
    print('Fuel required:', fuel_requirement)
