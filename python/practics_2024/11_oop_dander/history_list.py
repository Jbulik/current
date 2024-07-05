from typing import Union
#для красоты Аргумент `number` может быть либо целым числом (int), либо числом с плавающей запятой (float)


# Определение класса Archive
class Archive:
    # Переменная класса для хранения единственного экземпляра (синглтон)
    _instance = None
    # Переменные класса для хранения архивов текста и чисел
    archive_text = []
    archive_number = []

    # Переопределение метода __new__ для реализации паттерна Singleton
    def __new__(cls, text: str, number: Union[int, float]):
        # Если экземпляр класса еще не создан
        if cls._instance is None:
            # Создаем новый экземпляр с помощью супер-класса и сохраняем в _instance
            cls._instance = super(Archive, cls).__new__(cls)
            # Инициализируем архивы текстов и чисел пустыми списками
            cls.archive_text = []
            cls.archive_number = []
        # Возвращаем уже существующий или только что созданный экземпляр
        return cls._instance

    # Инициализация экземпляра класса
    def __init__(self, text: str, number: Union[int, float]):
        # Присваиваем значения переданных аргументов атрибутам экземпляра
        self.text = text
        self.number = number
        # Добавляем текст в архив текстов
        Archive.archive_text.append(self.text)
        # Добавляем число в архив чисел
        Archive.archive_number.append(self.number)

    # Переопределение метода __repr__ для пользовательского представления объекта
    def __repr__(self):
        # Возвращаем строковое представление объекта, включающее текущий текст и число,
        # а также весь архив текстов и чисел
        return (f'Text is {self.text} and number is {self.number}. '
                f'Also {Archive.archive_text} and {Archive.archive_number}')


archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)

print(archive1)
print(archive2)
