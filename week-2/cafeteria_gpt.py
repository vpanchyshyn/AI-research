RECIPE = {
    "espresso": {
        'espresso': 30
    },
    "latte": {
        'espresso': 60,
        'steamed_milk': 120,
        'foamed_milk': 15
    },
    "macchiato": {
        'espresso': 60,
        'foamed_milk': 15
    },
    "flat white": {
        'espresso': 60,
        'steamed_milk': 120
    },
    "dopio": {
        'espresso': 60
    },
    "cappuccino": {
        'espresso': 60,
        'steamed_milk': 60,
        'foamed_milk': 60
    },
    "lungo": {
        'espresso': 90
    },
    "cortado": {
        'espresso': 60,
        'steamed_milk': 60
    }
}

class Track:
    MENU = {
        "espresso": 40,
        "latte": 70,
        "flat white": 70,
        "dopio": 50,
        "cappuccino": 60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60
    }
    __beans = 5000
    __milk = 20000
    safety = True

    def __init__(self, date) -> None:
        self.date = date
        self.orders = []

    @property
    def beans(self):
        return self.__beans - self.total_beans() if self.__beans >= self.total_beans() else 0

    @property
    def milk(self):
        m = self.__milk - self.total_milk()
        return m if m >= 0 else 0

    def total_milk(self):
        return sum(order.milk for order in self.orders)

    def total_beans(self):
        return sum(order.espresso for order in self.orders) / 5

    def place_order(self, other:'Coffee'):
        if self.safety is False:
            return 'Unfortunately, now it is not safe to make coffee.'
        if not isinstance(other, Coffee):
            return "We can't create anything that is not a Coffee instance."
        if self.beans - other.espresso/5 < 0 or self.milk - other.milk < 0:
            return "Unfortunately, we don't have enough ingredients."
        if other.name not in self.MENU:
            return "Unfortunately, we don't have such kind of coffee in the menu."

        other.price = self.MENU[other.name] * other.count
        other.is_paid = True
        self.orders.append(other)
        return 'Done!'

    def total_revenue(self):
        return sum(order.price for order in self.orders)

    def milk_spoil(self, sp_m):
        self.__milk = max(self.__milk - sp_m, 0)

    @classmethod
    def set_limit_milk(cls, value):
        cls.__milk = value

    @classmethod
    def change_air_state(cls):
        cls.safety = not cls.safety


class Coffee:
    __recipe = {}

    def __init__(self, name, count=1) -> None:
        self.name = name
        self.count = count
        if self.__recipe and self.name in self.__recipe:
            self.is_paid = False

    @classmethod
    def set_recipe(cls, recipe):
        cls.__recipe = recipe

    @property
    def espresso(self):
        return self.__recipe[self.name]['espresso'] * self.count

    @property
    def milk(self):
        if 'steamed_milk' in self.__recipe[self.name] and 'foamed_milk' in self.__recipe[self.name]:
            return (self.__recipe[self.name]['steamed_milk'] + self.__recipe[self.name]['foamed_milk']) * self.count
        if 'steamed_milk' in self.__recipe[self.name] and 'foamed_milk' not in self.__recipe[self.name]:
            return self.__recipe[self.name]['steamed_milk'] * self.count
        if 'steamed_milk' not in self.__recipe[self.name] and 'foamed_milk' in self.__recipe[self.name]:
            return self.__recipe[self.name]['foamed_milk'] * self.count
        return 0

    def __str__(self) -> str:
        if not self.__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in RECIPE:
            return "Order cannot be created. We don't have recipe for it."
        if self.__recipe and not self.is_paid:
            return f'Order "{repr(self)}" is created.'
        if self.__recipe and self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return "We don't have this kind of drinks."

    def __repr__(self) -> str:
        return f'{self.count} {self.name}'

    def __eq__(self, other: 'Coffee') -> bool:
        if self.name == other.name and self.count == other.count:
            return True
        return False


class FlavorMixin:
    def add_flavor(self, sugar, cinammon, syrup):
        if self.is_paid:
            self.flavor = True
            self.sugar = sugar * self.count
            self.cinammon = cinammon
            self.syrup = syrup
            return 'Done!'
        return 'Please, pay for it.'


class CustomCoffee(Coffee, FlavorMixin):
    def __init__(self, name, count=1, flavor=False) -> None:
        Coffee.__init__(self, name, count)
        self.flavor = flavor

    def __str__(self) -> str:
        if self.flavor:
            if self.sugar > 0 and self.cinammon and self.syrup:
                return f'Your best {self.name} is ready! It has: {self.sugar} stickers of sugar, cinammon, {self.syrup} syrup.'
            if self.sugar > 0 and self.cinammon and not self.syrup:
                return f'Your best {self.name} is ready! It has: {self.sugar} stickers of sugar, cinammon.'
            if self.sugar > 0 and not self.cinammon and self.syrup:
                return f'Your best {self.name} is ready! It has: {self.sugar} stickers of sugar, {self.syrup} syrup.'
            if not self.sugar > 0 and self.cinammon and self.syrup:
                return f'Your best {self.name} is ready! It has: cinammon, {self.syrup} syrup.'
            if self.sugar > 0 and not self.cinammon and not self.syrup:
                return f'Your best {self.name} is ready! It has: {self.sugar} stickers of sugar.'
            if not self.sugar > 0 and self.cinammon and not self.syrup:
                return f'Your best {self.name} is ready! It has: cinammon.'
            if not self.sugar > 0 and not self.cinammon and self.syrup:
                return f'Your best {self.name} is ready! It has: {self.syrup} syrup.'
        return Coffee.__str__(self)

    def __repr__(self) -> str:
        return f'{self.count} custom {self.name}'

    def __eq__(self, other: 'Coffee') -> bool:
        if self.name == other.name and self.count == other.count:
            if isinstance(self, CustomCoffee) and isinstance(other, CustomCoffee):
                if self.flavor == other.flavor:
                    return True
                return False
            if isinstance(self, CustomCoffee) and not isinstance(other, CustomCoffee):
                if self.flavor is False:
                    return True
                return False
            if not isinstance(self, CustomCoffee) and isinstance(other, CustomCoffee):
                if other.flavor is False:
                    return True
                return False
        return False

