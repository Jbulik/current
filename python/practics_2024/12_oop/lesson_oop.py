# from collections import defaultdict
#
#
# # Класс Storage для хранения объектов по их типам
# class Storage:
#     # Инициализация при создании объекта класса
#     def __init__(self):
#         # Создание словаря, где ключи - это типы объектов, а значения - списки объектов этого типа
#         self.storage = defaultdict(list)
#
#     # Метод для строкового представления объекта класса
#     def __str__(self):
#         # Формирование строки с перечислением всех объектов, сгруппированных по их типам
#         txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
#         return f'Объекты хранилища по типам:\n{txt}'
#
#     # Метод, позволяющий вызывать объект класса как функцию
#     def __call__(self, value):
#         # Добавление объекта в список, соответствующий его типу
#         self.storage[type(value)].append(value)
#         return f'К типу {type(value)} добавлен {value}'
#
#
# # Создание объекта класса Storage
# s = Storage()
#
# # Добавление различных объектов и вывод результата
# print(s(42))  # Добавление целого числа 42
# print(s(72))  # Добавление целого числа 72
# print(s('Hello world!'))  # Добавление строки 'Hello world!'
# print(s(0))  # Добавление целого числа 0
#
# # Вывод содержимого хранилища
# print(s)

import sqlite3
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()
cursor.execute("""create table if not exists users(name,
age);""")
cursor.execute("""insert into users values ('Гвидо', 66);""")
connection.commit()
connection.close()