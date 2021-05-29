class Car:
    def __init__(self, name: str, color: str, speed=0, is_police: bool = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'{self.name} поехал')
        else:
            print(f'{self.name} стоит')

    def stop(self):
        if self.speed > 0:
            self.speed = 0
            print(f'{self.name} остановился')

    def turn(self, direction=None):
        if self.speed > 0:
            if direction == None:
                print(f'{self.name} едет прямо')
            else:
                print(f'{self.name} повернул {direction}')
        else:
            print(f'{self.name} стоит на месте и не может повернуть')

    def show_speed(self):
        if self.speed > 0:
            print(f'текущая скорость {self.speed} км/ч')
            if hasattr(self, '_max_speed') and self.speed > self._max_speed:
                print(f'ПРЕВЫШЕНИЕ СКОРОСТИ на {self.speed - self._max_speed} км/ч!')


class TownCar(Car):
    _max_speed = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    _max_speed = 40


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    car_list = [
        {
            'name': 'zaz',
            'color': 'green'
        },
        {
            'name': 'Ferrari',
            'color': 'yellow',
            'speed': 200
        },
        {
            'name': 'Lada',
            'color': 'yellow',
            'speed': 110
        },
        {
            'name': 'Jeep',
            'color': 'blue',
            'speed': 50
        },
        {
            'name': 'toyota',
            'color': 'black',
            'speed': 12,
            'is_police': True}
    ]
    class_list = [Car, SportCar, WorkCar, TownCar, PoliceCar]
    for i, k in zip(car_list, class_list):
        car = k(**i)
        print('-' * 50)
        print(type(car))
        print('Это данные: ', i)
        print('Это атрибуты класса: ', car.__dict__)
        car.go()
        car.turn()
        car.turn('направо')
        car.show_speed()
        car.stop()
        print('-' * 50)
car = Car()
a = Car ()