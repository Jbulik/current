from exceptions import InvalidInputException

# создаем класс Calculator для выполнения базовых математических операций
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise InvalidInputException("Division by zero is not allowed")
        return a / b

# класс PowerCalculator, который наследуется от Calculator
class PowerCalculator(Calculator):
    # Метод для вычисления степени числа
    def calculatePower(self, base, exponent):
        if base == 0 or (base < 0 and exponent < 0):
            raise InvalidInputException("Invalid input: Cant get Power - base cannot be zero or negative when exponent is negative")
        return base ** exponent
