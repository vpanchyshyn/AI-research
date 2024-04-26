import unittest

class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        point = Point(1, 2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

class TestLine(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(1, 1)
        self.point2 = Point(2, 2)
        self.point3 = Point(3, 3)
        self.point4 = Point(4, 4)

    def test_line_creation(self):
        line = Line(self.point1, self.point2)
        self.assertEqual(line.point1, self.point1)
        self.assertEqual(line.point2, self.point2)

    def test_line_creation_with_invalid_points(self):
        with self.assertRaises(ValueError):
            Line(self.point1, (2, 2))  # Should raise ValueError because the second argument is not a Point object

    def test_calculate_coefficients(self):
        line = Line(self.point1, self.point2)
        self.assertEqual(line.calculate_coefficients(), (1, 0))

    def test_intersect(self):
        line1 = Line(self.point1, Point(5,5))
        line2 = Line(self.point3, Point(0,5))
        intersection_point = line1.intersect(line2)
        self.assertIsInstance(intersection_point, Point)
        self.assertEqual(int(intersection_point.x), 3)
        self.assertEqual(int(intersection_point.y), 3)

    def test_intersect_with_parallel_lines(self):
        line1 = Line(self.point1, self.point2)
        line2 = Line(Point(2, 1), Point(3, 2))  # Parallel line to line1
        intersection_point = line1.intersect(line2)
        self.assertIsNone(intersection_point)  # Should return None for parallel lines

    def test_intersect_with_vertical_line(self):
        line1 = Line(Point(1, 1), Point(1, 2))  # Vertical line
        line2 = Line(Point(2, 3), Point(2, 1))
        intersection_point = line1.intersect(line2)
        print(type(intersection_point))
        self.assertIsNone(intersection_point)  # Should return None for vertical line intersecting non-vertical line

if __name__ == '__main__':
    unittest.main()
