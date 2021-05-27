class Road:
    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, weight: int, thickness: int):
        mass = self._length * self._width * weight//1000 * thickness
        print(mass)


a = Road(20, 5000)
a.mass_of_asphalt(25,5)
