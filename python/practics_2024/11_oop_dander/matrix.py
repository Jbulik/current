'''
### Разбиение на части

1. **Список элементов первой матрицы:**

    ```python
    [col for row in self.matrix for col in row]    ```

    Это list comprehension, который разворачивает матрицу `self.matrix` в одномерный список.

    - `self.matrix` — это, предположительно, двумерный список (матрица).
    - Внешний цикл `for row in self.matrix` проходит по строкам матрицы.
    - Внутренний цикл `for col in row` проходит по элементам каждой строки.
    - `col` добавляется к результирующему списку.

    Например, если `self.matrix = [[1, 2], [3, 4]]`, то результатом будет `[1, 2, 3, 4]`.

2. **Список элементов второй матрицы:**

    ```python
    [col for row in other.matrix for col in row]
    ```

    Аналогично первому списку, это разворачивает матрицу `other.matrix` в одномерный список.

    Например, если `other.matrix = [[1, 2], [3, 4]]`, то результатом будет `[1, 2, 3, 4]`.

3. **zip двух списков:**

    ```python
    zip([col for row in self.matrix for col in row],
        [col for row in other.matrix for col in row])
    ```

    Функция `zip` берёт два списка и объединяет их в последовательность кортежей, где каждый кортеж состоит из элементов, стоящих на одинаковых позициях в исходных списках.

    Например, если у нас есть списки `[1, 2, 3, 4]` и `[1, 2, 3, 4]`, то результатом будет `[(1, 1), (2, 2), (3, 3), (4, 4)]`.

4. **Функция `map` с лямбда-выражением:**

    ```python
    map(lambda el: el[0] == el[1], zip([...], [...]))
    ```

    Функция `map` применяет лямбда-выражение ко всем элементам, полученным из `zip`. Лямбда-выражение `lambda el: el[0] == el[1]` проверяет, равны ли первый и второй элементы в каждом кортеже.
'''



import random


class Matrix:

    def __init__(self, rows: int = 2, columns: int = 2, matrix: list[list[int]] = None):
        if matrix is None:
            if rows > 1 and columns > 1:
                self.rows = rows
                self.columns = columns
                self.matrix = [[random.randint(0, 4) for _ in range(columns)] for _ in range(rows)]
            else:
                raise ValueError
        else:
            if Matrix._check_matrix(matrix):
                self.rows = len(matrix) #кол-во строк/Верхний уровень
                self.columns = len(matrix[0]) #кол-во столбцов
                self.matrix = matrix
            else:
                raise ValueError


    def __eq__(self, other):
        #сравнили дл и шир
        #проверяет, что `other` является экземпляром класса `Matrix`. Это важно, потому что операции сравнения
        # матриц имеют смысл только тогда, когда `other` тоже является матрицей
        if Matrix._same_size_and_type(self, other):
            #ВАРИАНТ 1
            # return all([all([self.matrix[r][c] == other.matrix[r][c]
            #                  for c in range(self.columns)]) for r in range(self.rows)])

            # ВАРИАНТ 2
            return all(map(lambda el: el[0] == el[1], zip([col for row in self.matrix for col in row],
                                                          [col for row in other.matrix for col in row])))

    def __add__(self, other):
        if Matrix._same_size_and_type(self, other):
            return Matrix(matrix=[[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)]
                                  for i in range(self.rows)])
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            new_matrix = [[0] * other.columns for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in  range(other.rows):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(matrix=new_matrix)

        elif isinstance(other, int | float):
            return Matrix(matrix=[[self.matrix[r][c] * other
                                   for c in range(self.columns)] for r in range(self.rows)])
        else:
            raise ValueError












    @staticmethod
    # сравнили дл и шир
    # проверяет, что `other` является экземпляром класса `Matrix`. Это важно, потому что операции сравнения
    # матриц имеют смысл только тогда, когда `other` тоже является матрицей
    def _same_size_and_type(matrix1, matrix2):
        return isinstance(matrix2, Matrix) and matrix1.rows == matrix2.rows and matrix1.columns == matrix2.columns


    @staticmethod
    def _check_matrix(matrix:list[list[int]]) -> bool:
        # все длины строк д/б одинаковыми
        return len(set(map(len, matrix))) == 1


    def __str__(self):
        # 1-ый пробел для разделения строк, последний для расстояния м/д матриц
        # Спецификатор `:^5` означает, что элемент `x` будет выровнен по центру в поле шириной 5 символов.
        # Например, число `7` будет отображено как `'  7  '`, а число `123` как `' 123 '`.
        # Это создаёт равномерное расстояние между элементами, делая матрицу визуально приятной.
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self.matrix) + '\n'


my_matrix1 = Matrix(3, 3)
my_matrix2 = Matrix(3, 3)

print(my_matrix1)
print(my_matrix2)
print(my_matrix2 + my_matrix1)
print(my_matrix2 == my_matrix1)
print(my_matrix2 * my_matrix1)

















