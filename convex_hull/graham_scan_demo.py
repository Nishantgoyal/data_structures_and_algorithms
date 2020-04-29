'''
    WIP
'''
from random import randint, seed
import math

from point import Point


def sort_points(points):
    return sorted(points)


def get_points(n):
    range_val = 5
    seed(range_val)
    points = []
    for _ in range(n):
        point = Point(randint(-range_val, range_val),
                      randint(-range_val, range_val))
        points.append(point)
    points = [
        Point(0, 2),
        Point(-3, 2),
        Point(-4, -2),
        Point(-3, -3),
        Point(0, -3),
        Point(2, 0),
        Point(0, 0),
        Point(-2, 0),
        Point(-1, 0),
    ]
    return points


def get_next_point(fp, sp, points_array):
    print("First Point: {} Second Point: {}".format(fp, sp))
    min_radian = None
    min_point = None
    l = len(points_array)
    for i in range(0, l):
        if fp != points_array[i]:
            radian = fp.angle(points_array[i])
            # print("Radian of point:{} with point:{} is:{}".format(
            #     fp, points_array[i], radian))
            if min_radian is None:
                min_point = points_array[i]
                min_radian = radian
            if radian < min_radian:
                min_point = points_array[i]
                min_radian = radian
    print(min_radian)
    return min_point


def is_convex(p1, p2, p3):
    ang_1 = p1.angle(p2)
    ang_2 = p2.angle(p3)
    return (ang_1 - ang_2) < 180


def main():
    N = 10
    points = sort_points(get_points(N))
    print(points)
    start_point = points[0]
    print("start_point: {}".format(start_point))
    convex_hull = [start_point]

    for p in points[1:]:
        if len(convex_hull) < 3:
            convex_hull.append(p)
        else:
            p3 = p
            p2 = convex_hull.pop()
            p1 = convex_hull.pop()
            while not is_convex(p1, p2, p3):
                convex_hull.append(p1)
                convex_hull.append(p1)
                convex_hull.append(p3)

    # next_point = get_next_point(start_point, points)
    # print("Next Point: {}".format(next_point))
    # points.remove(next_point)
    # convex_hull.append(next_point)

    # first_point = start_point
    # second_point = next_point

    # while next_point != start_point:
    #     next_point = get_next_point(first_point, second_point, points)
    #     first_point = second_point
    #     second_point = next_point
    #     # if start_point not in points:
    #     # points.append(start_point)

    #     points.remove(next_point)
    #     convex_hull.append(next_point)
    #     print("Next Point: {}".format(next_point))
    # print("Convex Hull: {}".format(convex_hull))


if __name__ == "__main__":
    main()
