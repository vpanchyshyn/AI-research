"""
Line module."""
class Point:
    """
    Point class."""
    def __init__(self, x: float, y: float) -> None:
        """
        Initializes Point class attributes."""
        self.x = x
        self.y = y

class Line:
    """
    Line class."""
    def __init__(self, point_1: 'Point', point_2: 'Point') -> None:
        """
        Initializes Line class attributes."""
        if (point_1.x, point_1.y) != (point_2.x, point_2.y):
            self.point_1 = point_1
            self.point_2 = point_2
        else:

            raise ValueError("Can't create the line from equal points")

    def intersect(self, other_line: 'Line'):
        """
        Checks whether lines intersect or not."""
        try:
            k_1 = (self.point_2.y - self.point_1.y)/(self.point_2.x - self.point_1.x)
            b_1 = self.point_1.y - (k_1*self.point_1.x)
        except ZeroDivisionError: # that means x2 = x1
            k_1 = 1
            x_point = self.point_1.x
            b_1 = None

        try:
            k_2 = (other_line.point_2.y - other_line.point_1.y)/(
                other_line.point_2.x - other_line.point_1.x)
            b_2 = other_line.point_1.y - (k_2*other_line.point_1.x)
        except ZeroDivisionError:
            k_2 = 1
            x_point = other_line.point_1.x
            b_2 = None

        if k_1 and k_2:
            if not b_1 is None and not b_2 is None:
                if k_1 == k_2:
                    if b_1 == b_2:
                        return self
                    return None
                x_point = (b_2 - b_1)/(k_1 - k_2)
                y_point = (k_1*x_point) + b_1
                return Point(x_point, y_point)
            return None
        if not k_1 and k_2:
            if b_1 is not None and b_2 is not None:
                x_point = (b_2 - b_1)/(k_1 - k_2)
                y_point = (k_1*x_point) + b_1
                return Point(x_point, y_point)
            x_point = other_line.point_1.x
            return Point(x_point, b_1)
        if k_1 and not k_2:
            if b_1 is not None and b_2 is not None:
                x_point = (b_2 - b_1)/(k_1 - k_2)
                y_point = (k_1*x_point) + b_1
                return Point(x_point, y_point)
            x_point = self.point_1.x
            return Point(x_point, b_2)
        if b_1 == b_2:
            return self
        return None
# return None
