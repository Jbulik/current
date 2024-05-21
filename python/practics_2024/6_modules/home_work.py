'''Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
 На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
является ли введенная дата корректной или нет. Ваша программа должна предоставить ответ "True" (дата корректна)
 или "False" (дата некорректна) в зависимости от результата проверки.
Пример использования На входе:date_to_prove = 15.4.2023 На выходе: True
На входе: date_to_prove = 31.6.2022 На выходе: False
'''
import sys


# def leap_year(year: int) -> bool:
#     return bool(not year%4 and year%100 or not year%400)
#
#
# def check_date(user_date: list[str]) -> bool:
#     monthes = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     day, month, year = list(map(int, user_date))
#     if 0 < year <9999:
#         if month ==2:
#             # monthes[month-1][1] -> [month-1] = 2 -1 первый элемент в списке monthes = (28, 29), [1]=29
#             return bool(0 < day <= (monthes[month-1][1] if leap_year(year) else monthes[month-1][0]))
#         else:
#             if 0 < month < 13:
#                 return 0 < day <= monthes[month-1]
#
#
# print(check_date(input(list('Введите дату: ').replace('.', ''))))

# if __name__ == '__main__':
#     date = sys.argv[-1].split('.')
#     print(check_date(date))

# !!! Корректный вариант
def _is_leap(current_year: int) -> bool:
    return not current_year % 4 and current_year % 100 or not current_year % 400


def date_validate(user_date: str) -> bool:
    day, month, year = map(int, user_date.split('.'))
    _months = {i: 30 if i in (4, 6, 9, 11) else 31 for i in range(1, 13)}
    _months[2] = 29 if _is_leap(year) else 28

    if 0 < year < 10000 and month in _months and 0 < day <= _months[month]:
        return True
    return False


if __name__ == '__main__':
    print(date_validate('29.02.2024'))
    print(date_validate('29.02.2023'))
    print(date_validate('29.13.2024'))
    print(date_validate('29.02.20245'))



