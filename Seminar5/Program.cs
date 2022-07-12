// № 36 задайте одномерный массив случайных чисел. найти сумму эл-ов на нечетных позициях

    // int[] CreateRandomArray(int size, int min, int max)
    // {
    //     int[] array = new int[size];
    //     for (int i = 0; i < size; i++)
    //     {
    //         array[i] = new Random().Next(min, max + 1);
    //     }
    //     return array;
    // }


    // void ShowArray(int[] array)
    // {
    //     Console.Write("[ ");
    //     for (int i = 0; i < array.Length; i++)
    //     {
    //         Console.Write(array[i] + " ");
    //     }
    //     Console.Write(" ] -> ");
        
    // }

//  int SummUneven (int [] array)
//     {
//         int Sum = 0;
//         for (int i = 0; i < array.Length; i+=2)
//         {
//             Sum = Sum + array[i];
//         }
//         return Sum;
//     }
 
 
 
//  int[] myArray = CreateRandomArray(5 , 1, 10);
//   ShowArray(myArray);
//   Console.WriteLine(SummUneven(myArray));
  
//№ 38 задайте одномерный массив случайных чисел. Найти разницу м/д макс и мин элементами

// int[] CreateRandomArray(int size, int min, int max)
//     {
//         int[] array = new int[size];
//         for (int i = 0; i < size; i++)
//         {
//             array[i] = new Random().Next(min, max + 1);
//         }
//         return array;
//     }


//     void ShowArray(int[] array)
//     {
//         Console.Write("[ ");
//         for (int i = 0; i < array.Length; i++)
//         {
//             Console.Write(array[i] + " ");
//         }
//         Console.Write(" ] -> ");
        
//     }


//  int DeltaFind (int [] array)
//     {
//         int MinNum = array[0];
//         int Max = array[0];
//         for (int i = 0; i < array.Length; i++)
//         {
//            if (array[i] < MinNum) 
//            MinNum = array[i];
                      
//         }

//         for (int i = 0; i < array.Length; i++)
//         {
//            if (array[i] > Max) 
//             Max = array[i];           
//         }

//         int delta= Max - MinNum;
        
//         return delta;
        
//     }

 
 
//  int[] myArray = CreateRandomArray(5 , 1, 10);
//   ShowArray(myArray);
//   Console.WriteLine(DeltaFind(myArray));
  

  //Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2

int[] CreateRandomArray(int size, int min, int max)
    {
        int[] array = new int[size];
        for (int i = 0; i < size; i++)
        {
            array[i] = new Random().Next(min, max);
        }
        return array;
    }


int QuantityPositive(int[] array){
    int quantity = 0;
    for (int i = 0; i<array.Length; i++ )
    {
    if (array[i] % 2 == 0)
    {
      quantity++;
    }
  }
  return quantity;
}

 Console.Clear();
int[] array = CreateRandomArray(4, 100, 900);
Console.WriteLine(String.Join( " ", array));

int quantity = QuantityPositive (array);
Console.WriteLine($"Количество чётных чисел в массиве: {quantity}");


