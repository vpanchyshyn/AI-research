'''Прибульці та IQ'''
# Після оптимізації ChatGPT час виконання зменшився з 8.06 с до 4.85 с
# та після оптимізації ШІ зламав саму логіку коду, через що не працює повноцінно з великими файлами
# і не проходить усі тести

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


def rescue_people_gpt(smarties: dict[str, int], limit_iq: int) -> tuple[int, list[list[str]]]:
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
    # Sort the smarties by IQ in descending order
    smarties = sorted(smarties.items(), key=lambda x: x[1], reverse=True)

    rides = []
    remaining_capacity = limit_iq

    current_ride = []
    for name, iq in smarties:
        if iq <= remaining_capacity:
            current_ride.append(name)
            remaining_capacity -= iq
        else:
            rides.append(current_ride)
            current_ride = [name]
            remaining_capacity = limit_iq - iq

    if current_ride:
        rides.append(current_ride)

    return len(rides), rides
