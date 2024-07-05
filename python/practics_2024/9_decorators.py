'''Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.'''
import json
import os
from random import randint

# def zagadayka(a: int, b: int):
#     number = randint(1, a)
#     count = b
#     def game():
#         nonlocal number, count
#         for i in range(count):
#             a = int(input('Введите число от 1 до 100:'))
#             if a == number:
#                 print('Вы угадали')
#                 return i + 1
#             elif a < number:
#                 print('Загаданное число больше.')
#             else:
#                 print('Загаданное число меньше.')
#             return False
#         return game
#
#
# start_game = zagadayka(100, 10)
# start_game()


'''Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюу гадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.'''


# def game_decorator(func):
#     def wrapper(func_number, func_count):
#         if not (100 >= func_number >= 1):
#             func_number = randint(1,100)
#         if not (10 >= func_count >= 1):
#             func_count = randint(1, 10)
#         func(func_number, func_count)
#     return wrapper # Вернуть функцию-обёртку
#
# @game_decorator
# def game(number, count):
#     print(number)
#     print(count)
#
#     for i in range(count):
#         a = int(input('Введите число от 1 до 100:'))
#         if a == number:
#             print('Вы угадали')
#             return i + 1
#         elif a < number:
#             print('Загаданное число больше.')
#         else:
#             print('Загаданное число меньше.')
#
#
# game(0, 105)


'''Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
Этот код включает декоратор, который логирует вызовы функции в JSON-файл. Декоратор сохра
няет переданные аргументы и результаты вызова функции, и если файл с логами уже существует,
он обновляет его новыми данными.'''


# def some_decorator(func):
#     # Определяем функцию-обёртку wrapper, которая принимает
#     # произвольное количество позиционных и ключевых аргументов
#     def wrapper(*args, **kwargs):
#         # Вызываем оригинальную функцию с переданными аргументами и сохраняем результат
#         result = func(*args, **kwargs)
#         # Создаем имя файла, используя имя оригинальной функции и расширение .json
#         file_name = f'{func.__name__}.json'
#         # Инициализируем пустой словарь для хранения данных
#         data_json = {}
#         if os.path.exists(file_name):
#             # Если файл существует, открываем его в режиме чтения
#             with open(file_name, 'r') as f:
#                 # Загружаем данные из файла в словарь data_json
#                 #После выполнения `json.load(f)`, результат (объект Python, соответствующий JSON данным)
#                 #после этого с данными из файла джисон можно работать в коде
#                 data_json = json.load(f)
#                 # Добавляем результат вызова функции в словарь data_json,
#                 # используя результат (сумму "return sum(args)"  как ключ
#                 # и аргументы функции как значение
#         data_json[result] = {'args':args, **kwargs}
#
#         with open(file_name, 'w') as f:
#             json.dump(data_json, f)
#     return wrapper
#
# @some_decorator
# def func(*args, **kwargs):
#     print(args, kwargs)
#     return sum(args)
#
# func(1, 4, 3, 5, j=4, i=7, h=8)

'''Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
Декоратор запускает функцию  func count раз + kwargs['k'] += 1 + result.append'''

# def count(number):
#     def some_decorator(func):
#         result = []
#         def wrapper(*args, **kwargs):
#             for i in range(number):
#                 kwargs['k'] += 1
#                 result.append(func(*args, **kwargs))
#             return result
#         return wrapper
#     return some_decorator
#
# @count(5)
# def func(*args, **kwargs):
#     print(args, kwargs)
#     return sum(args)
#
# print(func(1, 4, 3, j=4, k=7))

'''Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
Запускаем ф-цию с запредельными значениями для контроля
снизу вверх: check значения ->сохранение значений ->  многократный запуск 
результат - число, ноль - если неугаданно, колич-во попыток - кортеж''
! в джисон в качестве ключа можно передать только строку'''


# Декоратор для записи результатов функции в JSON файл
def write_json(func):
    def wrapper(*args, **kwargs):
        # Выполняем декорируемую функцию и получаем результат
        result = func(*args, **kwargs)

        # Имя файла будет совпадать с именем функции и иметь расширение .json
        file_name = f'{func.__name__}.json'

        # Инициализируем пустой словарь для хранения данных
        data_json = {}

        # Если файл уже существует, загружаем данные из него
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data_json = json.load(f)

        # Добавляем новый результат в словарь
        data_json[result] = {'args': args, **kwargs}

        # Записываем обновленный словарь обратно в файл
        with open(file_name, 'w') as f:
            json.dump(data_json, f)

        return result

    return wrapper


# Декоратор, который позволяет вызывать функцию несколько раз и сохранять результаты
def count(number):
    def some_decorator(func):
        result = []

        def wrapper(*args, **kwargs):
            for i in range(number):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return some_decorator
#- Возвращает список результатов выполнения декорируемой функции `func`,
#  вызванной `number` раз.


# Декоратор для игры, проверяющий и корректирующий входные параметры
def game_decorator(func):
    def wrapper(func_number, func_count):
        # Если число вне диапазона 1-100, то выбираем случайное число
        if not (100 >= func_number >= 1):
            func_number = randint(1, 100)

        # Если количество попыток вне диапазона 1-10, то выбираем случайное число
        if not (10 >= func_count >= 1):
            func_count = randint(1, 10)

        return func(func_number, func_count)

    return wrapper


@count(3)
@write_json
@game_decorator
def game(number, count):
    for i in range(count):
        a = int(input('Введите число от 1 до 100: '))
        if a == number:
            print('Вы угадали')
            return f'{number}, {i + 1}'
        elif a < number:
            print('Загаданное число больше.')
        else:
            print('Загаданное число меньше.')
    print(f'Вы не угадали, загаданноечисло было: {number}')
    # если пользователь не угадал число за заданное количество попыток, функция
    # возвращает строку, содержащую загаданное число и 0, что указывает на то,
    # что пользователь не сделал ни одной успешной попытки.
    return f'{number}, {0}'


@count(5)
def func(*args, **kwargs):
    print(args, kwargs)
    return sum(args)


# Пример вызова функции game
print(game(105, 26))

