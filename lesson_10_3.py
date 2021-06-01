class Cell:
    def __init__(self, quantity: int):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self) -> str:
        return f"Клетка состоит из {self.quantity} ячеек"

    def make_order(self, cell_in_row: int) -> str:
        row = self.quantity // cell_in_row
        remainder_cell_in_row = self.quantity % cell_in_row
        return '\n'.join(['*' * cell_in_row] * row + (['*' * remainder_cell_in_row]))


cells1 = Cell(19)
cells2 = Cell(23)
print(cells1)
print(cells2, '\n')
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2 / cells1, '\n')
print(cells2.make_order(7), '\n')
print(cells1.make_order(10))
