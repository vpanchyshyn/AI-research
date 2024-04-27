"""
The equation module."""

import math
import copy

class Polynomial:
    """
    Polynomial class."""
    def __init__(self, coeffs: list | tuple) -> None:
        """
        Initializes Polynomial class."""
        if isinstance(coeffs, tuple):
            coeffs = list(coeffs)

        if len(coeffs) == 1 and 0 in coeffs:
            self.coeffs = [0]
            self.degree = 0
        else:
            while coeffs[0] == 0:
                coeffs = coeffs[1::]
                if len(coeffs) == 1:
                    self.coeffs = [0]
                    self.degree = 0
                    break
            self.coeffs = coeffs[::-1]
            if len(coeffs) == 1:
                self.degree = 0
            else:
                self.degree = len(coeffs) - 1

    def __str__(self) -> str:
        """
        Returns a string."""
        poly = []
        deg_counter = self.degree
        if len(self.coeffs) == 0:
            return 'Polynomial: []'
        if len(self.coeffs) == 1 and 0 in self.coeffs:
            return 'Polynomial: 0'
        for coef in self.coeffs[::-1]:
            if coef != 0:
                sign = '+' if coef > 0 else '-'
                coef_str = f'{sign}{abs(coef)}' if abs(coef) != 1 or deg_counter == 0 else sign
                term = f'{coef_str}x' if deg_counter > 0 else str(coef_str)
                term += f'**{deg_counter}' if deg_counter > 1 else ''
                poly.append(term)
            deg_counter -= 1
        poly_str = ''.join(poly).lstrip('+')
        return f'Polynomial: {poly_str}'

    def __repr__(self) -> str:
        """
        Returns a string."""
        return f'Polynomial(coeffs={self.coeffs[::-1]})'

    def eval_at(self, x_0):
        """
        Evaluates equation with x_0."""
        deg_counter = self.degree
        if len(self.coeffs) == 1:
            return self.coeffs[0]
        if len(self.coeffs) > 1:
            res = 0
            for coe in self.coeffs[::-1]:
                res += coe * (x_0**deg_counter)
                deg_counter -= 1
            return res
        return None

    def __eq__(self, __value: object) -> bool:
        """
        Checks the equality."""
        if isinstance(self, Polynomial) and isinstance(__value, int):
            if self.degree == 0:
                return self.coeffs[0] == __value
            return False
        if isinstance(self, Polynomial) and isinstance(__value, Polynomial):
            return self.coeffs == __value.coeffs
        return None

    def __hash__(self):
        """
        Computes the hash value for the Polynomial."""
        return hash(tuple(self.coeffs))

    def multiply_by_value(self, value):
        """
        Multiplies coeffs by given value."""
        new_coefs = []
        for coef in self.coeffs[::-1]:
            new_coefs.extend([coef * value])
        return Polynomial(new_coefs)

    @property
    def derivative(self):
        """
        Finds the derivative."""
        new_coeffs = []
        deg_count = self.degree
        for coef in self.coeffs[::-1]:
            new_coeffs.extend([coef * deg_count])
            deg_count -= 1
        if new_coeffs[-1] == 0:
            new_coeffs = new_coeffs[:-1]
        return Polynomial(new_coeffs)

    def __add__(self, other_poly: 'Polynomial'):
        """
        Adds two polynomials."""
        coeffs_self_cp = copy.deepcopy(self.coeffs)[::-1]
        coeffs_other_cp = copy.deepcopy(other_poly.coeffs)[::-1]
        if isinstance(self, Polynomial) and isinstance(other_poly, Polynomial):
            if len(self.coeffs) > len(other_poly.coeffs):
                for _ in range(len(self.coeffs) - len(other_poly.coeffs)):
                    coeffs_other_cp.insert(0, 0)
                combined = list(zip(coeffs_self_cp, coeffs_other_cp))
                new_coeffs = [sum(combo) for combo in combined]
                return Polynomial(new_coeffs)
            if len(self.coeffs) == len(other_poly.coeffs):
                combined = list(zip(coeffs_self_cp, coeffs_other_cp))
                new_coeffs = [sum(combo) for combo in combined]
                return Polynomial(new_coeffs)
            if len(self.coeffs) < len(other_poly.coeffs):
                for _ in range(len(other_poly.coeffs) - len(self.coeffs)):
                    coeffs_self_cp.insert(0, 0)
                combined = list(zip(coeffs_self_cp, coeffs_other_cp))
                new_coeffs = [sum(combo) for combo in combined]
                return Polynomial(new_coeffs)
        elif isinstance(self, Polynomial) and isinstance(other_poly, int):
            new_coeffs = coeffs_self_cp[:-1]
            new_coeffs.extend([coeffs_self_cp[-1]+other_poly])
            return Polynomial(new_coeffs)
        return None

    def __mul__(self, other_num: 'Polynomial'):
        """
        Multiplies two polynomials."""
        new_coeffs = []
        coeffs_self_cp = copy.deepcopy(self.coeffs)[::-1]
        coeffs_other_cp = copy.deepcopy(other_num.coeffs)[::-1]
        if isinstance(self, Polynomial) and isinstance(other_num, Polynomial):
            if len(self.coeffs) > len(other_num.coeffs):
                if other_num.coeffs == [0]:
                    return Polynomial(other_num.coeffs)
                for _ in range(len(self.coeffs) - len(other_num.coeffs)):
                    coeffs_other_cp.insert(0, 0)
                for coe in coeffs_other_cp:
                    if coe == 0:
                        new_coeffs.append(0)
                        continue
                    for ele in coeffs_self_cp:
                        new_coeffs.extend([coe * ele])
                return Polynomial(new_coeffs)
            if len(self.coeffs) == len(other_num.coeffs): # this case is wrong!!
                len_result = len(self.coeffs) + len(other_num.coeffs) - 1
                new_coeffs = [0] * len_result
                if 0 in coeffs_self_cp or 0 in coeffs_other_cp:
                    for coe in coeffs_other_cp:
                        if coe == 0:
                            new_coeffs.append(0)
                            continue
                        for ele in coeffs_self_cp:
                            new_coeffs.extend([coe * ele])
                    return Polynomial(new_coeffs)
                if 0 not in coeffs_self_cp and 0 not in coeffs_other_cp:
                    for i, coef_self in enumerate(self.coeffs[::-1]):
                        for j, coef_other in enumerate(other_num.coeffs[::-1]):
                            new_coeffs[i + j] += coef_self * coef_other
                    return Polynomial(new_coeffs)
            if len(self.coeffs) < len(other_num.coeffs):
                if self.coeffs == [0]:
                    return Polynomial(self.coeffs)
                for _ in range(len(other_num.coeffs) - len(self.coeffs)):
                    coeffs_self_cp.insert(0, 0)
                for coe in coeffs_other_cp:
                    if coe == 0:
                        new_coeffs.append(0)
                        continue
                    for ele in coeffs_self_cp:
                        new_coeffs.extend([coe * ele])
                return Polynomial(new_coeffs)
        elif isinstance(self, Polynomial) and isinstance(other_num, int):
            for coef in coeffs_self_cp:
                new_coeffs.extend([coef*other_num])
            return Polynomial(new_coeffs)
        return None

