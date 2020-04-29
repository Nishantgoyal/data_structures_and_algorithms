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
        x_mag = float(self._x - point._x)
        y_mag = float(self._y - point._y)
        if x_mag == 0:
            angle = 90 if y_mag > 0 else -90
        angle = math.degrees(math.atan(y_mag / x_mag))
        print("angle between {} and {} is {}".format(self, point, angle))
        return angle


if __name__ == "__main__":
    p1 = Point(0, -10)
    p2 = Point(0, 10)
    print(p1 not in [p1, p2])
    print("Angle in radian: {}".format(p1.angle(p2)))
