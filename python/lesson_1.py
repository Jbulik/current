# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# #print({a} \n{b})
# print('{} -- {}'.format(a, b))


# a = 1.32523
# b = 3



# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# for i in 'bla-bla':
#     print(f'{i},',end='')

#text = 'съешь ещё этих мягких французских булок'

# # for i in text:
# print(text)
#print(text[0:len(text):6]) 

# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"

#     print(line)

# colors = ['red', 'green', 'blue55']
# data = open('file.txt', 'a')
# #data.writelines(colors) # разделителей не будет
# data.write('\nLINE12\n')
# data.write('LINE12\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import hello

# print(hello.f(2.3))

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4))

# t = tuple(['red', 'green', 'blue'])
# a, b, c, d = t
# print(a, b)



# num = int(input('Введите число'))
# text = ['строка 1', 'строка', 'строка 3', 'строка', '13']

# for el in text:
#     if str(num) in el:
#         rez = True
#         break
#     else:
#         rez = False        
# print (rez)

dictionary = \
{
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
 
for i in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(i, dictionary[i]))

# print('Введите строку состоящую из чисел') #!!! Ввод через ПРОБЕЛ
# stroka = input().split()

# print(max([int(i) for i in stroka]))
# print(min([int(i) for i in stroka]))

#print(min([int(i) for i in input().split()]))

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(x, y, z)
#             print(not(x or y or z) == (not x and not y and not z)) 

# n = int(input('Введите число: '))
# for i in range(2, n + 1):
#     if n % i == 0:
#        print(f'Наименьший делитель числа {n} = {i}')
#        break 

# limit = int(input('Введите границу диапазона: '))
# spisok = []
# for i in range(-limit, limit+1): 
#     spisok.append(i)
# print(spisok) 

# index = []
# for i in input('введите идексы(позиции)').split():
#     index.append(int(i))

# rez = 1
# for idx in index:
#     rez = rez*spisok[idx]
# print(f'Произведение = {rez}')