'''Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:

animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости от типа животного.

Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением 'Недопустимый тип животного'.'''

from typing import Any

class Animal:
    def __init__(self, name: str, *args):
        self.name = name
        self.args = args  # Сохраняем args в атрибуте объекта

    def get_info(self) -> str:
        # Форматирование строки с информацией о типе и имени животного
        args_info = ", ".join(map(str, self.args))  # Преобразуем args в строку
        return (
            f"{'Type:':8}{type(self).__name__}\n"
            f"{'Name:':8}{self.name}\n"
            f"{'Args:':8}{args_info}\n"
            f"{'разновидность:':8}{Fish.depth(animal1)}\n"
        )



class Mammal(Animal):

    def __init__(self, name:str, weight: int, *args):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class Bird(Animal):

    def __init__(self, name: str, wingspan: float, **_):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self) -> float:
        return float(self.wingspan - 100)


class Fish(Animal):

    def __init__(self, name:str, max_depth:int, *args):
        super().__init__(name)
        self.max_depth = max_depth
        self.args = args

    def depth(self) -> str:
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

#Для сдачи на платформе

# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type: str, name: str, *args):
#         if animal_type == 'Bird':
#             if len(args) < 1:
#                 raise ValueError('Недостаточно аргументов для создания Bird')
#             # Извлекаем первый элемент из args
#             wing_length = args[0]
#             return Bird(name, wing_length)
#         elif animal_type == 'Fish':
#             if len(args) < 1:
#                 raise ValueError('Недостаточно аргументов для создания Fish')
#             # Извлекаем первый элемент из args
#             depth = args[0]
#             return Fish(name, depth)
#         elif animal_type == 'Mammal':
#             if len(args) < 1:
#                 raise ValueError('Недостаточно аргументов для создания Mammal')
#             weight = args[0]
#             return Mammal(name, weight)
#         else:
#             raise ValueError('Недопустимый тип животного')
# #


# # Создание экземпляров животных
# animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
#
# # Вывод результатов
# print(animal1.wing_length())
# print(animal2.depth())
# print(animal3.category())

#Вариант 1. Статическая функция - БЕЗ создания класса
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type: str, *args):
#         match animal_type:
#             case 'Fish':
#                 return Fish ('лосось', 50)
#             case 'Bird':
#                 return Bird('Орел', 200)
#
#
#
# # Создание экземпляров животных
# animal1 = AnimalFactory.create_animal('Bird')
# animal2 = AnimalFactory.create_animal('Fish')
# animal3 = AnimalFactory.create_animal('хзхзхз')
#
# # Вывод результатов
# print(animal1.wing_length())
# print(animal2.depth())
# print(type(animal3))


'''Универасальный вариант от Кирилла
1) не используем класс =не создаем экз-ры AnimalFabric(он Абстрактный)-а Создаем объекты внутри
2) `__new__` создает объект: Когда вы создаете экземпляр класса, сначала вызывается метод `__new__`,
 который отвечает за создание самой структуры объекта в памяти.    
2. **`cls` — это класс**: `cls` в данном методе — это сам класс `AnimalFabric`.
 Это то же самое, что и `self` в методах экземпляра, но для методов класса.
3. **Параметры**: 
   - `animal_type` указывает, какой тип животного вы хотите создать (например, 'mammal', 'bird', 'fish').'''
class AnimalFabric:
    #Мы вызываем `__new__` дважды: первый раз — чтобы определить метод в нашем классе,
    # второй раз — чтобы создать новый объект типа `animal_type`.
    def __new__(cls, animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal, Any]:
        try:
            # Создаем экземпляр объекта от родительского класса Object (или переданного animal_type)
            #super()` возвращает объект-посредник, который позволяет вызвать методы родительского класса.
            # В контексте метода `__new__`, родительским классом обычно является `object`.
            animal = super().__new__(animal_type)
            # # Инициализируем объект, наделяя его характеристиками, переданными в args и kwargs
            animal.__init__(*args, **kwargs)
            return animal
        except Exception as exc:
            #возвращается путь ошибки
            print(f'{exc.__class__.__name__} {exc}')
            return Animal('Cadaver')


animal1 = AnimalFabric(Fish, 'Буль', 50, [112321, 555, 0])


# Вывод результатов
print(animal1.get_info())
# print(animal2.get_info())
# print(animal3.get_info())





