class Vehicle:
    """ Транспортное средство """

    def __init__(self, model, vehicle_type):
        self.model = model
        self.vehicle_type = vehicle_type
    def horse_powers(self):
        return 300

    def __str__(self):
        return 'model {} , марка {}, мощность {}' .format(self.__class__.__name__, self.vehicle_type, horse_powers)

class Car:
    """ Машина """
    price = 200000

    def horse_powers(self):
        return 200


class Nissan(Vehicle, Car):
    vehicle_type = 'z51'
    price = 1000000

    def horse_powers(self):
       return 120

" Вывод "
my_car = Nissan('model', 'z51')
vehicle = my_car.vehicle_type
price = my_car.price
horse_powers = my_car.horse_powers()
print(my_car)
print(vehicle)
print(price)
print(horse_powers)