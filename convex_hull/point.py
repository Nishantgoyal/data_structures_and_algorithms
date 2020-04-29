import math


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return "({},{})".format(self._x, self._y)

    def __eq__(self, point):
        if self._x == point._x and self._y <= point._y:
            return True
        return False

    def __ne__(self, point):
        return not self == point

    def __le__(self, point):
        if self._x <= point._x:
            return True
        if self._x == point._x and self._y <= point._y:
            return True
        return False

    def __lt__(self, point):
        if self._x < point._x:
            return True
        if self._x == point._x and self._y < point._y:
            return True
        return False

    def __ge__(self, point):
        return self <= point

    def __gt__(self, point):
        return self < point

    def distance(self, point):
        x_mag = (self._x - point._x)
        y_mag = (self._y - point._y)
        dist = (x_mag ** 2 + y_mag ** 2) ** 0.5
        return dist

    def angle(self, point):
        angle_self = math.atan2(self._x, self._y)
        angle_point = math.atan2(point._x, point._y)
        # return math.degrees(angle_self - angle_point)
        return (angle_self - angle_point)


p1 = Point(0, -10)
p2 = Point(0, 10)
print("Angle in radian: {}".format(p1.angle(p2)))
