class Matrix:
    def __init__(self, matrix_data: list[list]):
        self.matrix = matrix_data
        self.size_matrix = len(self.matrix)
        self.size_row_matrix = frozenset(len(row) for row in self.matrix)
        if len(self.size_row_matrix) != 1:
            raise ValueError('ряды матрицы разного размера')

    def __add__(self, other):
        if self.size_matrix == other.size_matrix:
            if self.size_row_matrix == other.size_row_matrix:
                result = []
                for item in zip(self.matrix, other.matrix):
                    result.append([sum([i, k]) for i, k in zip(*item)])
                return Matrix(result)
            else:
                raise ValueError('складываемые матрицы имеют разный размер рядов')
        else:
            raise ValueError('складываемые матрицы имеют разный размер')

    def __str__(self):
        return '\n'.join(['  '.join(map(str, row)) for row in self.matrix])




a = [[1, 2, 3], [9, 9, 10]]
b = [[9, 8, 8], [9, 9, 9]]
m1 = Matrix(a)
m2 = Matrix(b)
print(m1 + m2)
