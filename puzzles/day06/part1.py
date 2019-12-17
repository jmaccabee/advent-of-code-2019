from collections import defaultdict


def read_input():
    with open('puzzles/day06/input.txt') as input_file:
        inputs = input_file.readlines()
    orbits = []
    for orbit_string in inputs:
        direct_orbitee, direct_orbiter = orbit_string.split(')')
        orbits.append((direct_orbitee.strip(), direct_orbiter.strip()))
    return orbits


def count_orbits(orbits):
    import pdb; pdb.set_trace()
    DIRECT_ORBITERS = ['COM']
    orbit_map = defaultdict(list)
    while DIRECT_ORBITERS:
        orbitee = DIRECT_ORBITERS.pop()
        direct_orbiters = get_orbiters(orbits, orbitee)
        for orbitees, orbiters in orbit_map.items():
            for orbiter in direct_orbiters:
                if orbiter in orbitees:
                    orbit_map

        orbit_map[orbitee].append(direct_orbiters)
        DIRECT_ORBITERS.extend(list(direct_orbiters))
        print('Direct orbiters remaining:', len(DIRECT_ORBITERS))
    import pdb; pdb.set_trace()
    total_orbits = 0
    for orbitee, orbiters in orbit_map:
        for orbiter in orbiters:
            orbit_map[orbiter].add(orbitee)
    print('#################################################')
    print('TOTAL DIRECT AND INDIRECT ORBITS:', total_orbits)
    print('#################################################')
    
def get_orbiters(orbits, match_string):
    direct_orbiters = []
    for orbitee, orbiter in orbits:
        if orbitee == match_string:
            direct_orbiters.append(orbiter)
    return direct_orbiters


if __name__ == '__main__':
    orbits = read_input()
    count_orbits(orbits)
