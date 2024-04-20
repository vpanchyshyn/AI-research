"""
This module contains 2 functions. The first one builds table
of numbers of size n by m. The second one returns a single
list consisting of all non-empty elements of each of the input lists.
"""
def create_table(n: int, m: int) -> list[list]:
    """
    The function builds a table of numbers of size n by m
    (n - the number of rows, m - the number of columns in the table).
    >>> create_table(4, 6) 
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    def fill(i, j, table):
        """
        Fill the table with numbers recursively
        """
        if i == 0 or j == 0:
            return 1
        table[i][j] = fill(i - 1, j, table) + fill(i, j - 1, table)
        return table[i][j]

    table = [[1] * m for _ in range(n)]
    fill(n - 1, m - 1, table)
    return table

def flatten(lst: list) -> list | float:
    """
    The flatten(lst) function returns a single list consisting of
    all non-empty elements of each of the input lists.
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

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
