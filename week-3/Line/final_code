class Point:
    """point object"""
    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


class Line:
    """line object"""
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def intersect(self, other):
        """check if two lines intersect"""
        y_diff1 = self.point2.y - self.point1.y
        x_diff1 = self.point1.x - self.point2.x
        constant1 = y_diff1 * (self.point1.x) + x_diff1 * (self.point1.y)
        
        y_diff2 = other.point2.y - other.point1.y
        x_diff2 = other.point1.x - other.point2.x
        constant2 = y_diff2 * (other.point1.x) + x_diff2 * (other.point1.y)

        determinant = y_diff1 * x_diff2 - y_diff2 * x_diff1

        if determinant == 0:
            if y_diff1 * other.point1.x + x_diff1 * other.point1.y == constant1 and \
                    y_diff1 * other.point2.x + x_diff1 * other.point2.y == constant1:
                return self
            return None

        intersection_x = (x_diff2 * constant1 - x_diff1 * constant2) / determinant
        intersection_y = (y_diff1 * constant2 - y_diff2 * constant1) / determinant
        return Point(intersection_x, intersection_y)
