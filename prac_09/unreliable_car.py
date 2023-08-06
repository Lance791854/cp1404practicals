from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{self.name} drove {self._odometer}km with the reliability of {self.reliability}, {self.fuel} fuel left"

    def drive(self, distance):
        if self.reliability >= random.randint(0, 100):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
