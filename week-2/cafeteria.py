"""Cafeteria"""

RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }

class Track:
    """Tracks the order."""
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    __beans = 5000
    __milk = 20000
    safety = True

    def __init__(self, date: str) -> None:
        """
        Initializes track object.
        >>> day_track = Track('07.02.2024')
        >>> day_track.date
        '07.02.2024'
        """
        self.date = date
        self.orders = []

    def total_revenue(self):
        """total revenue"""
        return sum(order.price for order in self.orders)

    def total_milk(self):
        """total milk"""
        return sum(order.milk for order in self.orders)

    def total_beans(self):
        """total milk"""
        return sum(order.espresso/30*6 for order in self.orders)

    @property
    def beans(self):
        """beans"""
        return self.__beans - self.total_beans()

    @property
    def milk(self):
        """milk"""
        if self.__milk - self.total_milk() < 0 :
            return 0
        return self.__milk - self.total_milk()


    def milk_spoil(self, spoilt: int) -> None:
        """spoit milk remover"""
        self.__milk -= spoilt

    @classmethod
    def set_limit_milk(cls, amount: int):
        """new limit of milk"""
        cls.__milk = amount


    @classmethod
    def change_air_state(cls):
        """Changes air state"""
        cls.safety = not cls.safety

    def place_order(self, order):
        """
        Place order.
        >>> day_track = Track('07.02.2024')
        >>> order1 = Coffee('latte')
        >>> Coffee.set_recipe(RECIPE)
        >>> day_track.place_order(order1)
        >>> len(day_track.orders)
        1
        """
        if self.safety:
            if isinstance(order, Coffee):
                if order.name in self.MENU:
                    if order.milk<= self.milk and order.espresso/30*6 <= self.beans:
                        order.price = self.MENU[order.name]*order.count
                        order.is_paid = True
                        self.orders.append(order)
                        return 'Done!'
                    return "Unfortunately, we don't have enough ingredients."
                return "Unfortunately, we don't have such kind of coffee in the menu."
            return "We can't create anything that is not a Coffee instance."
        return 'Unfortunately, now it is not safe to make coffee.'


class Coffee:
    """Coffee class."""
    __recipe = None
    def __init__(self, name: str, count = None) -> None:
        """
        Initializes coffee object.
        >>> order1 = Coffee('latte', 2)
        >>> order1.name
        'latte'
        >>> order1.count
        2
        """
        self.name = name
        self.count = 1 if not count else count
        if self.__recipe and self.name in self.__recipe.keys():
            self.is_paid = False

    @classmethod
    def set_recipe(cls, recipe):
        """
        Sets recipe for coffee.
        >>> order1 = Coffee('latte')
        >>> order1._Coffee__recipe
        None
        """
        cls.__recipe = recipe


    @property
    def espresso(self):
        """
        Amout of espresso needed.
        >>> order1 = Coffee('latte')
        >>> order1.espresso
        """
        return self._Coffee__recipe[self.name].get('espresso', 0)*self.count


    @property
    def milk(self):
        """
        Amount of milk needed.
        """
        return sum([self._Coffee__recipe[self.name].get('steamed_milk', 0),
self._Coffee__recipe[self.name].get('foamed_milk', 0)])*self.count

    def __repr__(self) -> str:
        """string representation of coffee"""
        return f'{self.count} {self.name}'

    def __str__(self) -> str:
        """Text massege."""
        if not self.__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in self.__recipe.keys():
            return "Order cannot be created. We don't have recipe for it."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self.count} {self.name}" is created.'

    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        return self.name == other.name and self.count == other.count



class FlavorMixin:
    """Flavor Mixin"""
    def add_flavor(self, sugar: int, cinammon: bool, syrup: str):
        """Flavors"""
        if self.is_paid:
            self.sugar = sugar*self.count
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
            return 'Done!'
        return 'Please, pay for it.'


class CustomCoffee(Coffee, FlavorMixin):
    """Custom coffee"""
    def __init__(self, name: str, count=None) -> None:
        """initializes custom coffe object"""
        super().__init__(name, count)
        FlavorMixin.__init__(self)
        self.flavor = False

    def __str__(self) -> str:
        """info about order"""
        if self.flavor:
            flavours = []
            if self.sugar:
                flavours.append(f'{self.sugar} stickers of sugar')
            if self.cinammon:
                flavours.append('cinammon')
            if self.syrup:
                flavours.append(f'{self.syrup} syrup')
            return f'Your best {self.name} is ready! It has: {", ".join(flavours)}.'
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self.count} custom {self.name}" is created.'

    def __repr__(self) -> str:
        """string representation of custom coffee."""
        return f'{self.count} custom {self.name}'

    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        if not isinstance(self, CustomCoffee):
            return CustomCoffee(self.name, self.count).flavor == other.flavor
        if not isinstance(other, CustomCoffee):
            return self.name == other.name and self.count == other.count\
and CustomCoffee(other.name, other.count).flavor == self.flavor
        if isinstance(other, CustomCoffee) and isinstance(self, CustomCoffee):
            return self.name == other.name and self.count == other.count and\
other.flavor == self.flavor
        return self.name == other.name and self.count == other.count
