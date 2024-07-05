'''✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.'''


from random import randint, uniform
#
# MIN_LIMIT= -1000
# MAX_LIMIT= 1000
#
# def fill_file(count_lines, file_name):
#      with open(file_name, 'a', encoding='utf-8') as f:
#         for _ in range(count_lines):
#             int_num = randint(MIN_LIMIT, MAX_LIMIT)
#             float_num = uniform(MIN_LIMIT, MAX_LIMIT)
#             f.write(f'{int_num} | {float_num}\n')
#
# fill_file(10, 'sample.txt')


'''Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.'''

from string import ascii_lowercase
from random import choice

# MIN_LEN = 4
# MAX_LEN = 7
# # VOWELS = 'aeiou'
# # CONSONANT = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower()
# rus_alpha = {chr(i) for i in range(ord('а'), ord('я') + 1)} #range  итератор -> set {}
# #{'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
# VOWELS = ''.join({'а', 'у', 'е', 'ё', 'о', 'э', 'я', 'и', 'ю'})# сделали строку из множества с гласными
# CONSONANT = ''.join(rus_alpha.difference(VOWELS)) # вывели разницу между алфавитом и гласными
#
#
# def random_name():
#     name = ''
#     for position in range(randint(MIN_LEN, MAX_LEN)):
#         if position % 2:
#             name += choice(VOWELS)
#         else:
#             name += choice(CONSONANT)
#     return name.capitalize()
#
#
# def fill_file(count, file_name):
#     with open(file_name, 'w', encoding='utf-8') as f:
#         for _ in range(count):
#             f.write(random_name() + '\n')
#
# fill_file(10, 'names.txt')

'''✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.'''

# def read_file(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         return list(map(lambda x: x.strip(), f.readlines()))
#
#
# def write_file(names, numbers, file_name):
#     max_len = len(max(names, numbers, key=len))
#     with open(file_name, 'w', encoding='utf-8') as f:
#         for i in range(max_len):
#             num1, num2 = map(float, numbers[i % len(numbers)].split('|'))
#             if (multiple:= num1 * num2) < 0:
#                 f.write(f'{names[i % len(names)].lower()} | {abs(multiple)}\n')
#             else:
#                 f.write(f'{names[i % len(names)].upper()} | {int(multiple)}\n')
#
#
# names = read_file('names.txt')
# numbers = read_file('sample.txt')
#
# write_file(names, numbers, 'multiple_file.txt')


'''✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
папку для файлов нужно создать предварительно'''
# from string import ascii_lowercase
# from random import choice
# from random import randbytes, randint
#
# rus_alpha = {chr(i) for i in range(ord('а'), ord('я') + 1)}
# VOWELS = ''.join({'а', 'у', 'е', 'ё', 'о', 'э', 'я', 'и', 'ю'})# сделали строку из множества с гласными
# CONSONANT = ''.join(rus_alpha.difference(VOWELS)) # вывели разницу между алфавитом и гласными
#
#
# # def create_file(extension, min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42 ):
# #     for _ in range(file_count):
# #         with open(f'test_dir/{random_name(min_len, max_len)}.{extension}', 'wb') as f:
# #             f.write(randbytes(randint(min_size, max_size)))
#
#
# def random_name(min_len, max_len):
#     name = ''
#     for position in range(randint(min_len, max_len)):
#         if position % 2:
#             name += choice(VOWELS)
#         else:
#             name += choice(CONSONANT)
#     return 'test_file'
#
#
# # create_file('txt')
#
# '''✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.'''
#
# def create_group_files(group_ext):
#     for key, value in group_ext.items():
#         create_file(key, file_count=value)
#
#
# # group_ext = {'txt': 3, 'jpg': 2, 'md': 4}
# #
# # create_group_files(group_ext)
#
# '''✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.'''
# from random import choice
# from random import randbytes, randint
# from pathlib import Path
# import os
#
#
# #добавим входной параметр для папки
# def create_file(extension, path="test_dir", min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42 ):
#     for i in range(file_count):
#         file_name = os.path.join(path, random_name(min_len, max_len)) + '.' + extension
#         if os.path.exists(file_name):
#             #если имена файла совпадают дописываем в имя вновь создаваемого '_' число из обхода цикла
#                 file_name = os.path.join(path, random_name(min_len, max_len) + str(i)) + '.' + extension
#         with open(file_name, 'wb') as f:
#             f.write(randbytes(randint(min_size, max_size)))
#
#
# def create_group_files_path(group_ext):
#     for key, value in group_ext.items():
#         create_file(key, file_count=value)
#
#
# def path_exist(path):
#     if not os.path.exists(path):
#         Path(path).mkdir()
#
#
# # create_file()
# group_ext = {'txt': 3, 'jpg': 2, 'md': 4}
#
# create_group_files(group_ext)

