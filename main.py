#!/usr/bin/env python3
"""main.py file"""


class Car:
    def __init__(self, model, year, odo, trip, fuel):
        self.model = model
        self.year = year
        self.odo = odo
        self.trip = trip
        self.fuel = fuel

    def add_fuel(self, gallons):
        if self.fuel + gallons > 10.4:
            max_add = 10.4 - self.fuel
            print(f'Adding to much fuel add only {max_add} gallons')
        else:
            self.fuel += gallons

    def get_fuel_balance(self):
        return 10.4 - self.fuel

    def calc_mpg(self):
        return self.trip / self.fuel


def main():
    """main function"""
    my_car = Car('Corolla', 2009, 53476, 321.6, 5.5)
    print(f'Fuel balance {my_car.get_fuel_balance()}')
    my_car.add_fuel(5.0)
    my_car.add_fuel(4.9)
    print(f'Fuel balance {my_car.get_fuel_balance()}')
    my_car.fuel = 9.8
    mpg = my_car.calc_mpg()
    print(mpg)


if __name__ == "__main__":
    import sys
    sys.exit(main())
