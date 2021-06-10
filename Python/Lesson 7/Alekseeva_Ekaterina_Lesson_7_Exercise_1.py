# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix_data = list_of_lists
        self.rows = len(list_of_lists)
        self.columns = len(list_of_lists[0])

    def __str__(self):
        result_string = ""
        for row in self.matrix_data:
            for column in row:
                result_string += "{:>10}".format(str(column))
            result_string += "\n"
        return result_string

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Складывать можно только матрицы одинакового размера")

        new_matrix_data = list()
        for i in range(0, len(self.matrix_data)):
            new_matrix_data.append(list())
            for j in range(0, len(self.matrix_data[i])):
                new_matrix_data[i].append(self.matrix_data[i][j] + other.matrix_data[i][j])
        return Matrix(new_matrix_data)



m1 = Matrix([[1, 1, 2], [1, 2, 1], [2, 1, 1]])
print(f"Матрица 1:\n{m1}\n\n")
m2 = Matrix([[4, 2, 4], [4, 5, 3], [5, 4, 4]])
print(f"Матрица 2:\n{m2}\n\n")
print(f"Матрица 1 + Матрица 2:\n{m1 + m2}\n\n")