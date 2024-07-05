'''Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.'''

# PI = 3.14
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def length(self):
#         return PI * self.radius * 2
#
#     def area(self):
#         return PI * self.radius ** 2
#
#
# if __name__ == '__main__':
#     circle = Circle(5)
#
#     print(circle.length())
#     print(circle.area())

'''Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.'''

# class Rectangle:
#
#     def __init__(self, sitd_a, sitd_b=None):
#         self.sitd_a = sitd_a
#         self.sitd_b = sitd_b if not sitd_b is None else sitd_a
#
#     def perimeter(self):
#         return (self.sitd_a + self.sitd_b) * 2
#
#     def area(self):
#         return self.sitd_b * self.sitd_a
#
#
# if __name__ == '__main__':
#     rectangle = Rectangle(5, 4)
#     print(rectangle.perimeter())
#     print(rectangle.area())
#     square = Rectangle(6)
#     print(square.perimeter())
#     print(square.area())

'''Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.'''

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def full_name(self):
        return f'My name is {self.name + " " + self.surname} and my age is {self.__age}'

    def birthday(self): # увеличиваем на  1 год
        self.__age += 1


    def age(self):
        return self.__age
#
# if __name__ == '__main__':
#     person_1 = Person("Lucky", "Pop", 52)
#     print(person_1.full_name())
#     print(person_1.age())
#     person_1.birthday()
#     print(person_1.age())

'''Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь'''

# class Worker(Person):
#     def __init__(self, name, surname, age, id: int):
#         super().__init__(name,surname,age)
#         self.id = id
#         self.access_level = sum(map(int,str(id))) % 7
#
#     def worker_info(self):
#         return f'{self.full_name()} and my id is {self.id} and my access level {self.access_level}'
#
#
# if __name__ == '__main__':
#     worker_1 = Worker("Lucky_2", "Popik", 55, 100001)
#     print(worker_1.worker_info())

'''Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.'''

# class Animals:
#     def __init__(self, name, age):
#         self._name = name
#         self.age = age
#
#     def info(self):
#         return (f'Меня зовут {self._name}, мне {self.age} лет')
#
#     def set_name(self, name):
#         self._name = name
#
#
# class Birds(Animals):
#     def __init__(self, name, age, flight_altitude):
#         super().__init__(name, age)
#         self.flight_altitude = flight_altitude
#
#     def info(self):
#         return super().info() + f' и высота полета {self.flight_altitude}'
#
#
#     def set_height(self, height):
#         self.flight_altitude = height
#
#
# class Cat(Animals):
#     def __init__(self, name, age, run):
#         super().__init__(name, age)
#         self.run = run
#
#     def set_run(self, len_run):
#         self.run = len_run
#
#
# if __name__ == '__main__':
#     utka = Birds('Kryaka', 1, 80)
#     print(utka.info())
#     cat = Cat('Barsik', 3, 100)




