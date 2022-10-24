# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

# u_number = input("Enter number:")

# sum = 0
# el = 0

# for i in u_number:
#     try:
#         el = int(i)
            
#     except: continue
    
#     sum = sum+el

# if sum!=0:
#     print(sum)
# else:
#     print("Введите число")


# #Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# el_in_list = 1
# my_list = []
# u_number = input("Enter number + enter: ")

# while not u_number.isdigit():
#     print("Please, repeat ...")
#     u_number = input("Enter number + enter: ")
# else:
#     u_number = int(u_number)
#     for i in range(1, u_number + 1):
#         el_in_list = el_in_list * i
#         my_list.append(el_in_list)

# print(my_list)

# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.


# polin = input("Enter number + enter: ")

# while not polin.isdigit():
#     print("Please, repeat ...")
#     polin = str(input("Enter number + enter: "))

# if  polin.find("-") != -1:
#     polin = int(polin) * -1

# while True:
#     polin2 = '' .join(reversed(polin))
#     if polin == polin2:
#         print("Полиндром ->" ,polin2, polin)
#         break     
#     else:
#         polin=str(int(polin) + int(polin2))   

print("*\n" + "*"*2\n)