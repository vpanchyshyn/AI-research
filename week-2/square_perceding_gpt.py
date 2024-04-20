# link on cms: https://cms.ucu.edu.ua/mod/vpl/view.php?id=356092&userid=10019

# У цьому завданні та завданні flower ми намагаємося перевірити здатність ChatGPT стилізувати код.
# Тут ми бачимо, що першу дію з isinstance він не прокоментував, проте все решта він коментує лаконічно.
# Тобто можна зробити висновок, що у промпті варто вказувати побажання стилізувати код,
# оскільки Чат концентрується на тому, щоб надати рішення задачі.
# Але якщо просити написати задачу "з нуля", то тоді він сам коментує код, навіть якщо такого прохання не було.

def square_preceding(values: list) -> None:
    """
    Replace each item in the list with the square of the value of the 
    preceding item, and replace the first item with 0.
    
    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    if not isinstance(values, list):
        raise TypeError("The item must be a list!")

    # Check if the list is not empty.
    if values:
        # Initialize the first value to zero.
        # Save the first element's value to be used in the loop.
        previous = values[0]
        values[0] = 0

        # Loop over the list starting from the second element.
        for i in range(1, len(values)):
            # Store current value temporarily before modifying.
            current = values[i]
            # Set the current index to the square of the previous value.
            values[i] = previous ** 2
            # Update previous to the current value before modification.
            previous = current
