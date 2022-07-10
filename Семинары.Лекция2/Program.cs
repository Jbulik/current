// вывод случайных чисел c 10 до 99



int number = new Random().Next(1, 100);
//Console.Write(number);

int num1 = number / 10;
int num2 = number % 10;

Console.WriteLine(number + " "+ num1 + ' ' + num2);


