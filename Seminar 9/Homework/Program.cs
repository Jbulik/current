// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.


int[,] GetArray(int m, int n, int minValue, int maxValue) // генерация массива
{
    int[,] MyArray = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            MyArray[i, j] = new Random().Next(minValue, maxValue + 1);
        }
    }
    return MyArray;
}


void PrintArray(int [,] AnyArray) // вывод массива
{
    for (int i = 0; i < AnyArray.GetLength(0); i++)
    {
        for (int j = 0; j < AnyArray.GetLength(1); j++)
        {
            Console.Write($"{AnyArray[i,j]} ");
        }
        Console.WriteLine();
    }
}

 
 int[,] GetMultiArray(int[,] Array1, int[,] Array2)
            {
                int[,] MultiMatrix = new int[Array1.GetLength(0), Array2.GetLength(1)];
                for (int i = 0; i < Array1.GetLength(0); i++)

                {
                    for (int j = 0; j < Array2.GetLength(1); j++)
                    {
                        for (int k = 0; k < Array1.GetLength(1); k++)
                        {

                            MultiMatrix[i,j] += Array1[i, k] * Array2[k, j];
                        }

                    }
                }
                return MultiMatrix;

            }


//Console.Clear();
Console.WriteLine("Введите число строк 1-й матрицы: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число столбцов 1-й матрицы : ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число столбцов 2-й матрицы: ");
int p = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число строк 2-й матрицы: ");
int l = Convert.ToInt32(Console.ReadLine());

if (n != l)
            {
                Console.WriteLine("Нельзя умножать, число колонок 1-ой должны быть равны числу строк второй");
               // return 0;
            }

int[,] FirstArray = GetArray(m, n, 1, 10);
PrintArray(FirstArray);
Console.WriteLine("___________________");

int[,] SecondArray = GetArray(l, p, 1, 10);
PrintArray(SecondArray);
Console.WriteLine("___________________");

int[,] ResultArray = GetMultiArray(FirstArray, SecondArray);
PrintArray(ResultArray);
