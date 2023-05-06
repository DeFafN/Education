// Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
void DoubleArray2D()
{
    Console.WriteLine("Введите размер 1-го измерения массива");
    int firstLength = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите размер 2-го измерения массива");
    int secondLength = Convert.ToInt32(Console.ReadLine());
    double[,] array = new double[firstLength, secondLength];
    Random rnd = new Random();
}


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