"""
Flower module"""

# link on cms: https://cms.ucu.edu.ua/mod/vpl/view.php?id=356092&userid=10019

# ChatGPT з першого промпту намагався лише оптимізувати код не робивши якоїсь стилізації.
# Проте коли був ще один промпт з проханням стилізувати код, то Чат надав коменти до своїх дій,
# які досить лаконічно пояснюють суть функцій.
# Також надає приклади використання, щоб одразу перевірити як працює код.

class Flower:
    """ A class representing a generic flower. """
    def __init__(self, color, petals, price):
        # Initialize a Flower object with color, number of petals, and price.
        # Ensures correct data types for attributes to prevent logical errors.
        if not isinstance(color, str):
            raise TypeError("The color is not a string!")
        if not isinstance(petals, int) or petals < 0:
            raise ValueError("Petals must be a non-negative integer")
        if not isinstance(price, int) or price < 0:
            raise ValueError("Price must be a non-negative integer")
        self.color = color
        self.petals = petals
        self.price = price

class Tulip(Flower):
    """ A class representing a tulip. """
    def __init__(self, petals, price):
        # Inherits from Flower, automatically setting the color to 'pink'
        # for all instances of Tulip.
        super().__init__('pink', petals, price)

class Rose(Flower):
    """ A class representing a rose. """
    def __init__(self, petals, price):
        # Inherits from Flower, automatically setting the color to 'red'
        # for all instances of Rose.
        super().__init__('red', petals, price)

class Chamomile(Flower):
    """ A class representing a chamomile. """
    def __init__(self, petals, price):
        # Inherits from Flower, automatically setting the color to 'white'
        # for all instances of Chamomile.
        super().__init__('white', petals, price)

class FlowerSet:
    """ A class to hold a collection of flowers. """
    def __init__(self):
        # Initializes an empty list to store Flower objects.
        self.flowers = []

    def add_flower(self, flower):
        # Adds a flower to the flower set if it's an instance of Flower,
        # otherwise raises a TypeError.
        if not isinstance(flower, Flower):
            raise TypeError("The flower must be an instance of Flower!")
        self.flowers.append(flower)

class Bucket:
    """ A class representing a bucket that can contain multiple sets of flowers. """
    def __init__(self):
        # Initializes an empty list to store FlowerSet objects.
        self.flower_sets = []

    def add_set(self, flower_set):
        # Adds a set of flowers to the bucket if it's an instance of FlowerSet,
        # otherwise raises a ValueError.
        if not isinstance(flower_set, FlowerSet):
            raise ValueError("The argument must be an instance of FlowerSet!")
        self.flower_sets.append(flower_set)

    def total_price(self):
        # Calculates and returns the total price of all flowers in all flower sets within the bucket.
        # Uses a nested generator expression to iterate over each flower set and each flower within those sets.
        return sum(flower.price for flower_set in self.flower_sets for flower in flower_set.flowers)

# Usage Example:
bucket = Bucket()
set1 = FlowerSet()
set1.add_flower(Tulip(5, 10))
set1.add_flower(Rose(7, 20))
bucket.add_set(set1)

print(f"Total Price: {bucket.total_price()}")  # Outputs the total price of all flowers in the bucket
