using System.Threading.Tasks;
using System;
string Input (string text)
{
    Console.Write($"{text}");
    return Console.ReadLine();
}


void Print(int[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
    {
        Console.Write($"{numbers[i]} ");
    }
    Console.WriteLine();
}


void UserEnterArray(int [] numbers)
{
    
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] = Convert.ToInt32(Input($"Введите {i+1}-ое число: "));
    }
}


int PositiveNumbers(int [] numbers)
{
     int count = 0;
        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] > 0)
            count++;
        }
    return count;
}


void UserEnerCoordinates(double [] numbers)
{
    numbers[0] = Convert.ToDouble(Input($"Введите k1: "));
    numbers[1] = Convert.ToDouble(Input($"Введите b1: "));
    numbers[2] = Convert.ToDouble(Input($"Введите k2: "));
    numbers[3] = Convert.ToDouble(Input($"Введите b2: "));
}

void Paralel (double[] coordinate)
{
    if (coordinate[0] == coordinate[2])
        {
            Console.WriteLine("Линии паралелльны, решения не существует");
        }
    else
    {
        double coordinataX = (coordinate[3] - coordinate[1]) / (coordinate[0] - coordinate[2]);
        double coordinataY = coordinate[0] * coordinataX + coordinate[1];
        Console.WriteLine($"Точка пересечения прямых иммет координаты Х = {Math.Round(coordinataX, 1)} и У = {Math.Round(coordinataY, 1)}");       
    }
}

// Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
// 0, 7, 8, -2, -2 -> 2
// -1, -7, 567, 89, 223-> 3
void PositiveNumbersInArray()
{
    Console.WriteLine("Введите размер массива");
    int size = int.Parse(Console.ReadLine());
    int [] numbers = new int [size];
    UserEnterArray(numbers);
    Print(numbers);
    Console.WriteLine($"Количество чисел больше 0 равно {PositiveNumbers(numbers)}");
}

// Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
//b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)
void FindIntersection()
{
    double [] coordinate = new double [4];
    UserEnerCoordinates(coordinate);
    Paralel(coordinate);
}