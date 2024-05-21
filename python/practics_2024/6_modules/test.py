import sys

print(*map(int, sys.argv[1:]))



# from random import choice
# def riddle(riddle_text, answer_list, attempts):
#     #переводим лист с отгадками в нижний регистр
#     answer_list = list(map(lambda answer: answer.lower(), answer_list))
#     print(riddle_text)
#     count = 0
#     while count < attempts:
#         answer = input("Введите отгадку: ")
#         count += 1
#         if answer.lower() in answer_list:
#             print(f"Вы угадали! Попытка номер {count}")
#             return count
#         print("Попробуйте еще раз!")
#         #берет рандомное значение из списка с отгадками
#     print(f"Попытки закончились. Правильный ответ {choice(answer_list)}")
#     return 0
#
#
# riddle(
#      'Зимой и летом одним цветом?',
#     ['ель', 'елка', 'елочка'],
#     3
#  )