from calculator import PowerCalculator
from exceptions import InvalidInputException

if __name__ == "__main__":
    calculator = PowerCalculator()

    # Запрашиваем у пользователя ввод чисел до тех пор, пока не будет введено корректное значение
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Выполняем базовые операции с числами
            sum_result = calculator.add(num1, num2)
            difference_result = calculator.subtract(num1, num2)
            product_result = calculator.multiply(num1, num2)

            print(f"Sum: {sum_result}")
            print(f"Difference: {difference_result}")
            print(f"Product: {product_result}")

            # Проверяем, что введены корректные числа для операции деления
            try:
                quotient_result = calculator.divide(num1, num2)
                print(f"Quotient: {quotient_result}")
            except InvalidInputException as e:
                print(e)

            # Проверяем, что введены корректные числа для операции возведения в степень
            try:
                power_result = calculator.calculatePower(num1, num2)
                print(f"Power: {power_result}")
            except InvalidInputException as e:
                print(e)

            break  # Выходим из цикла, если введены корректные числа

        except ValueError:
            print("Invalid input: Please enter valid numbers")
        except ZeroDivisionError:
            print("Invalid input: Division by zero")
