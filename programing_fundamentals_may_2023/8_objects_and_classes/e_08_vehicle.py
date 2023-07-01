
class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is None and money >= self.price:
            change = money - self.price
            return_statement = f"Successfully bought a {self.type}. Change: {change:.2f}"
            self.owner = owner
        elif money < self.price:
            return_statement = "Sorry, not enough money"
        else:
            return_statement = "Car already sold"
        return return_statement

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return_statement = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return_statement = f"{self.model} {self.type} is on sale: {self.price}"
        return return_statement


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
