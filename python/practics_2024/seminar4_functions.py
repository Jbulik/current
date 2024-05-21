'''✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.'''

# import string
# text = 'Hello world. hello Python. Hello python again.'
#
#
# def text_func(text: str):
#     # Удаление знаков препинания
#     # создание таблицы перевода символов
#     table = text.maketrans("", "", string.punctuation)
#
#     # применение таблицы к строке
#     sample_text = (text.translate(table)).lower().split()
#     for i, item in enumerate(sample_text, 1):
#         print(f'{i}. {item: >{len(max(sample_text, key=len))}}')


# text_func(text)

#ВАРИАНТ 2

# def sort_text(text: str):
#     text = sorted(text.split())
#     for i, item in enumerate(text, 1):
#         print(f'{i}. {item: >{len(max(text, key=len))}}')
#
#
# sort_text(input('Введите текст: '))


# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def text_list(text: str):
#     res = set()
#     for i in text:
#         res.add(ord(i))
#     return sorted(res, reverse=True)
#
#
# in_text = input("Введите текст: ")
#
# print(text_list(in_text))
#вариант №2
# def text_list(text: str):
#     return sorted([ord(i) for i in set(text)], reverse=True)
#
#
# in_text = input("Введите текст: ")
# print(text_list(in_text))

'''✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''


# def dict_from_text(numbers):
#     a, b = sorted(list(map(int, numbers.split())))
#     return {chr(i): i for i in range(a, b + 1)}
#
# print(dict_from_text('130 115'))


'''✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.'''
# def mysort(lst, reverse=False):
#     for j in range(len(lst)):
#         for i in range(len(lst) - j - 1):
#             if reverse:
#                 if lst[i] < lst[i + 1]:
#                     lst[i], lst[i + 1] = lst[i + 1], lst[i]
#             else:
#                 if lst[i] > lst[i + 1]:
#                     lst[i], lst[i + 1] = lst[i + 1], lst[i]
#
# lst = [4, 7, 2, 6, 3]
#
# mysort(lst, reverse=True)
# print(lst)
'''✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии
'''
# def dict_salary(name, salary, bonus):
# # my_dict = {}
# # for i in range(len(name)):
# # my_dict[name[i]] = salary[i] * float(bonus[i].replace('%', '')) / 100
# # return my_dict
#     return {name[i]: salary[i] * float(bonus[i][:-1]) / 100 for i in range(len(name))}
#
#
# my_name = ["Иван", "Владимир", "Сергей"]
# my_salar = [1000, 2000, 3000]
# my_bonus = ["10%", "12.2%", "11%"]
# print(dict_salary(my_name, my_salar, my_bonus))

'''✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.'''


# def sum_slice(int_list: list[int], a_index: int, b_index: int) -> int:
#     a_index, b_index = sorted([a_index, b_index])
#     if a_index < 0:
#         a_index = 0
#     if b_index < 0:
#         b_index = 1
#     return sum(int_list[a_index:b_index + 1])
#
#
# print(sum_slice([1, 2, 3, 4, 5, 6], 2, 3))
'''✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.'''


# def is_profit(dct_companies: dict) -> bool:
#     for profit in dct_companies.values():
#          if sum(profit) < 0:
#              return False
#     return True
#
# dct_companies = {
#     'Abibas': [1234, -456, 2345, 1000, 800],
#     'Nuke': [-3000, 5600, 8000],
#     'Ribok': [5000, -2300, -4000, 9000]
# }

# print(is_profit(dct_companies))

'''✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.'''

# names = ['stone', 'wanderer']
# ages = [18, 34, 40]
# sample = 'Пример'
# s = 417
# apple = 'Яблоко'
#
#
# def change_name():
# new_vars = {}
# for var_name, var_value in globals().items():
# if var_name.endswith('s') and len(var_name) > 1:
# new_vars[var_name[:-1]] = var_value
# new_vars[var_name] = None
# else:
# new_vars[var_name] = var_value
# globals().update(new_vars)
#
#
# change_name()
#
# print(name)
# print(age)
# print(names)
# print(ages)
# print(sample)
# print(s)

'''Homework
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает транспонированную матрицу.

Пример использования На входе:
matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]
transposed_matrix = transpose(matrix)
На выходе:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]'''
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
# def transposed_matrix(matrix):
#     temp_matrix = []
#     for i in range(len(matrix[0])): #внешний цикл. Идем по индексам списка - кол-во списков в списке.
#         temp_matrix.append([])  #добавляем пустой список символы скобок для наполнения i=0
#         for j in range(len(matrix)):  #берем первый эл-т в первой  матрице j=0 далее 1-ый эл из второй...
#             temp_matrix[i].append(matrix[j][i])  #внутренний цикл наполняем в i список первые эл-ты из каждого листа
#     return temp_matrix
#
# print(transposed_matrix(matrix))

# Вариант 2

# def transpose(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
#
#     return transposed

# print(transpose(matrix))

# ''' ВАРИАНТ №3
# zip берёт, и составляет кортежи последовательно из элементов каждого аргумента.
# Первый возвращённый кортеж будет состоять из первых элементов переданных списков,
#  второй кортеж будет состоять из вторых элементов аргументов,
#   И так, пока элементы в аргументах не закончатся.'''
# # def transpose(matrix):
# #     return list(zip(*matrix))
#
# print(transpose(matrix))

'''Преобразование ключей и значений словаря

Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
Пример использования.
На входе:
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
На выходе: {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
'''
# def inverse_items(**kwargs): # step1 -> {'a': 1, 'b': 'hello', 'c': [1, 2, 3], 'd': {}}
#     new_dict = {}
#     for key, value in kwargs.items():# берем ключ и значение из словаря-список кортежей после items
#         try:
#             new_dict[value] = key
#         except:
#             new_dict[str(value)] = key
#     return new_dict
#
#  params = inverse_items(a=1, b='hello', c=[1, 2, 3], d={})
#
# def isinstance_items(**kwargs): # step1 -> {'a': 1, 'b': 'hello', 'c': [1, 2, 3], 'd': {}}
#     new_dict = {}
#     for key, value in kwargs.items():# берем ключ и значение из словаря-список кортежей после items
#         if not isinstance(value, list | set | dict):
#             new_dict[str(value)] = key
#         else:
#             new_dict[str(value)] = key
#     return new_dict
#
#
#
# params = isinstance_items(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)






