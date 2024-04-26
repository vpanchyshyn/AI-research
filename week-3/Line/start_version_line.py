"""code6"""
class Point:
    """code6"""
    def __init__(self,x,y):
        """code6"""
        self.x = x
        self.y = y
    def __eq__(self, _other):
        if isinstance(_other, Point):
            if self.x == _other.x and self.y == _other.y:
                raise ValueError('Ну не вийде створити такої лінії')
class Line:
    """code6"""
    def __init__(self, point1, point2):
        """code6"""
        if not isinstance(point1, Point) or not isinstance(point2, Point):
            raise ValueError('Має будуть Point')
        self.point1 = point1
        self.point2 = point2
        try:
            self.k, self.b = self.calculate_coefficients()
        except TypeError:
            return None
    def calculate_coefficients(self):
        """code6"""
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        if x2 - x1 == 0:
            return None
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        return k, b
    def intersect(self, line):
        """code6"""
        x1 = self.point1.x, self.point1.y
        x2 = self.point2.x, self.point2.y
        if x2 - x1 == 0:
            return None
        try:
            k_self, b_self = self.calculate_coefficients()
            k_line, b_line = line.calculate_coefficients()
        except TypeError:
            return None
        if k_self == k_line and b_self == b_line:
            return self
        try:
            x = (b_line - b_self) / (k_self - k_line)
        except ZeroDivisionError:
            return None
        y = k_self * x + b_self
        return Point(x, y)
