
class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:
    def __init__(self, name, content=3):
        self.name = name
        self.content = content
        self.road_out = None
        self.set_road_out_1 = None
        self.queue_in = []
        self.queue_out = []
    def __str__(self):
        return 'Склад {} груза {}'.format(self.name, self.content)
    def set_road_out(self, road):
        self.set_road_out_1 = road
    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print('{} прибыл грузовик {}'.format(self.name, truck))

    def get_next_truck(self):
        if self.queue_in and self.queue_out != []:
            truck = self.queue_out.pop()
            return truck
        return 'Нет очереди'

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print('{} грузовик готов {}'.format(self.name, truck))
    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out())

class Vehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} топлива {}'.format(self.model, self.fuel)
    def tank_up(self):
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        print('{} заправился'.format(self.model))

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True

class Truck(Vehicle):
    fuel_rate = 50
    dead_time = 0
    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0
    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.cargo)
    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print('{} едет по дороге, осталось'.format(self.model, self.distance_to_target))
        else:
            self.place = self.place.end
            self.place.truck_arrived()
            print('{} доехал'.format(self.model))


    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print('{} выехал в путь'.format(self.model))
    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1

class AutoLoader(Vehicle):
    fuel_rate = 30
    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.truck)

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_next_truck()
                print('{} взял в работу {}'.format(self.model, self.truck))
            elif self.role == 'loader':
                self.load()
            else:
                self.unload()
            if self.truck is None:
                Truck.dead_time += 1


    def load(self):
        if not isinstance(self.truck, Truck):
            print('Мы никого не загрузили, потому что были пусты')
            return
        if self.warehouse.content == 0:
            print('{} на складе ничего нет!'.format(self.model))
            if self.truck:
                self.warehouse.truck_ready(self.truck)
                self.truck = None
            return
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            cargo = self.bucket_capacity
        else:
            cargo = truck_cargo_rest
        if self.warehouse.content < cargo:
            cargo = self.warehouse.content
            self.warehouse.content -= cargo
            self.truck.cargo += cargo
        print('{} грузил'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= self.truck.cargo
            self.truck.cargo += self.truck.cargo
        print('{} выгружал {}'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

TOTAL_CARGO = 100000

msc = Warehouse(name='Москва', content=TOTAL_CARGO)
spb = Warehouse(name='Питер', content=3)

msc_spb = Road(start=msc, end=spb, distance=715)
spb_msc = Road(start=spb, end=msc, distance=780)

msc.set_road_out(msc_spb)
spb.set_road_out(spb_msc)

loader1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=msc, role='loader')
loader2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=spb, role='unloader')

trucks = []
for number in range(2):
    truck = Truck(model='КАМАЗ # {}'.format(number), body_space=5000)
    msc.truck_arrived(truck)
    trucks.append(truck)

hour = 0
while spb.content < TOTAL_CARGO:
    hour += 1
    print('---------- Час {} ----------'.format(hour))
    for truck in trucks:
        truck.act()
    loader1.act()
    loader2.act()
    msc.act()
    spb.act()
    for truck in trucks:
        print(truck)
    print(loader1)
    print(loader2)
    print(msc)
    print(spb)


print('всего затраченно топлива {}'.format(Vehicle.total_fuel))