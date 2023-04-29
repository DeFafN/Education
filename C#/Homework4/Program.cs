using System.Data;
using System.Dynamic;
using System;
// Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16
int Raw (int number, int degree)
        {
            int result = number;
            for (int i = 0; i < degree-1; i++)
            {
                result = number * result;
            }
            return result;
        }


void degree()
{
    Console.WriteLine("Введите число которое хотите возвести в степень");
    int number = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите степень в которую необходимо возвести число");
    int degree = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine($"Число {number} в степени {degree} равно {Raw(number, degree)}");    
}

// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
// 452 -> 11
// 82 -> 10
// 9012 -> 12
void Summa()
{
    Console.WriteLine("Введите цифру в которой необходимо посчитать сумму чисел");
    int number = Convert.ToInt32(Console.ReadLine());
    int sum = 0;
    while (number > 0)
    {
        sum = number%10 + sum;
        number = number / 10;
    }
    Console.WriteLine(sum);
}

// Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
// 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
// 6, 1, 33 -> [6, 1, 33]
void Print(int[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
    {
        Console.Write($"{numbers[i]} ");
    }
    Console.WriteLine();
}

void Array()
{
    Console.WriteLine("Введите элементы массива");
    int[] array = new int[8];
    for (int i = 0; i < array.Length; i++)
        {
            array[i] = Convert.ToInt32(Console.ReadLine());
        }
    Print(array);
}