from puzzles.utils import run_test


def read_inputs():
    with open('puzzles/day3/inputs.txt') as input_file:
        inputs = input_file.readlines()
    return [
        wire_path_string.strip().split(',')
        for wire_path_string in inputs
    ]


def get_intersections(set0, set1):
    # find the intersection between the two wire sets
    return set0.intersection(set1)


def get_closest_intersection_distance(
        intersections, 
        center_coord=(0, 0),
    ):
    # remove center coordinate intersection,
    # since both wires start at the center
    intersections.remove(center_coord)

    # calculate the Manhattan distance
    # from center for each intersection coordinate
    distances = []
    for intersection in intersections:
        # take the absolute value of the x and y
        # positions of each intersection
        x_abs_dist = abs(intersection[0])
        y_abs_dist = abs(intersection[1])
        # calculate the absolute distance from center
        manhattan_distance = (
            (x_abs_dist - center_coord[0]) + 
            (y_abs_dist - center_coord[1])
        )
        # and add this Manhattan distance to a list
        distances.append(manhattan_distance)
    # then return the minimum distance
    return min(distances)


def wire_path_coordinates_from_string(
        wire_path_string, 
        center_coord=(0, 0),
    ):
    # calculates the wire path coordinates
    # from a list of wire path strings

    # unpack center coordinate as x and y
    x, y = center_coord

    # calculate the coordinate path of each wire
    wire_path_coordinates = []
    for vector_string in wire_path_string:
        # get the vector from it's vector string
        vector = vector_from_string(
            vector_string
        )
        # create the range of integers from current
        # starting coordinate (x, y) 
        # terminating at (x + vector[0], y + vector[1])
        # since starting coordinate (x, y) is our reference point
        vector_x_coordinates = get_vector_coordinates(x, x + vector[0])
        vector_y_coordinates = get_vector_coordinates(y, y + vector[1])
        # convert the x and y vector coordinates into an
        # integer-coordinate line segment
        segment_coordinates = get_segment_coordinates(
            vector_x_coordinates, 
            vector_y_coordinates,
        )
        # add each integer-coordinate line segment to the wire path
        wire_path_coordinates.extend(segment_coordinates)
        # increment our reference coordinate by vector[0], vector[1]
        x += vector[0]
        y += vector[1]
    # return a set to remove any duplicate coordinates
    # and to allow us to easily find the wire intersections
    return set(wire_path_coordinates)


def get_segment_coordinates(x_coordinates, y_coordinates):
    # calculates the coordinates representing the wire segment
    wire_path = []
    for x_coord in x_coordinates:
        for y_coord in y_coordinates:
            wire_path.append((x_coord, y_coord))
    return wire_path


def get_vector_coordinates(val0, val1):
    # ensures our range of coordinates 
    # always starts at the lower value
    start_val = min(val0, val1)
    end_val = max(val0, val1)
    # our range ends at end_val + 1 so
    # we don't end up with an empty list
    # when calculating the vector coordinates
    # when the magnitude of the vector is 0
    return list(range(start_val, end_val+1))        


def vector_from_string(vector_string):
    # direction string to unit coordinate converter
    direction_from_string = {
        'D': (0, -1),
        'L': (-1, 0),
        'U': (0, 1),
        'R': (1, 0),
    }
    direction_string = vector_string[0]
    # convert direction string to unit coordinate
    x_direction, y_direction = direction_from_string[direction_string]
    magnitude = int(vector_string[1:])
    # only the non-zero direction will have a resulting non-zero magnitude
    return (magnitude * x_direction, magnitude * y_direction)


def run_full_test(wire_path_strings):
    wire_path0 = wire_path_coordinates_from_string(
        wire_path_strings[0]
    )
    wire_path1 = wire_path_coordinates_from_string(
        wire_path_strings[1]
    )        
    # find the intersections between the two wires
    intersections = get_intersections(wire_path0, wire_path1)
    # find the distances of the nearest intersection
    closest_distance = get_closest_intersection_distance(
        intersections
    )
    return closest_distance


if __name__ == '__main__':
    # run a few unit tests to make sure our functions are correct
    run_test('R100', (100, 0), vector_from_string)
    run_test(
        (-100, 0), 
        list(range(-100, 1)), 
        get_vector_coordinates, 
        expand_inputs=True
    )
    run_test(
        (100, 0), 
        list(range(0, 101)), 
        get_vector_coordinates,
        expand_inputs=True
    )
    run_test(
        (0, 0), 
        [0], 
        get_vector_coordinates,
        expand_inputs=True
    )
    run_test(
        ([0, 1], [0]), 
        [(0, 0), (1, 0)], 
        get_segment_coordinates,
        expand_inputs=True,
    )
    run_test(
        [(0, 0), (100, 0), (50, 0)], 
        50,
        get_closest_intersection_distance,
    )

    assert run_full_test((
        "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(','),
        "U62,R66,U55,R34,D71,R55,D58,R83".split(','),
    )) == 159

    assert run_full_test((
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(','),
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(','),
    )) == 135
    print('################################')

    # read the inputs
    wire_path_strings = read_inputs()
    # convert the input wire path strings to wire path coordinates
    wire_path0 = wire_path_coordinates_from_string(
        wire_path_strings[0]
    )
    wire_path1 = wire_path_coordinates_from_string(
        wire_path_strings[1]
    )        
    # find the intersections between the two wires
    intersections = get_intersections(wire_path0, wire_path1)
    # find the distances of the nearest intersection
    closest_distance = get_closest_intersection_distance(
        intersections
    )
    # print the nearest intersection distance
    print("Closest Manhattan distance:", closest_distance)
