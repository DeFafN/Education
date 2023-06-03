/*Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2*/

using System.ComponentModel.DataAnnotations;

int[,] array = CreateTwoDimensionArray(4,3);
PrintArray(array);
Sort(array);
Console.WriteLine("Упорядоченная матрица");
PrintArray(array);
Console.WriteLine();
int[,] CreateTwoDimensionArray(int firstLength = 10, int secondLength = 10)
{
    int[,] array = new int[firstLength, secondLength];

    for (int i = 0; i < array.GetLength(0); i++)
        for (int j = 0; j < array.GetLength(1); j++)
            array[i, j] = new Random().Next(0, 10);

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
void Sort(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(1) - 1; k++)
            {
                if (array[i, k] < array[i, k + 1])
                {
                    int temp = array[i, k + 1];
                    array[i, k + 1] = array[i, k];
                    array[i, k] = temp;
                }
            }
        }
    }
}

/*Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка*/

int[,] arraySecond = CreateTwoDimensionArray(8, 2);
PrintArray(arraySecond);
Console.WriteLine();
MinRow(arraySecond);
void MinRow(int[,] array)
{
    int minSumElementsInRow = 0;
    int rowWithMinSum = 0;
    int sumElementsinRow = 0;
    for (int i = 0; i < array.GetLength(1); i++)
    {
        minSumElementsInRow += array[0, i];
    }
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++) sumElementsinRow += array[i, j];
        if (sumElementsinRow < minSumElementsInRow)
        {
            minSumElementsInRow = sumElementsinRow;
            rowWithMinSum = i;
        }
        sumElementsinRow = 0;
    }
    Console.Write($"Строка с минимальной суммой элементов: {rowWithMinSum + 1}");
}
Console.WriteLine();

/*Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18*/

int[,] firstMartrix = CreateTwoDimensionArray(2, 2);
int[,] secomdMartrix = CreateTwoDimensionArray(2, 2);
Console.WriteLine("Первая матрица:");
PrintArray(firstMartrix);
Console.WriteLine("Вторая матрица:");
PrintArray(secomdMartrix);
MultiplyMatrix(firstMartrix, secomdMartrix);
Console.WriteLine("Произведение первой и второй матриц:");
PrintArray(MultiplyMatrix(firstMartrix,secomdMartrix));

int[,] MultiplyMatrix(int[,] firstMartrix, int[,] secomdMartrix)
{
    int[,] resultMatrix = new int[2, 2];
    for (int i = 0; i < resultMatrix.GetLength(0); i++)
    {
        for (int j = 0; j < resultMatrix.GetLength(1); j++)
        {
            int sum = 0;
            for (int k = 0; k < firstMartrix.GetLength(1); k++)
            {
                sum += firstMartrix[i, k] * secomdMartrix[k, j];
            }
            resultMatrix[i, j] = sum;
        }
    }
    return resultMatrix;
}

/*Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Массив размером 2 x 2 x 2
66(0,0,0) 25(0, 1, 0)
34(1, 0, 0) 41(1, 1, 0)
27(0, 0, 1) 90(0, 1, 1)
26(1, 0, 1) 55(1, 1, 1)

Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
Например, на выходе получается вот такой массив:
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07*/