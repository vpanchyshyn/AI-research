import unittest

class TestLineIntersect(unittest.TestCase):
    def test_parallel_lines(self):
        line1 = Line(Point(0, 0), Point(1, 1))
        line2 = Line(Point(1, 0), Point(2, 1))
        self.assertIsNone(line1.intersect(line2))  # Повинен повертати None, оскільки прямі паралельні

    def test_non_intersecting_lines(self):
        line1 = Line(Point(0, 0), Point(1, 1))
        line2 = Line(Point(0, 1), Point(1, 2))
        self.assertIsNone(line1.intersect(line2))  # Повинен повертати None, оскільки прямі не перетинаються

    def test_intersecting_lines(self):
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(0, 2), Point(2, 0))
        intersection_point = line1.intersect(line2)
        self.assertIsInstance(intersection_point, Point)  # Повинен повертати екземпляр класу Point
        self.assertAlmostEqual(intersection_point.x, 1.0)  # Перевірка координати x перетину
        self.assertAlmostEqual(intersection_point.y, 1.0)  # Перевірка координати y перетину

    def test_coinciding_lines(self):
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(-1, -1), Point(3, 3))  # Прямі збігаються
        intersection_point = line1.intersect(line2)
        self.assertEqual(intersection_point, line1.point1)  # Повинен повертати першу точку першої прямої

    def test_vertical_lines(self):
        line1 = Line(Point(1, 0), Point(1, 2))  # Вертикальна пряма
        line2 = Line(Point(0, 1), Point(2, 1))  # Горизонтальна пряма
        self.assertIsInstance(line1.intersect(line2), Point)

    def test_vertical_intersecting_lines(self):
        line1 = Line(Point(1, 0), Point(1, 2))  # Вертикальна пряма
        line2 = Line(Point(0, 1), Point(2, 1))  # Горизонтальна пряма
        intersection_point = line2.intersect(line1)
        self.assertIsInstance(intersection_point, Point)  # Повинен повертати екземпляр класу Point
        self.assertAlmostEqual(intersection_point.x, 1.0)  # Перевірка координати x перетину
        self.assertAlmostEqual(intersection_point.y, 1.0)  # Перевірка координати y перетину

if __name__ == '__main__':
    unittest.main()
