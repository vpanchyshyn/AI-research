class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

class Line:
    def __init__(self, point1, point2):
        if not isinstance(point1, Point) or not isinstance(point2, Point):
            raise ValueError('Параметри мають бути об\'єктами класу Point')
        self.point1 = point1
        self.point2 = point2
        if point1 == point2:
            raise Exception
        try:
            self.k, self.b = self.calculate_coefficients()
        except ZeroDivisionError:
            self.k, self.b = float('inf'), float('inf')  # Vertical line case

    def calculate_coefficients(self):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        if x2 - x1 == 0:
            raise ZeroDivisionError('Лінія вертикальна')
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        return k, b

    def intersect(self, line):
        try:
            k_self, b_self = self.calculate_coefficients()
            k_line, b_line = line.calculate_coefficients()
        except ZeroDivisionError:
            if self.point1.x == line.point1.x:  # Check if lines are vertically aligned
                if self.point1 == line.point1 or self.point1 == line.point2:
                    return self.point1  # Return common endpoint
                elif self.point2 == line.point1 or self.point2 == line.point2:
                    return self.point2  # Return common endpoint
                else:
                    return None  # No common points for parallel vertical lines
            return None  # No intersection for parallel non-vertical lines
        if k_self == k_line and b_self == b_line:
            return self  # Lines are identical
        if k_self == k_line:
            return None  # Lines are parallel and non-identical
        x = (b_line - b_self) / (k_self - k_line)
        y = k_self * x + b_self
        return Point(x, y)  # Intersection point
