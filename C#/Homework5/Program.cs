// Задайте массив заполненный случайными положительными трёхзначными числами.
// Напишите программу, которая покажет количество чётных чисел в массиве.
//[345, 897, 568, 234] -> 2

Console.WriteLine("Введите размер массива");
int size = int.Parse(Console.ReadLine());
int[] numbers = new int[size];
void Fill(int[] numbers)
{
    Random rnd = new Random();
    for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = rnd.Next(100, 1000);
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
Fill(numbers);
Console.WriteLine("созданный массив:");
Print(numbers);
Console.WriteLine(Even(numbers));