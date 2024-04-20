"""
Flower module."""

# link on cms: https://cms.ucu.edu.ua/mod/vpl/view.php?id=356092&userid=10019

class Flower:
    """
    Flower class."""
    def __init__(self, color, petals, price):
        """
        Initializes Flower attributes."""
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
    """
    Tulip class."""
    def __init__(self, petals, price):
        super().__init__('pink', petals, price)

class Rose(Flower):
    """
    Rose class."""
    def __init__(self, petals, price):
        super().__init__('red', petals, price)

class Chamomile(Flower):
    """
    Chamomile class."""
    def __init__(self, petals, price):
        super().__init__('white', petals, price)

class FlowerSet:
    """
    FlowerSet class."""
    def __init__(self) -> None:
        """
        Initializes FlowerSet."""
        self.flowers_set = []

    def add_flower(self, flower):
        """
        Adds flowers to a set."""
        if isinstance(flower, Flower):
            self.flowers_set.append(flower)
        else:
            raise TypeError("The flower must belong to a Flower class!")

class Bucket:
    """
    Bucket class."""
    def __init__(self) -> None:
        self.flower_bucket = []

    def add_set(self, set_of_flowers):
        """
        Adds sets of flowers to a bucket."""
        if not isinstance(set_of_flowers, FlowerSet):
            raise ValueError("The set of flowers must be a list!")
        self.flower_bucket.append(set_of_flowers.flowers_set)

    def total_price(self):
        """
        Counts total price of a bucket."""
        total = 0
        for bucket_of_fl in self.flower_bucket:
            for flower in bucket_of_fl:
                total += flower.price
        return total
  