class Quadratic(Polynomial):
    """
    Quadratic class."""
    def __init__(self, coeffs: list | tuple) -> None:
        """
        Initializes Quadratic class."""
        super().__init__(coeffs)
        self.coeffs = self.coeffs[::-1]
        if len(self.coeffs) > 3:
            raise ValueError('Quadratic polynomial must have exactly 3 coefficients')
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]
        self.discriminant = (self.b**2) - (4*self.a*self.c)
        self.number_of_real_roots = (
            2 if self.discriminant > 0 else
            1 if self.discriminant == 0 else
            0)

    def __repr__(self) -> str:
        """
        Returns a string."""
        if 0 not in self.coeffs:
            return f'Quadratic(a={self.a}, b={self.b}, c={self.c})'
        if 0 in self.coeffs[1]:
            return f'Quadratic(a={self.a}, c={self.c})'
        if 0 in self.coeffs[2]:
            return f'Quadratic(a={self.a}, b={self.b}'
        return None

    def __str__(self) -> str:
        """
        Returns a string."""
        return super().__str__().replace("Polynomial", "Quadratic")

    def get_real_roots(self):
        """
        Gets real roots of Quadratic equation."""
        if self.discriminant < 0:
            return []
        if self.discriminant == 0:
            x_1_2 = (-self.b) / (2*self.a)
            return [x_1_2]
        if self.discriminant > 0:
            x_1 = (-self.b-math.sqrt(self.discriminant)) / (2*self.a)
            x_2 = (-self.b+math.sqrt(self.discriminant)) / (2*self.a)
            return [x_1, x_2]
        return None
