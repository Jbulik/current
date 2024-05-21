''' ✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
хранятся в кортеже как значения второго ключа.'''
# sample_string = input("Введите строку через '/': ").split('/')
#
# val_1, key_1, key_2, *val_2 = map(int, sample_string)
#
# print(res_dict := {key_1: val_1, key_2: val_2})

# str_dict = input("Введите строку через '/': ")
# dict_cur = str_dict.split('/')
# dict_res = {}
# dict_res[dict_cur[1]] = dict_cur[0]
# dict_res[dict_cur[2]] = dict_cur[3:]
# print(dict_res)
'''✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.'''
# sample_str = "Always be happy"
#
# print(res_dict := {i: ord(i) for i in sample_str if i.isalpha()})

# print({i: ord(i) for i in set(input('Введите строку: ').replace(' ', ''))})

'''✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение'''
# fizz_buzz = ('FizzBuzz' if not i % 3 and not i % 5 else ('Fizz' if not i % 3 else ('Buzz' if not i % 5 else i)) for i in
# range(1, 101))

# print(*fizz_buzz)

# for i in range(100):
#     if not (i % 3) and not (i % 5):
#         print('FizzBuzz')
#     elif not (i % 3):
#         print('Fizz')
#     elif not (i % 5):
#         print('Buzz')
#     else:
#         print(i)

'''✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''
# def simple_numbers(count: int):
#     yield 2
#     cur_number = 3
#     counter = 1
#     while counter < count:
#         for dev in range(3, int(cur_number ** 0.5) + 1, 2):
#             if not cur_number % dev:
#                 break
#         else:
#             yield cur_number
#             counter += 1
#         cur_number += 2
#
#
# for i in simple_numbers(5):
#     print(i)


# def gen_numbers(count_chain: int):
#     for i in range(count_chain):
#         curr_num = i
#         yield curr_num
#         curr_num += 1
#
#
# print(*gen_numbers(4))




