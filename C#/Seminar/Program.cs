int SumNumber(int number)
{
    int sum = 0;
    for (int i = 1; i <= number; i++)
        {
            sum = sum + i;
        }
    return sum;
}
Console.WriteLine("введите число:");
int number = int.Parse(Console.ReadLine());
Console.WriteLine("Сумма чисел равна " + SumNumber(number));