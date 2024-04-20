"""
This module contains 2 functions. The first one builds table
of numbers of size n by m. The second one returns a single
list consisting of all non-empty elements of each of the input lists.
"""

# link on cms: https://cms.ucu.edu.ua/mod/vpl/view.php?id=361861&userid=10019

# Оскільки завдання не надто складне з алгоритмічного боку, то ChatGPT,
# отримавши просто початковий код та прохання його оптимізувати, справився з першої спроби.
# Час виконання ф-ї create_table та flatten скоротився з 10.7732 та 0.4229 секунд до 2.4892 та 0.4221, відповідно.
# Тобто для create_table ефективність покращилась аж на 8 секунд (за рахунок того, що уникнув рекурсію).
# Оскільки ф-я flatten згідно з умовою має бути рекурсивною, то тут ChatGPT не надто сильно зміг покращити ефективність коду.

def create_table(n: int, m: int) -> list[list]:
    """
    The function builds a table of numbers of size n by m
    (n - the number of rows, m - the number of columns in the table).
    The table is filled based on Pascal's triangle properties.
    >>> create_table(4, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    table = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table

def flatten(lst: list) -> list | float:
    """
    The flatten function returns a single list consisting of all
    non-empty elements of each of the input lists.
    The elements are ordered as in the original list.
    >>> flatten([1,[2]])
    [1, 2]
    >>> flatten([1, 2, [3, [4, 5], 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(['wow', [2, [[]]], [True]])
    ['wow', 2, True]
    >>> flatten([])
    []
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    """
    if not isinstance(lst, list):
        return lst

    flattened_lst = []
    for element in lst:
        if isinstance(element, list):
            flattened_lst.extend(flatten(element))
        elif element is not None:
            flattened_lst.append(element)
    return flattened_lst
