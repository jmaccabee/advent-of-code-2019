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
    return (module_amount // 3) - 2


if __name__ == '__main__':
    run_test(1969, 654, calculate_module_fuel_requirement)
    run_test(100756, 33583, calculate_module_fuel_requirement)

    print('Tests passed!\n')
    fuel_requirement = calculate_total_fuel_requirements()
    print('Fuel required:', fuel_requirement)
