from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import List
import datetime


class Dish(ABC):

    def __init__(self, price, size, typeOfFood, onDelivery):
        self.size = size
        self.price = price
        self.typeOfFood = typeOfFood
        self.onDelivery = onDelivery

    @abstractmethod
    def cook(self):
        pass


class FriedChicken(Dish):
    def __init__(self, price, size, typeOfFood, onDelivery, recipe):
        Dish.__init__(self, size, typeOfFood, onDelivery)
        self.recipe = recipe

    @abstractmethod
    def cook(self):
        pass


class SecretRecipe(FriedChicken):
    def __init__(self, price, size, typeOfFood, onDelivery, recipe):
        FriedChicken.__init__(
            self, price, size, typeOfFood, onDelivery, recipe)
        self.recipe = recipe
        self.price = size*5
        self.name = "Secret Recipe Fried Chicken"

    def cook(self):
        print("Cooking secret recipe fried chicken")


class CrispyFriedChicken(FriedChicken):
    def __init__(self, price, size, typeOfFood, onDelivery, recipe):
        FriedChicken.__init__(
            self, price, size, typeOfFood, onDelivery, recipe)
        self.recipe = recipe
        self.price = size*4
        self.name = "Crispy Fried Chicken"

    def cook(self):
        print("Cooking crispy fried chicken")


class ChickenWings(Dish):
    def __init__(self, price, size, typeOfFood, onDelivery, sauce):
        Dish.__init__(self, price, size, typeOfFood, onDelivery)
        self.price = size*3
        self.sauce = sauce
        self.name = "Chicken Wings"

    def cook(self):
        print("Cooking chicken wings")


class BuffaloWings(ChickenWings):
    def __init__(self, price, size, typeOfFood, onDelivery):
        ChickenWings.__init__(
            self, price, size, typeOfFood, onDelivery, sauce)
        self.price = size*4
        self.sauce = "Buffalo sauce"
        self.name = "Buffalo Wings"

    def cook(self):
        print("Cooking buffalo wings")

    class HabaneroWings(ChickenWings):
        def __init__(self, price, size, typeOfFood, onDelivery, sauce):
            ChickenWings.__init__(
                self, price, size, typeOfFood, onDelivery)
            self.price = size*5
            self.sauce = "Habanero sauce"
            self.name = "Habanero Wings"

        def cook(self):
            print("Cooking habanero wings")


class Identification():
    @abstractmethod
    def identify(self):
        pass


class DNI(Identification):
    def __init__(self, dni):
        self.dni = dni

    def identify(self):
        print("Identifying by DNI")


class DriverLicense(Identification):
    def __init__(self, license):
        self.license = license

    def identify(self):
        print("Identifying by Driver License")


class PayMethod():
    @abstractmethod
    def pay(self):
        pass


class DebitOrCreditCard(PayMethod):
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber

    def pay(self):
        print("Paying by debit or credit card")


class CryptoCurrency(PayMethod):
    def __init__(self, cryptoCurrency):
        self.cryptoCurrency = cryptoCurrency

    def pay(self):
        print("Paying by crypto currency")


@dataclass
class Purchase():
    Dishes: List[Dish]
    PaymentMethod: PayMethod
    Identification: Identification
    Service: str

    def __ne__(self):
        pass
