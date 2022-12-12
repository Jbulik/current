# № 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# 3 1 2 3
# 2 1

# data = list(map(int,input('Введите первый набор').split()))

# data_unique = list(filter(lambda x: data.count(x)==1, data)) 

# print(f' исходный список: {data}')
# print((f' уникальный список: {data_unique}'))



#spisok1 = list(map(int,(file.readline.split())))

# # № 1. Пользователь вводит число, Вам необходимо вывести число Пи
# #  с той точностью знаков после запятой, сколько указал пользователь
# import math
# print(math.pi)

# n = int(input('Введите число'))
# p = str(math.pi)
# poz = n+2

# print(float(p[:poz]))

# # № 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# # N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# # 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

# n = int(input('Введите число'))
# spisok = []

# i = 2 # первое простое число
# spisok = []

# while i <= n:
#     if n % i == 0:
#         spisok.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {n} приведены в списке: {spisok}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h = 0
#     a, b, c, d, e, h - рандом
# Клеим: 1){рандом-коэффициент} * 'x' * {степень k} +
# 2) {последнее слагаемое, рандом} '= 0' 
# Идем с конца. 

# from random import randint

# k = int(input('Введите степень многочлена:  '))
# for i in range(k, 0, -1):
#     kof = randint(1,100)
#     if kof == 1: # ничего не добавляем
#         kof = '' 
#     else:
#         if i != 1: # bx^4+
#             part = f'{kof} * x^{i} + ' 

#         else: 
#             part = f'{kof} * x + ' # ex // число без k, когда k=1
#     print(part, end= '') # выводим 2*x² + 4*x +
# print(f'{randint(1,101)} = 0') #доклеиваем   5 = 0 



def check_input_number(my_num):
    while my_num.isdigit() == False:    
             
        my_num=input('Опечаталась, бывает..  ')
    else:  
        #задаем условие, если 1-ый while не срабатывает 
        while int(my_num)<0 or int(my_num)>28:  
           my_num=int(input('Промахнулась, бывает..  '))
    return int(my_num)          
        
my_num=input('ввод') 
print(check_input_number(my_num))
print(type(my_num))


    



