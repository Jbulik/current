# from random import randint
# from random import uniform
# print(rnd.random())
# rnd.seed(42)
# state = rnd.getstate()
# print(rnd.random())
# rnd.setstate(state)
# print(rnd.random())

'''� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.'''

'''2 ЧАСТЬ
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.'''

import kazino

kazino.number_generator(1, 15, 3)




