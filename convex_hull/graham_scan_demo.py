from random import randint

from point import Point


def sort_points(points):
    return sorted(points)


def get_points(n):
    range_val = 10
    points = []
    for _ in range(n):
        point = Point(randint(-range_val, range_val),
                      randint(-range_val, range_val))
        points.append(point)
    return points


def main():
    N = 20
    points = sort_points(get_points(N))
    convex_hull = []


if __name__ == "__main__":
    main()
