'''Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
!!! Содержимое json файла. ЭТО <class 'dict'>
{
    "2": {
        "1": "grem",
        "2": "era",
        "4": "qwerty"
    },
    "1": {
        "3": "wwert",
        "8": "frod",
        "5": "rty"
    }
}
1) читаем джисон файл
'''

import os
import json
import csv
from typing import Iterator


def json_load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    return {}


# def convert_dict_to_list(json_data):
#     csv_data = []
#     for level, value in json_data.items():# level + словарь (внутри)
#         # json_data.items() -> лист ([
#         # ('2', {'1': 'grem', '2': 'era', '4': 'qwerty'}),
#         # ('1', {'3': 'wwert', '8': 'frod', '5': 'rty'})
#         # ])
#         for id, user_name in value.items(): #Проходит по каждому ключу `id` и значению `user_name`
#          # во вложенном словаре `value`
#          csv_data.append([level, id, user_name])
#     return csv_data #[['2', '1', 'grem'], ['2', '2', 'era'], ['2', '4', 'qwerty'], ['1', '3', 'wwert'],
#     # ['1', '8', 'frod'], ['1', '5', 'rty']]


def write_csv(file_name, csv_data):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel-tab')
        csv_write.writerows(csv_data)


def read_csv_dict(file_name):
    # json_data_dict = []
    with open(file_name, 'r', newline='') as f:
        csv_dict = csv.DictReader(f, dialect='excel-tab')
        for line in csv_dict:
            print(f'{line}')
        return csv_dict


def write_dict_csv(csv_dict, file_name):
    # Получаем заголовки столбцов из первого элемента словаря
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['lev', 'lev', 'lev'], dialect='excel-tab')
        csv_write.writeheader()  # Записываем заголовки
        csv_write.writerows(csv_dict)  # Записываем строки








# Пример использования:
# Загрузка данных из JSON файла
json_data = json_load('users.json')

# Чтение данных из CSV файла (для проверки)
read_csv_dict('users.json')

# Запись данных в CSV файл
write_dict_csv('output.csv', csv_dict)



# if __name__ == '__main__':
#     json_data = json_load('users.json')
#     json_data_dict = read_csv_dict('users.json')
#     # print(json_data)
#     write_dict_csv(json_data_dict)


    # csv_data = convert_dict_to_list(json_data)
    # write_csv("csv_text.csv", csv_data)




