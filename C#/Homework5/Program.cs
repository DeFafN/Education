string input (string text)
{
    Console.Write($"{text}");
    return Console.ReadLine();
}

void Fill_random_thre_digit_positive_numbers(int[] numbers)
{
    Random rnd = new Random();
    for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = rnd.Next(100, 1000);
        }
}

void Fill_user_numbers(int[] numbers, int minvalue = -1000, int maxvalue = 1000)
{
    Random rnd = new Random();
    maxvalue++;
    for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = rnd.Next(minvalue, maxvalue);
        }
}

void Print(int[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
    {
        Console.Write($"{numbers[i]} ");
    }
    Console.WriteLine();
}

int Even(int[] numbers)
{
    int count = 0;
        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] % 2 == 0)
            count++;
        }
    return count;
}

int sum_not_even_numbers (int[] numbers)
{
    int result = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        if (i % 2 != 0)
        {
            result = result + numbers[i];
        }
    }
    return result;    
}

// Задайте массив заполненный случайными положительными трёхзначными числами.
// Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2
void Even_in_Array()
{
    Console.WriteLine("Введите размер массива");
    int size = int.Parse(Console.ReadLine());
    int[] numbers = new int[size];
    Fill_random_thre_digit_positive_numbers(numbers);
    Console.WriteLine("Созданный массив:");
    Print(numbers);
    Console.Write("Количество чётных чисел: ");
    Console.WriteLine(Even(numbers));
}
//Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов с нечётными индексами.
//[3, 7, 23, 12] -> 19
//[-4, -6, 89, 6] -> 0
void not_even_index()
{
    Console.WriteLine("Введите размер массива");
    int size = int.Parse(Console.ReadLine());
    int[] numbers = new int[size];
    Fill_user_numbers(numbers, -100, 500);
    Console.WriteLine("Созданный массив:");
    Print(numbers);
    Console.WriteLine($"Сумма нечётных элементовсозданного массива: {sum_not_even_numbers(numbers)}");
}
// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементами массива.
// [3,21 7,04 22,93 -2,71 78,24] -> 80,95





