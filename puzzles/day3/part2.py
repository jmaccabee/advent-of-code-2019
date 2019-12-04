from puzzles.day3.part1 import (
    read_inputs,
    get_vector_coordinates,
    vector_from_string
)


def get_intersection_with_minimum_distance(
        intersections_with_distances
    ):
    return sorted(
        intersections_with_distances, 
        key=lambda x: x[1],
    )[0]


def get_intersections_and_distances(set0, set1, center_coord=(0, 0)):
    intersections_with_distance = []

    coordinate_set0 = set(pair[0] for pair in set0)
    coordinate_set1 = set(pair[0] for pair in set1)
    intersections = coordinate_set0.intersection(
        coordinate_set1
    ) 
    
    intersections.remove(center_coord)

    for intersection in intersections:
        dist1 = get_distance_for_matching_coordinate(
            intersection,
            set0,
        )
        dist2 = get_distance_for_matching_coordinate(
            intersection,
            set1,
        )
        total_distance = dist1 + dist2
        intersections_with_distance.append(
            (intersection, total_distance)
        )

    return intersections_with_distance


def get_distance_for_matching_coordinate(
        coordinate_to_match, 
        coordinates_and_distances,
    ):
    for (coord, dist) in coordinates_and_distances:
        if coord == coordinate_to_match:
            return dist


def wire_path_coordinates_from_string(
        wire_path_string, 
        center_coord=(0, 0),
    ):
    # calculates the wire path coordinates
    # from a list of wire path strings

    # unpack center coordinate as x and y
    x, y = center_coord

    distance_from_center = 0

    # calculate the coordinate path of each wire
    wire_path_coordinates_and_distances = []
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
        ascending_step = (
            (vector_string[0] == 'U') or
            (vector_string[0] == 'R')
        )
        segment_coordinates_and_distance = get_segment_coordinates_and_distance(
            vector_x_coordinates, 
            vector_y_coordinates,
            distance_from_center,
            ascending_step,
        )

        # calculate the vector distance

        # add each integer-coordinate line segment to the wire path
        wire_path_coordinates_and_distances.extend(
            segment_coordinates_and_distance
        )

        # increment our reference coordinate by vector[0], vector[1]
        # and our distance from center by their absolute values
        x += vector[0]
        y += vector[1]
        distance_from_center += (abs(vector[0]) + abs(vector[1]))
        
    return wire_path_coordinates_and_distances


def get_segment_coordinates_and_distance(
        x_coordinates, 
        y_coordinates, 
        elapsed_distance,
        ascending_step,
    ):
    if not ascending_step:
        x_coordinates.reverse()
        y_coordinates.reverse()

    # calculates the coordinates representing the wire segment
    wire_path = []
    for x_coord in x_coordinates:
        for y_coord in y_coordinates:
            wire_path.append(
                ((x_coord, y_coord), elapsed_distance)
            )
            elapsed_distance += 1
    return wire_path


def run_part2_test_case(wire_string0, wire_string1):
    wire_path0 = wire_path_coordinates_from_string(
        wire_string0
    )
    wire_path1 = wire_path_coordinates_from_string(
        wire_string1
    )
    # find the intersections between the two wires
    intersections_with_distances = get_intersections_and_distances(
        wire_path0, 
        wire_path1
    )
    # find the distances of the nearest intersection
    closest_distance = get_intersection_with_minimum_distance(
        intersections_with_distances
    )
    return closest_distance[1]


if __name__ == '__main__':
    # test cases from puzzle:
    test_wire_string0 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    test_wire_string1 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert run_part2_test_case(
        test_wire_string0.split(','), 
        test_wire_string1.split(','),
    ) == 610
    test_wire_string2 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    test_wire_string3 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert run_part2_test_case(
        test_wire_string2.split(','), 
        test_wire_string3.split(','),
    ) == 410

    test_wire_string4 = "U7,R6,D4,L4"
    test_wire_string5 = "R8,U5,L4,D4"
    assert run_part2_test_case(
        test_wire_string4.split(','), 
        test_wire_string5.split(','),
    ) == 30
    print("##################################")
    print("Tests passed!")
    print("##################################")

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
    intersections_with_distances = get_intersections_and_distances(
        wire_path0, 
        wire_path1
    )
    # find the distances of the nearest intersection
    closest_distance = get_intersection_with_minimum_distance(
        intersections_with_distances
    )
    # print the nearest continuguous intersection distance
    print("Closest contiguous Manhattan distance:", closest_distance)
