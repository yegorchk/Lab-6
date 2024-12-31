class Gun:
    className = 'Gun'
    objectsCount = 0

    def __init__(self, name, number_of_rounds, fire_rate, range):
        self._name = name
        self._number_of_rounds = number_of_rounds
        self._fire_rate = fire_rate
        self._range = range
        Gun.objectsCount = Gun.objectsCount + 1

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_number_of_rounds(self):
        return self._number_of_rounds
    
    def set_number_of_rounds(self, number):
        if number > 0:
            self._number_of_rounds = number
        else:
            self._number_of_rounds = 1

    def get_fire_rate(self):
        return self._fire_rate
    
    def set_fire_rate(self, fr):
        if fr > 0:
            self._fire_rate = fr
        else:
            self._fire_rate = 1

    def get_range(self):
        return self._range
    
    def set_range(self, range):
        if range > 0:
            self._range = range
        else:
            self._range = 0.1

    def info (self):
        print(f'The number of rounds in a store is {self._number_of_rounds}')
        print(f'The fire rate is {self._fire_rate} rpm')
        print(f'The range is {self._range} meters')

    def time_to_get_empty(self):
        print(f'Time for store to get empty is {self._number_of_rounds/(self._fire_rate/60)}')

    def fire_rate2range (self):
        return self._fire_rate/self._range


class SniperRifle(Gun):
    className = 'SniperRifle'

    def __init__(self, name, number_of_rounds, fire_rate, range):
        super().__init__(name, number_of_rounds, fire_rate, range)

class AssaultRifle(Gun):
    className = 'AssaultRifle'

    def __init__(self, name, number_of_rounds, fire_rate, range):
        super().__init__(name, number_of_rounds, fire_rate, range)

sr = SniperRifle('m24', 5, 20, 1500)
ar = AssaultRifle('m16', 30, 800, 550)

print(sr.fire_rate2range())
print(ar.fire_rate2range())

sr.time_to_get_empty()
ar.time_to_get_empty()



    
