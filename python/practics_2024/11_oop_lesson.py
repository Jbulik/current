# '''Расширение неизменяемых классов'''
#
# class NamedInt(int): #родительский класс int
#     def __new__(cls, value, name):
#         #super() - тут обращение к классу Int
#         #Параметр value нужен для передачи значения в родительский класс int
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
#
#
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a + b
# print(f'{c = }\t{type(c) = }')
#
#
# '''Шаблон Одиночка, Singleton
# Ещё один вариант использования дандре __new__ — паттерн Singleton. Он
# позволяет создавать лишь один экземпляр класса. Вторая и последующие попытки
# будут возвращать ранее созданый экземпляр
# Переменные a и b ссылаются на один и тот же класс, а
# следовательно их свойство name общее.
# '''
#
# class Singleton:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self, name: str):
#         self.name = name
#         a = Singleton('Первый')
#
#
# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(f'{a.name = }\n{b.name = }')


class User:
    """A User training class for demonstrating class
    documentation.
    Shows the operation of the help(cls) and the dander method
    __doc__"""
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_1 = User('Спенглер')
print('Справка класса User ниже', '*' * 50)
help(User)
print('Справка экземпляра u_1 ниже', '*' * 50)
help(u_1)


'''Переопределение методов не обязательно должно быть для чисел. Напишем класс,
который генерирует шкаф с одеждой и выбрасывает указанное количество вещей
при правом сдвиге. Не забудем, что дандер метод должен возвращать новый
экземпляр'''

from random import choices
class Closet:
CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка',
'перчатки', 'носки', 'туфли')
def __init__(self, count: int, storeroom=None):
self.count = count
if storeroom is None:
self.storeroom = choices(self.CLOTHES, k=count)
else:
self.storeroom = storeroom
def __str__(self):
names = ', '.join(self.storeroom)
return f'Осталось вещей в шкафу {self.count}:\n{names}'
def __rshift__(self, other):
shift = self.count if other > self.count else other
self.count -= shift
return Closet(self.count, choices(self.storeroom,
k=self.count))
storeroom = Closet(10)
print(storeroom)
19
for _ in range(4):
storeroom = storeroom >> 3
print(storeroom)


