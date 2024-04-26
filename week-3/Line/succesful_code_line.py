"""intersections"""
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
        if self.point1 == self.point2:
            raise ValueError

    def intersect(self, other):
        """check if two lines intersect"""
        sub_1 = self.point2.y - self.point1.y
        sub_rev_1 = self.point1.x - self.point2.x
        sum_1 = sub_1 * (self.point1.x) + sub_rev_1 * (self.point1.y)
        sub_2 = other.point2.y - other.point1.y
        sub_rev_2 = other.point1.x - other.point2.x
        sum_2 = sub_2 * (other.point1.x) + sub_rev_2 * (other.point1.y)

        dit = sub_1 * sub_rev_2 - sub_2 * sub_rev_1

        if dit == 0:
            if sub_1 * other.point1.x + sub_rev_1 * other.point1.y == sum_1 and \
                    sub_1 * other.point2.x + sub_rev_1 * other.point2.y == sum_1:
                return self
            return None

        x = (sub_rev_2 * sum_1 - sub_rev_1 * sum_2) / dit
        y = (sub_1 * sum_2 - sub_2 * sum_1) / dit
        return Point(x, y)
