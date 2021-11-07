from abc import abstractmethod, ABC


class FriedChicken(ABC):
    def __init__(self, price, qty, breast, legs):
        self.price = price
        self.qty = qty
        self.breast = breast
        self.legs = legs


class ChickenWings(ABC):
    def __init__(self, price, qty):
        self.price = price
        self.qty = qty


class ChickenBurguer(ABC):
    def __init__(self, bun, pickles, cheese, mustard, ketchup):
        self.bun = bun
        self.pickles = pickles
        self.cheese = cheese
        self.mustard = mustard
        self.ketchup = ketchup
