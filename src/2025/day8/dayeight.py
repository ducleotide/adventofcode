import math


def euclidean_distance(point1: tuple[int, int, int],
                       point2: tuple[int, int, int]) -> float:
    """
    Calculate the Euclidean distance between two 3D points.

    Args:
        point1: A tuple (x1, y1, z1) representing the first point
        point2: A tuple (x2, y2, z2) representing the second point

    Returns:
        float: The Euclidean distance between the two points
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def load_points(filename) -> tuple[list[tuple[int, int, int]],
                                   list[tuple[int, int, int]],
                                   list[tuple[int, int, int]]]:
    # load the points and store into data structure(s) sorted by x y and z
    points = []
    
    # Read points from file
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                x, y, z = map(int, line.split(','))
                points.append((x, y, z))
    
    # Sort by x, y, and z coordinates
    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])
    points_sorted_by_z = sorted(points, key=lambda p: p[2])
    
    return points_sorted_by_x, points_sorted_by_y, points_sorted_by_z


def main():
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    points_x, points_y, points_z = load_points(args.file)

    point_distances: dict[tuple[int, int, int],
                          dict[tuple[int, int, int],
                               float]] = {}

    min_point_distances: list[tuple[tuple[int, int, int],
                                    tuple[int, int, int], float]] = []

    distance_points: dict[float, tuple[ tuple[int, int, int], tuple[int, int, int] ]] = {}
    distances = []
    for point1 in points_x:
        # distances: dict[tuple[int, int, int], float] = {}
        for point2 in points_x:
            print(f"points {point1}, {point2}")

            point_dist: float = 0.0
            if point1 != point2:
                point_dist = euclidean_distance(point1, point2)
                print(f"point {point1}, {point2} distance is {point_dist}")
                point_distances[point1][point2] = point_dist
                distance_points[point_dist] = (point1, point2)
                distances.append(point_dist)
                # if point_dist < min_point[1]:
                #     min_point_distances[point1][point2] = point_dist

            # point_distances[point1][point2] = point_dist
            # min_point = (point2, point_dist)
        # point_distances[point1] = min_point

    # 10 shortest distances
    sorted_distances = sorted(distances)
    size_of_list = len(sorted_distances)

    mult = 1
    for distance in sorted_distances[size_of_list-3:]:
        print(f"largest: {distance}")
        mult *= distance
    print(f"mult: {mult}")


if __name__ == '__main__':
    main()
