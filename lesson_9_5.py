class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen:
    def draw(self):
        print('Запуск письма')


class Pencil:
    def draw(self):
        print('Запуск штриховки')


class Handle:
    def draw(self):
        print('Запуск выделения')


if __name__ == '__main__':
    class_list = [Stationery, Pen, Pencil, Handle]
    for i in class_list:
        stationery = i()
        print('-' * 50)
        stationery.draw()
        print('-' * 50)
