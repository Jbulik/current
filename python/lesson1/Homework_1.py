# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#day = int(input('Введите день едели и нажмите enter: '))
#if day<=7 and day >=1:
#    if day==6 or day==7:
#        print(str(day) + ' -> да')
#    else:
#       print(str(day) + ' -> нет')
# else: 
#   print('Введён несуществующий день')


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#  и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
#- x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите кординаты Х и нажмите enter: '))
y = int(input('Введите кординаты Y и нажмите enter: '))

if x != 0 and x != 0:
    if  x>0 and y>0:
        print(f"2-ая четверть") 
    
    elif x>0 and y<0:
        print(f"4-ая четверть") 
    elif x<0 and y>0:
        print(f"1-ая четверть") 

    elif x<0 and y<0: 
        print(f"3-ая четверть")    
    
else:
    print('Введите X ≠ 0 и Y ≠ 0')

#____________________________________________________________
#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


# n = int(input('Введите номер четверти: '))
# if n == 1:
#    print('Коордитнаты x(0; inf), y(0; inf)')
# elif n == 2:
#    print('Координаты x(-inf; 0), y(0; inf)')
# elif n == 3:
#    print('Координаты x(-inf; 0), y(-inf; 0)')
# elif n == 4:
#    print('Координаты x(0; inf), y(-inf; 0)')
# else: print('Такой четверти нет!')
#____________________________________________________________

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# print('Введите координаты: x и y для точек a  и  b ')
# x_a = int(input('Введите х для A и нажмите enter: '))
# y_a = int(input('Введите y для A и нажмите enter: '))
# x_b = int(input('Введите х для B и нажмите enter: '))
# y_b = int(input('Введите y для B и нажмите enter: '))


# lengthSegment = ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** (0.5)

# print(round(lengthSegment,2))

#____________________________________________________________
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# print (f'x\t y\t z\t result')
# print ('_' * 40)
# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print (f'{x}\t {y}\t {z}\t {not(x or y or z) == (not x and not y and not z)}')






