'''ЧАСТЬ 3
� Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение.'''
_riddle_statistic = {}


def logging(riddle_text, attempt):
    if riddle_text in _riddle_statistic:
        _riddle_statistic[riddle_text].append(attempt)
    else:
        _riddle_statistic[riddle_text] = [attempt]

def log_wiew():
    for ridlle_text, attempt in _riddle_statistic.items():
        #проходим по списку с попытками
        for item in attempt:
            print(f'Загадка {ridlle_text} отгадана с попытки {attempt}')



