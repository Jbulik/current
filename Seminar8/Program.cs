____________________________________________________________
ДЗ к семинару №8
Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

Например, задан массив:

1 4 7 2

5 9 2 3

8 4 2 4

В итоге получается вот такой массив:

1 2 4 7

2 3 5 9

2 4 4 8

Console.Clear();
int[,] GetArray(int m, int n, int minValue, int maxValue)
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

void PrintArray(int [,] AnyArray)
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

int[,] Remix (int [,] MixArray)
    {
  for (int i = 0; i < MixArray.GetLength(0); i++)
  {
    for (int j = 0; j < MixArray.GetLength(1); j++)
    {
      for (int k = 0; k < MixArray.GetLength(1) - 1; k++)
      {
        if (MixArray[i, k] < MixArray[i, k + 1])
        {
          int temp = MixArray[i, k + 1];
          MixArray[i, k + 1] = MixArray[i, k];
          MixArray[i, k] = temp;
        }
      }
    }
   }
   return MixArray;
}



Console.Write("Введите количество строк массива: ");
int row =Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов массива: ");
int column =Convert.ToInt32(Console.ReadLine());
int[,] FirstArray = GetArray(row, column, 1, 10);

PrintArray(FirstArray);
int[,] RezArray= Remix (FirstArray);
PrintArray(RezArray);  

Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

Например, задан массив:

1 4 7 2

5 9 2 3

8 4 2 4

5 2 6 7

Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка

Console.Clear();

Console.Write("Введите нижнюю границу диапазона: ");
int FirstEL =Convert.ToInt32(Console.ReadLine());
Console.Write("Введите верхнюю границу диапазона: ");
int LastEl =Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество строк массива: ");
int row =Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов массива: ");
int column =Convert.ToInt32(Console.ReadLine()); 


int[,] FirstArray = GetArray(row, column, FirstEL, LastEl);

PrintArray(FirstArray);

Console.WriteLine($"{NomberMinSTR(FirstArray)} - строкa с наименьшей суммой элементов ");



int SumLine(int [,]Array, int i) // поиск суммы ОДНОЙ строки

{int SumLine = 0;

{
    for (int j = 0; j < Array.GetLength(1); j++)
  {
    SumLine += Array[i,j];

    }
    return SumLine;
}
}

//основной блок
int NomberMinSTR(int[,]Array)
{
int StrNumber = 0;
int SumSTR = SumLine(Array,0);


for (int i = 1; i < Array.GetLength(0); i++)
{
for (int j = 0; j < Array.GetLength(1); j++)
    {
        int Temp = SumLine(Array, i);   
        if (SumSTR > Temp) 
        {
          SumSTR = Temp;
           StrNumber = i; 
        }
    }       

}
return StrNumber;
}





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
