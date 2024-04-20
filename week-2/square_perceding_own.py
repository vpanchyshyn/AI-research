"""
Square preceding module."""
def square_preceding(values: list) -> None:
    """
    Replace each item in the list with square the value of the 
    preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    if not isinstance(values, list):
        raise TypeError("The item is not a list!")
    if values != [] and len(values) > 1: # [1, 2, 3]
        previous = values[0] # 1
        for i in range(1, len(values)): # from 1 to 3 including
            current = values[i]
            values[i] = previous ** 2
            previous = current
        values[0] = 0 # [0, 1, 2, 3]
    elif values != [] and len(values) == 1 and values != [0]: # [5]
        values[0] = 0
    elif values != [] and len(values) == 1 and values == [0]: # [0]
        values = [0]
