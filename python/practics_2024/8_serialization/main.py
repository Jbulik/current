# import json
#
# json_text = """
# [
# {
# "userId": 1,
# 6
# "id": 9,
# "title": "nesciunt iure omnis dolorem tempora et
# accusantium",
# "body": "consectetur animi nesciunt iure dolore"
# },
# {
# "userId": 1,
# "id": 10,
# "title": "optio molestias id quia eum",
# "body": "quo et expedita modi cum officia vel magni"
# },
# {
# "userId": 2,
# "id": 11,
# "title": "et ea vero quia laudantium autem",
# "body": "delectus reiciendis molestiae occaecati non minima
# eveniet qui voluptatibus"
# },
# {
# "userId": 2,
# "id": 12,
# "title": "in quibusdam tempore odit est dolorem",
# "body": "praesentium quia et ea odit et ea voluptas et"
# }
# ]"""
#
# #
# # print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)

# import json

# my_dict = {
# "first_name": "Джон",
# "last_name": "Смит",
# "hobbies": ["кузнечное дело", "программирование",
# "путешествия"],
# "age": 35,
# "children": [
# {
# "first_name": "Алиса",
# "age": 5
# },
# {
# "first_name": "Маруся",
# "age": 3
# }
# ]
# }
# # print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f:
#     # json.dump(my_dict, f)
#       json.dump(my_dict, f, ensure_ascii=False)
#
# # with open('new_user.json', 'r', encoding='utf-8') as f:
# #     new_dict = json.load(f)
# # print(f'{new_dict = }')

# dict_to_json_text = json.dumps(my_dict)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# res = json.dumps(my_dict, indent=5, separators=(';', '->'), sort_keys=True)
# print(res)


# import csv
#
# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
#         print(type(line))

'''Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
Считываем текст - сделать список строк - распилить - в словарь - затем в джисон '''

# def read_text_file(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         text = f.readlines()
#     text_dict = {}
#     for item in text:
#         key, value = item.strip().split('|') #убираем пробелы и переходы на нов. строку и пилим по /
#         key = key.title()
#         if key in text_dict:
#             text_dict[key].append(value)
#         else:
#             text_dict[key] = [value]
#     return text_dict
#
#
# def write_json(file_name, json_data):
#     with open(file_name, 'w', encoding='utf-8') as f:
#         json.dump(json_data, f, indent=4, ensure_ascii=False)
#
#
#
# json_data = read_text_file("multiple_file.txt")
# write_json('names.json', json_data)

'''Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
1-ый уровень словарь - Доступы, внутри словарь с ID + имя
Читаем, кладем в буфферную переменную, т к в джисоне только один словарь может лежать,
далее еперзаписываем дополненный словарь  в джисон_файл
1) ф-ция проверки ввода на INT
2) ф-ция get_user_id, в ней 1-ая ф-ция как проверка
3)  
'''
import os
import json

JSON_FILE_NAME = 'users.json'


# def input_int(input_msg: str, error_msg: str, min_value: int = None, max_value: int = None):
#     while True:  #
#         number = input(input_msg)
#         if number.isdigit():
#             if min_value and max_value:
#                 # если число не равно None, передано число и НЕ = 0
#                 if min_value <= int(number) <= max_value:
#                     return int(number)
#             else:
#                 return int(number)
#         print(error_msg)

def input_int(input_msg: str, error_msg: str, min_value: int = None, max_value: int = None):
    while True:
        number = input(input_msg)
        if number.isdigit():
            number = int(number)
            if (min_value is not None and number < min_value) or (max_value is not None and number > max_value):
                print(error_msg)
            else:
                return number
        else:
            print(error_msg)



def get_user_id(id_list: list):
    while True:  # если введен id который уже есть, нужно ввести заново, файл считывается каждый раз
        user_id = input_int('Введите ID: ', 'ID должен состоят из цифр!')
        if str(user_id) not in id_list:  # str - так как в джисон все строки
            return user_id
        print('Такой ID уже зарегистрирован!')


def get_list_id(json_data):
    id_list = []
    for level, user in json_data.items():  # проходимся по ключам
        for user_id in user:  # проходимся по ключам юзеров и собираем только ключи юзеров
            id_list.append(str(user_id))  # str - так как в джисон все строки
    return id_list


def json_load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    return {}


def json_write(file_name, json_data):
    with open(file_name, 'w', encoding='UTF-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


def create_users():
    while True:
        user_data = json_load(JSON_FILE_NAME)
        id_list = get_list_id(user_data)  # получили ид-лист
        # если ничего не вели - то выходим
        if not (user_name := input('Введите имя пользователя: ')):
            print('Спасибо, ввод пользователей закончен')
            break
        user_id = get_user_id(id_list)
        user_level = input_int('Введите уровень доступа: ', 'Уровень должен быть от 1 до 7', 1, 7)
        # Проверяем, существует ли ключ user_level в словаре user_data
        if str(user_level) in user_data:
            # Если ключ существует, добавляем/обновляем запись с ключом user_id и значением user_name в соответствующем подсловаре
            user_data[str(user_level)][str(user_id)] = user_name
        else:
            # Создаем новую запись в словаре user_data с ключом user_level и значением - новый словарь, содержащий user_id и user_name
            user_data[str(user_level)] = {str(user_id): user_name}
        json_write(JSON_FILE_NAME, user_data)


if __name__ == '__main__':
    create_users()





