from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)

        return instance

    def __init__(self, value, author):
        self.value = value
        self.author = author
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M')

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time}'

    #используется для предоставления строкового представления объекта, которое должно быть однозначным и,
    # предпочтительно, таким, что при передаче этой строки в функцию `eval` будет создан объект, эквивалентный данному
    def __repr__(self):
        #  Оператор `!r` вызывает метод `__repr__` для аргументов, что гарантирует,
        #  что строки будут заключены в кавычки.
        return f"MyStr({self.value!r}, {self.author!r})"







my_string = MyStr("Пример текста", "Иван")
print(my_string)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))




