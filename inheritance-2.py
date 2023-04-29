class vehicle(object):
    def __init__(self, price, gas, color):
        self.price=price
        self.gas=gas
        self.color=color

    def filluptank(self):
        self.gas=1000

    def emptytank(self):
        self.gas(0)

    def gasleft(self):
        return self.gas

class car(vehicle):
    def __init__(self, gas, price, color, speed):
        super().__init__(price,gas,color)
        self.speed=speed

    def beep(self):
        print('beep beep')

class truck(vehicle):
    def __init__(self, gas, price, color, tires):
        super().__init__(price,gas,color)
        self.tires=tires

    def beep(self):
        print('honk honk')

tesla=car(100,'$45K','white',300 )
tesla.beep()