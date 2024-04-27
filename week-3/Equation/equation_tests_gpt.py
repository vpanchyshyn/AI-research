import unittest
import math
from equation import Polynomial, Quadratic

class TestPolynomial(unittest.TestCase):
    def test_polynomial_initialization(self):
        poly = Polynomial([1, 2, 3])
        self.assertEqual(poly.coeffs, [1, 2, 3])

    def test_polynomial_basics(self):
        # Basic properties and string representations
        p1 = Polynomial([5])
        self.assertEqual(p1.degree, 0)
        self.assertEqual(p1.coeffs, [5])
        self.assertEqual(str(p1), "Polynomial: 5")
        self.assertEqual(repr(p1), "Polynomial(coeffs=[5])")

        p2 = Polynomial([3, 5])
        self.assertEqual(p2.degree, 1)
        self.assertEqual(p2.coeffs, [5, 3])
        self.assertEqual(str(p2), "Polynomial: 3x+5")

        p3 = Polynomial([1, 5])
        self.assertEqual(str(p3), "Polynomial: x+5")

        p4 = Polynomial([1, 2, 3])
        self.assertEqual(p4.degree, 2)
        self.assertEqual(p4.coeffs, [3, 2, 1])
        self.assertEqual(str(p4), "Polynomial: x**2+2x+3")
        self.assertEqual(repr(p4), "Polynomial(coeffs=[1, 2, 3])")

        # Testing eval_at
        self.assertEqual(p1.eval_at(0), 5)
        self.assertEqual(p1.eval_at(2), 5)
        self.assertEqual(p2.eval_at(0), 5)
        self.assertEqual(p2.eval_at(2), 11)

        # Testing polynomial equality and inequality
        self.assertTrue(Polynomial([1, 2, 3]) == Polynomial([1, 2, 3]))
        self.assertFalse(Polynomial([1, 2, 3]) == Polynomial([1, 2, 3, 0]))
        self.assertFalse(Polynomial([1, 2, 3]) == Polynomial([1, 2, 0, 3]))
        self.assertFalse(Polynomial([1, 2, 3]) == Polynomial([1, -2, 3]))
        self.assertFalse(Polynomial([1, 2, 3]) == 42)
        self.assertFalse(Polynomial([1, 2, 3]) == "Wahoo!")

        # Testing multiplication by scalar
        p10 = p4.multiply_by_value(10)
        self.assertIsInstance(p10, Polynomial)
        self.assertEqual(str(p10), 'Polynomial: 10x**2+20x+30')

        # Testing derivatives
        p11 = p4.derivative
        self.assertIsInstance(p11, Polynomial)
        self.assertEqual(str(p11), "Polynomial: 2x+2")

        # Testing addition
        p5 = Polynomial([2, -3, 5])
        p8 = Polynomial([-1, 0, 0])
        p12 = p5 + p8
        self.assertIsInstance(p12, Polynomial)
        self.assertEqual(str(p12), "Polynomial: x**2-3x+5")

        # Testing multiplication
        p13 = p5 * p8
        self.assertIsInstance(p13, Polynomial)
        self.assertEqual(str(p13), "Polynomial: -2x**4+3x**3-5x**2")

        # Testing constructor with tuple and set behavior
        coeffs = (0, 0, 0, 1, 2)
        poly_from_tuple = Polynomial(coeffs)
        self.assertEqual(poly_from_tuple, Polynomial([1, 2]))
        s = set()
        s.add(poly_from_tuple)
        self.assertIn(poly_from_tuple, s)

    def test_repr_poly(self):
        # Ascending order for coefficients: c0 + c1*x + c2*x^2 ...
        poly = Polynomial([1, 2, 3])  # represents 1 + 2x + 3x^2
        self.assertEqual(repr(poly), "Polynomial(coeffs=[1, 2, 3])")

        # Testing edge cases like zero or negative coefficients
        poly = Polynomial([0, 0, 1])
        self.assertEqual(repr(poly), "Polynomial(coeffs=[1])")  # assuming leading zeros are stripped

        poly = Polynomial([-1, -2, -3])
        self.assertEqual(repr(poly), "Polynomial(coeffs=[-1, -2, -3])")

    def test_quadratic_specifics(self):
        q1 = Quadratic([3, 2, 1])
        self.assertEqual(q1.discriminant, -8)
        self.assertEqual(q1.number_of_real_roots, 0)
        self.assertEqual(q1.get_real_roots(), [])

        q2 = Quadratic([1, -6, 9])
        self.assertEqual(q2.discriminant, 0)
        self.assertEqual(q2.number_of_real_roots, 1)
        self.assertEqual(q2.get_real_roots(), [3])

        q3 = Quadratic([1, 1, -6])
        self.assertEqual(q3.discriminant, 25)
        self.assertEqual(q3.number_of_real_roots, 2)
        roots = q3.get_real_roots()
        self.assertTrue(math.isclose(roots[0], -3))
        self.assertTrue(math.isclose(roots[1], 2))

    def test_repr_quadr(self):
        # Properly creates a quadratic polynomial and checks the __repr__ output
        quad = Quadratic([1, -2, 1])
        self.assertEqual(repr(quad), "Quadratic(a=1, b=-2, c=1)")

        # Checking for zero coefficients
        quad = Quadratic([0, 0, 0])
        self.assertEqual(repr(quad), "Quadratic(a=0, b=0, c=0)")

        # Negative and zero coefficients combination
        quad = Quadratic([0, -2, 3])
        self.assertEqual(repr(quad), "Quadratic(a=0, b=-2, c=3)")

    def test_repr_edge_cases_quadr(self):
        # Zero coefficients in Quadratic
        quad = Quadratic([0, 0, 0])
        self.assertEqual(repr(quad), "Quadratic(a=0, b=0, c=0)")

        # Negative coefficients
        quad = Quadratic([-1, -2, -3])
        self.assertEqual(repr(quad), "Quadratic(a=-1, b=-2, c=-3)")
        
        # Large coefficients
        quad = Quadratic([10**6, -10**6, 10**6])
        self.assertEqual(repr(quad), "Quadratic(a=10**6, b=-10**6, c=10**6)")

    def test_quadratic_initialization(self):
        quad = Quadratic([1, 2, 3])
        self.assertEqual(quad.coeffs, [1, 2, 3])
        
    def test_quadratic_repr(self):
        quad = Quadratic([1, -2, 1])
        self.assertEqual(repr(quad), "Quadratic(a=1, b=-2, c=1)")


if __name__ == '__main__':
    unittest.main()
