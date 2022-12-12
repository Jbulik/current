# # 1. Создайте программу для игры с конфетами человек против бота.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# # Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход.
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# # 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# import random

# def check_input_number(my_num):# проверка
#     is_correct = False
#     while is_correct==False:
#         if my_num.isdigit() == False: 
#             my_num=input('Опечаталась, бывает..Введите число! ')
#         elif int(my_num)<0 or int(my_num)>28:               
#             my_num=input('Промахнулась, бывает...Повторите ввод: Число от 1 до 28 ')
#         else: 
#           is_correct = True  
#           return (my_num)
      

# amount_sweets = 120 # количество конфет

# while amount_sweets > 28:
#     print('Мой ход, я загадываю число от 1 до 28.')
#     my_num=input('Мое число такое:  ')
#     #check_input_number(my_num)
    
#     amount_sweets= amount_sweets - int(check_input_number(my_num))
#     print(f'В коробке осталось {amount_sweets} конфет')
#     if amount_sweets < 28:
#         print('Я победитель!!!') 
#         break  
     
#     print('Бот, ходите пожалуйста')
#     num = random.randint(0, 28)
#     print(num)
#     amount_sweets = amount_sweets - num
#     print(f'В коробке осталось {amount_sweets} конфет')
#     if amount_sweets < 28:
#         print('БОТ ты выиграл !') 
#         break  

 # 2. Создайте программу для игры в ""Крестики-нолики"". 


# import random

# # Разрешение игроку ввести букву, которую он выбирает.
# # Возвращает список, в котором буква игрока — первый элемент, а буква Второго — второй.
# def inputPlayerLetter():
#     letter = ''
#     while not (letter == 'x' or letter == '0'):
#         print('Вы выбираете Х или О?')
#         letter = input().upper()
# # Первым элементом списка является буква  1 игрока, вторым — буква 2-го.
#     if letter == 'Х':
#         return ['x', '0']
#     else:
#         return ['0', 'x']
# #________________________________________________________________________________________
# # Вставляем в позицию символ
# def makeMove(board, letter, move): #лист, символ, позиция
#     board[move] = letter #на позицию=move  
# #________________________________________________________________________________________
# def isWinner(bo, le):
# # Учитывая заполнение игрового поля и буквы игрока, эта функция возвращает True, если игрок выиграл.
# # Мы используем "bo" вместо "board" и "le" вместо "letter", поэтому нам не нужно много печатать.
#     return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
#     (bo[3] == le and bo[2] == le and bo[5] == le) or # через центр
#     (bo[0] == le and bo[1] == le and bo[2] == le) or # через низ
#     (bo[6] == le and bo[3] == le and bo[0] == le) or # вниз по левой стороне
#     (bo[7] == le and bo[4] == le and bo[1] == le) or # вниз по центру
#     (bo[8] == le and bo[5] == le and bo[2] == le) or # вниз по правой стороне
#     (bo[6] == le and bo[4] == le and bo[2] == le) or # по диагонали
#     (bo[8] == le and bo[4] == le and bo[0] == le)) # по диагонали   
# #________________________________________________________________________________________

# def isSpaceFree(board, move):
# # Возвращает True, если сделан ход в свободную клетку.
#     return board[move] == ' '

# def getPlayerMove(board):
# # Разрешение игроку сделать ход.
#     move = ' '
#     while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
#         print('Ваш следующий ход? (1-9)')
#         move = input()
#         return int(move)
# #____________________________________________________________________________
# def isBoardFull(board):
# # Возвращает True, если клетка на игровом поле занята. В противном случае, возвращает False.
#     for i in range(1, 10):
#         if isSpaceFree(board, i):
#             return False
#         return True




# #############################################################################################
# theBoard=["","","","","","","","",""]   
# for i in range(9):
#     if i % 2 == 0:
#         print(f'Ходит 1 - ый ИГРОК')
#         playerLetter = inputPlayerLetter()    
#     # letter=inputPlayerLetter() ## выбираем Х или 0
#     # position ## получаем позицию
#     # def isSpaceFree(board, move):# свободна ли позиция?
        
#         move = getPlayerMove(theBoard)
#         isSpaceFree(theBoard, move)
#         makeMove(theBoard, playerLetter, move)
#         if isWinner(theBoard, playerLetter):
#             print(f'Выиграл 1 - ый ИГРОК')
#         else:
#             if isBoardFull(theBoard):
                
#                 print('Ничья!')
#                 break

#     #_________    
#     if i % 2 == 1:
#         print(f'Ходит 2 - ый ИГРОК') 
#         move = getPlayerMove(theBoard)
#         isSpaceFree(theBoard, move)
#         makeMove(theBoard, playerLetter, move)
#         if isWinner(theBoard, playerLetter):
#             print(f'Выиграл 2 - ый ИГРОК')
#         else:
#             if isBoardFull(theBoard):
                
#                 print('Ничья!')
#                 break  
#____________________________________________________________________________________________________________________________________
# # 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # stroka = "aaabbbbccbbb"
# # stroka = "3a4b2c3b"  
# def encode(s): 
#     encoding = "" # сохраняет выходную строку 
#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1 
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1 
#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1
 
#     return encoding 

# def decode(s): 
#     decoding = "" # сохраняет выходную строку 
#     i = 0
    
#     while i < len(s):
               
#         if s[i].isdigit():

#             decoding += s[i + 1] * int(s[i])
        
#         i = i + 1  
 
#     return decoding 

# stroka = "aaabbbbccbbb"
# print(encode(stroka))
# stroka = "3a4b2c3b" 
# print(decode(stroka))
    




