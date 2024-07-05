"""
Программа предназначена для выполнения основных операций с матрицами, таких как сложение, умножение и сравнение.
Она использует класс `Matrix`, чтобы создать две матрицы, наполняя их случайными числами. Аргуменнты для создания
матриц задаются вручную в основном модуле Main().
Журнал операций с результатами сохраняются в файл `matrix_operations.log`
Аргументы для запуска из командной строки:
- `--operation`: Указывает операцию для выполнения (`add` для сложения, `mul` для умножения, `eq` для сравнения).
- `--verbose`: Включает подробное логирование.

Для выполнения программы с командной строки:
```bash
python final_task_matrix.py --operation add --verbose
"""

import random
import logging
import argparse

# Настройка логирования
logging.basicConfig(filename='matrix_operations.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Matrix:
    @staticmethod
    def _same_size_and_type(matrix1, matrix2):
        """
        Проверяет, имеют ли две матрицы одинаковый размер и тип.
        """
        return isinstance(matrix2, Matrix) and matrix1.rows == matrix2.rows and matrix1.columns == matrix2.columns

    @staticmethod
    def _check_matrix(matrix: list[list[int]]) -> bool:
        """
        Проверяет, является ли матрица корректной (все строки одинаковой длины).
        """
        return len(set(map(len, matrix))) == 1

    def __init__(self, rows: int = 2, columns: int = 2, matrix: list[list[int]] = None):
        """
        Инициализирует матрицу с указанным количеством строк и столбцов.
        Если матрица не передана, создает матрицу с случайными значениями.
        """
        try:
            if matrix is None:
                if rows > 1 and columns > 1:
                    self.rows = rows
                    self.columns = columns
                    self.matrix = [[random.randint(0, 4) for _ in range(columns)] for _ in range(rows)]
                    logging.info(f'Создана матрица {rows}x{columns} с случайными значениями. {self.matrix}')

                else:
                    raise ValueError("Rows and columns must be greater than 1")

        except Exception as e:
            logging.error(f'Ошибка в инициализации матрицы: {e}')
            raise

    def __eq__(self, other):
        try:
            if Matrix._same_size_and_type(self, other):
                result = all(map(lambda el: el[0] == el[1], zip([col for row in self.matrix for col in row],
                                                                [col for row in other.matrix for col in row])))
                logging.info(f'Операция сравнения матриц выполнена. {result}')
                return result
            else:
                raise ValueError("Matrices are not the same size or type")
        except Exception as e:
            logging.error(f'Ошибка в операции сравнения матриц: {e}')
            raise

    def __add__(self, other):
        try:
            if Matrix._same_size_and_type(self, other):
                new_matrix = Matrix(matrix=[[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)]
                                            for i in range(self.rows)])
                logging.info(f'Операция сложения матриц выполнена = {self.matrix}')
                return new_matrix
            else:
                raise ValueError("Matrices are not the same size or type")
        except Exception as e:
            logging.error(f'Ошибка в операции сложения матриц: {e}')
            raise

    def __mul__(self, other):
        try:
            if isinstance(other, Matrix):
                new_matrix = [[0] * other.columns for _ in range(self.rows)]
                for i in range(self.rows):
                    for j in range(other.columns):
                        for k in range(other.rows):
                            new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                logging.info(f'Операция умножения матриц выполнена = {self.matrix}')
                return Matrix(matrix=new_matrix)
            elif isinstance(other, (int, float)):
                new_matrix = Matrix(
                    matrix=[[self.matrix[r][c] * other for c in range(self.columns)] for r in range(self.rows)])
                logging.info(f'Операция умножения матрицы на число выполнена = {self.matrix}')
                return new_matrix
            else:
                raise ValueError("Unsupported operand type(s) for multiplication")
        except Exception as e:
            logging.error(f'Ошибка в операции умножения: {e}')
            raise

    # def __str__(self):
    #     return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self.matrix) + '\n'


def main():
    """
    Основная функция для выполнения операций с матрицами на основе аргументов командной строки.
    """
    parser = argparse.ArgumentParser(description="Matrix operations script")
    parser.add_argument('--operation', type=str, choices=['add', 'mul', 'eq'], help='Operation to perform: add or mul or eq')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    matrix1 = Matrix(3,3)
    matrix2 = Matrix(3,3)
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)

        if args.operation == 'add':
            result = matrix1 + matrix2


        elif args.operation == 'mul':
            result = matrix1 * matrix2

        elif args.operation == 'eq':
            result = matrix1 == matrix2

        else:
            result = None


if __name__ == "__main__":
    main()
















