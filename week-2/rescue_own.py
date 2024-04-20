"""Прибульці та IQ"""
def read_file(file_path: str) -> dict:
    """
    Reads file and returns dictionary with names and surnames as keys and level of IQ as values
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmpfile:
    ...     _ = tmpfile.write('#data from https://iqcertificate.org/famous-people-iq-score\\n\
Elon Musk,165\\n\
Mark Zuckerberg,152\\n\
Will Smith,157\\n\
Marilyn vos Savant,186')
    >>> read_file(tmpfile.name)
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186}
    """
    people = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ',' in line:
                line = line.strip().split(',')
                people[line[0]] = int(line[1])
            else:
                pass
    return people

def rescue_people(smarties: dict[str, int], limit_iq: int) -> tuple[int, list[list[str]]]:
    """
    Returns a tuple of the number of trips required and a list of lists, where each inner
    list represents a trip and contains the names of the people being transported on that 
    trip in the order in which they were chosen by the aliens.
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195, \
"Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({"Alice": 100, "Bob": 80, "Charlie": 90}, 180)
    (2, [['Alice', 'Bob'], ['Charlie']])
    """
    smarties = list(smarties.items())
    smarties = sorted(sorted(smarties), key=lambda pearson: pearson[1], reverse=True)

    rides = 0
    passengers = []
    while smarties:
        left = limit_iq
        ride = []
        i = 0
        while i < len(smarties):
            elem = smarties[i]
            if left >= elem[1]:
                left -= elem[1]
                ride.append(elem[0])
                del smarties[i]
            else:
                i += 1
        rides += 1
        passengers.append(ride)

    return rides, passengers
