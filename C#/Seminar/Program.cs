using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Dynamic;
using System;
using System.Globalization;
void Fill(int[] numbers, int minvalue = -9, int maxvalue = 9)
{
    maxvalue++;
    Random rnd = new Random();
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] = rnd.Next(minvalue, maxvalue);
    }

}

void Print (int[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
    {
        Console.Write($"{numbers[i]} ");
    }
    Console.WriteLine();
}
void reverse(int[] numbers)
{
    int halfsize = numbers.Length / 2;
    int lastindex = numbers.Length -1;
    for (int i = 0; i < halfsize; i++)
    {
        int temp = numbers[i];
        numbers[i] = numbers[lastindex -i];
        numbers[lastindex - i] = temp;
    }
}
string input (string text)
{
    Console.Write($"{text}");
    return Console.ReadLine();
}

void task1()
{
int size = 10;
int[] numbers = new int[size];
Fill(numbers);
Print(numbers);
reverse(numbers);
Print(numbers);
}


void task2()
{
int side1 = Convert.ToInt32(input("Введите длинну стороны 1 "));
int side2 = Convert.ToInt32(input("Введите длинну стороны 2 "));
int side3 = Convert.ToInt32(input("Введите длинну стороны 3 "));
if (side1 + side2 > side3 && side2 + side3 < side3 && side2 + side3 < side1)
    Console.WriteLine("Труегольник существует");
else 
{
    Console.WriteLine("Труегольник не существует");
}
}

void task3 ()
{
    int number = Convert.ToInt32(input("Введите число:"));
    int value = number;
    int resultint = 0;
    string resultStr = "";
    int shift = 1;
    while (number > 0)
    {
        resultStr = value % 2 + resultStr;
        resultint += value % 2 * shift;
        shift*=10;
        value /= 2;
    }
    Console.WriteLine($"Число в двоичном представлении {resultStr}");
    Console.WriteLine($"Число в двоичном представлении {resultint}");
}

void task4();
{
 int numf = 0;
 int nums = 1;
 int count = Convert.ToInt32(input("количество элементов последовательности"));
    for (int i = 0; i < count; i++)
        {
        Console.Write($"{numf} ");
        int temp = numf;
        numf = nums;
        nums = temp + nums;
        }
}
void task5()
{
maxvalue++;
    Random rnd = new Random();
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] = rnd.Next(minvalue, maxvalue);
    }

}