from time import sleep


class TrafficLight:
    _color = {'red': 7, 'yellow': 2, 'green': 3}

    def running(self):
        # time_sleep = [7, 2, 1]
        for color, time_sleep in self._color.items():
            return f'{color}'
            sleep(time_sleep)


a = TrafficLight()
print(a.running())
