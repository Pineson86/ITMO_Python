class Bus:
    def __init__(self, number, doors):
        self.number = number
        self.doors = doors  # Теперь атрибут не защищенный
        self.driver = None
        self.engine_started = False
        self.doors_opened = False
        self.passengers = []

    def assign_driver(self, driver):
        if isinstance(driver, Driver):
            self.driver = driver
            driver.in_bus = True
            return f'{driver.name} is assigned as the driver of bus {self.number}'
        return 'Only a driver can be assigned to the bus'

    def start_engine(self):
        if self.driver and self.driver.in_bus:
            self.engine_started = True
            return f'Bus {self.number} engine started'
        else:
            return 'Bus cannot start without the driver in the bus'

    def goes(self):
        if self.driver and self.engine_started:
            return f'Bus {self.number} goes'
        else:
            return f'Bus {self.number} stops'

    def passenger_enters(self, passenger):
        if isinstance(passenger, Passenger) and passenger.ticket and self.doors_opened:
            self.passengers.append(passenger)
            passenger.in_bus = True
            return f'{passenger.name} entered the bus {self.number}'
        return 'Passenger cannot enter without a ticket or if doors are closed'

    def open_doors(self):
        if self.driver and self.driver.opens_doors():
            self.doors_opened = True
            return f'Doors of bus {self.number} are opened'
        else:
            return 'Doors cannot be opened'

class Person:
    def __init__(self, name):
        self.name = name
        self.in_bus = False

class Driver(Person):
    def __init__(self, name):
        super().__init__(name)

    def starts_engine(self):
        return 'Engine starts'

    def opens_doors(self):
        return True  # Driver can always open doors

    def say_something(self):
        return f'{self.name} says: "Please take your seats and hold on!"'

class Controller(Person):
    def __init__(self, name):
        super().__init__(name)

    def checks_ticket(self, passenger):
        if passenger.ticket:
            return True
        else:
            return False

    def say(self, passenger):
        if not self.checks_ticket(passenger):
            return 'Get out of here!'

class Passenger(Person):
    def __init__(self, name):
        super().__init__(name)
        self.ticket = False

    def buys_ticket(self):
        self.ticket = True
        return f'{self.name} bought a ticket'

# создаем объекты классов
driver = Driver("John")
controller = Controller("Tom")
passenger1 = Passenger("Alice")
passenger2 = Passenger("Bob")
bus = Bus(number=42, doors=True)

# Назначаем водителя автобуса
print(bus.assign_driver(driver))

# Водитель заводит автобус
print(bus.start_engine())

# Водитель говорит пассажирам занять свои места
print(driver.say_something())

# Пассажиры покупают билеты
print(passenger1.buys_ticket())
print(passenger2.buys_ticket())

# Водитель открывает двери
print(bus.open_doors())

# Пассажиры заходят в автобус
print(bus.passenger_enters(passenger1))
print(bus.passenger_enters(passenger2))

# Проверяем, может ли автобус ехать
print(bus.goes())
