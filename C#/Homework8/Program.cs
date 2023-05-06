// Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
Console.WriteLine("Введите размер 1-го измерения массива");
int firstLength = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите размер 2-го измерения массива");
int secondLength = Convert.ToInt32(Console.ReadLine());
double[,] array = new double[firstLength, secondLength];
Random rnd = new Random();

double[,] CreateTwoDimensionArray(double[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
        for (int j = 0; j < array.GetLength(1); j++)
            array[i, j] = Math.Round(rnd.NextDouble() * 100 - 50, 1);

    return array;
}


void PrintArray(double[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write($"{array[i, j]} ");
        Console.WriteLine();
    }
}

PrintArray(CreateTwoDimensionArray(array));


//Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
//Например, задан массив:
/*1 4 7 2
5 9 2 3
8 4 2 4
17->такого числа в массиве нет*/

Console.WriteLine("Введите номер строки в массиве");
int element1 = Convert.ToInt32(Console.ReadLine()) - 1;
Console.WriteLine("Введите номер столбца в массиве");
int element2 = Convert.ToInt32(Console.ReadLine()) - 1;
int[,] array = CreateTwoDimensionArray(4, 4);
PrintArray(array);
if (element1 < array.GetLength(0) && element2 < array.GetLength(1))
{
    Console.WriteLine($"Элемент равен {array[element1, element2]}");
}
else // Вот здесь не понял почему не работает а выдаёт стандартную ошибку о том что индекс за пределами массива
{
    Console.WriteLine($" Элемента не существует");
}


int[,] CreateTwoDimensionArray(int firstLength = 10, int secondLength = 10)
{
    int[,] array = new int[firstLength, secondLength];

    for (int i = 0; i < array.GetLength(0); i++)
        for (int j = 0; j < array.GetLength(1); j++)
            array[i, j] = new Random().Next(0, 100);

    return array;
}


void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write($"{array[i, j]} ");
        Console.WriteLine();
    }
}

//Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
//Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
//Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.


int[,] array = CreateTwoDimensionArray(4, 4);
PrintArray(array);
string result = "";
for (int i = 0; i < array.GetLength(1); i++)
{
    int sum = 0;
    for (int j = 0; j < array.GetLength(0); j++)
    {
        sum+= array[j,i];
        
    }
    double avg = Math.Round((Convert.ToDouble(sum) / array.GetLength(0)), 1);
    result = result + " " + avg.ToString();
    Console.WriteLine($"Среднее арифметическое по столбцам равно {result} ");
}



int[,] CreateTwoDimensionArray(int firstLength = 10, int secondLength = 10)
    {
        int[,] array = new int[firstLength, secondLength];

        for (int i = 0; i < array.GetLength(0); i++)
            for (int j = 0; j < array.GetLength(1); j++)
                array[i, j] = new Random().Next(0, 100);

        return array;
    }

void PrintArray(int[,] array)
    {
        for (int i = 0; i < array.GetLength(0); i++)
        {
            for (int j = 0; j < array.GetLength(1); j++)
                Console.Write($"{array[i, j]} ");
            Console.WriteLine();
        }
    }


