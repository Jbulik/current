from itertools import chain, combinations
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

# cort = (1, 2, 'ss', 'rr', 4.5, 6.7, True, False)
# dct = {}
#
# for item in cort:
#     if type(item) in dct:
#         dct[type(item)].append(item)
#     else:
#         dct[type(item)] = [item]
#
# print(dct)


# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

# sample_list = [1, 2, 1, 1, 2]
#
# for item in set(sample_list):
#     if sample_list.count(item) == 2:
#         sample_list.remove(item)
#         sample_list.remove(item)
# print(sample_list)


# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔

# sample_list = [1, 2, 1, 1, 2, 4, 4]
#
# for i, item in enumerate(sample_list, 1):
#     if item % 2:
#         print(i, end=' ')

'''Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.'''
import string
from collections import Counter

# string = input("Введите текст: ").split()
# string = sorted(string)
# for i, item in enumerate(string, 1):
#     print(f'{i}. {item: >{len(max(string, key=len))}}')

'''✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.'''

# text = input("Введите текст: ")
#
# dict_text = dict()
#
# for char in text:
# if char in dict_text:
# dict_text[char] += 1
# else:
# dict_text[char] = 1
# print(dict_text)

# text = input("Введите текст: ")
#
# dict_text = dict()
#
# for char in text:
# dict_text[char] = dict_text.get(char, 0) + 1
# print(dict_text)

# text = input("Введите текст: ")
#
# dict_text = dict()
#
# for char in set(text):
#     dict_text[char] = text.count(char)
# print(dict_text)


'''На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.

Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
'''
# def fill_backpack(items, max_weight):
#     backpack = {}
#     total_weight = 0
#
#     # Сортируем предметы по их массе
#     sorted_items = sorted(items.items(), key=lambda x: x[1])
#
#     for item, weight in sorted_items:
#         # Проверяем, поместится ли предмет в рюкзак
#         if total_weight + weight <= max_weight:
#             backpack[item] = weight
#             total_weight += weight
#
#     return backpack
#
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
#
# backpack = fill_backpack(items, max_weight)
#  # Не выводим на экран, сохраняем результат в переменную backpack


# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# VAR 1
# lst = [1, 1, 2, 2, 3, 3, 4]
#
# double_list = [item for item in set(lst) if lst.count(item) > 1]
#
# print(double_list)
#
# # VAR 2
# duplicates = set()
#
# for item in lst:
#     if lst.count(item) >= 2:
#         duplicates.add(item)
#
# result = list(duplicates)
# print(result)


'''В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.'''

# text = 'Hello world. hello Python. Hello python again.'
#
# # Удаление знаков препинания
# # создание таблицы перевода символов
# table = text.maketrans("", "", string.punctuation)
#
# # применение таблицы к строке
# sample_text = (text.translate(table)).lower().split()
#
# popular_words = Counter(sample_text).most_common(3)
# print(popular_words)

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
# max_weight = 1.0
# total_summ = 0
# pack = []
# for name, weght in items.items():
#     if total_summ + weght <= max_weight:
#         total_summ += weght
#         pack.append(name)
# pack.append(total_summ)
#
# print(pack)

# вариант 2. Комбинации. Составляет все возможные комбинации наполнения


# def powerset(invetory: list[str]):
#     return chain.from_iterable(combinations(invetory, r) for r in range(1, len(invetory) + 1))
#
#
# def all_optuons(inventory: dict[str, float], capacity: int):
#     result = []
#     for cur_option in powerset(list(inventory)):
#         weght = 0
#         for item in cur_option:
#             weght += inventory.get(item)
#         if (capacity - min(inventory.values())) <= weght <= capacity:
#             result.append((cur_option, weght))
#     return result
#
#
# for option in all_optuons(items, 10):
#     print(option)


