class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int = 0, bonus: int = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

    fullname = property(fget=get_full_name)
    salary = property(fget=get_total_income)


if __name__ == '__main__':
    data_base = [
        {
            'name': 'Egor',
            'surname': 'Velosipedov',
            'position': 'data engineer',
            'wage': 250000,
            'bonus': 150000

        },
        {
            'name': 'Artem',
            'surname': 'Punksov',
            'position': 'network engineer',
            'wage': 187000,
            'bonus': 74599

        },
        {
            'name': 'Mihail',
            'surname': 'Zuev',
            'position': 'Big boss',
            'wage': 567899,
            'bonus': 7134

        }
    ]
    for item in data_base:
        worker = Position(**item)
        print('-' * 50)
        print(f'This is the data: {item}')
        print(f'Worker name: {worker.name}')
        print(f'Worker surname: {worker.surname}')
        print(f'Worker full name: {worker.fullname}')
        print(f'Worker position: {worker.position}')
        print(f'Worker salary: {worker.salary}')
        print('-' * 50)