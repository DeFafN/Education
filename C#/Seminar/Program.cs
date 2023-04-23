static void fillarray(int[] numbers)
{
    Random rnd = new Random();
    for (int i = 0; i < numbers.Length; i++)
        {
            numbers[i] = rnd.Next(-9, 10);
        }
}

static void printarray(int[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
     {
        Console.Write($"{numbers[i]} ");
     }
    Console.WriteLine();
}

static int Get_Positive_Sum(int[] numbers)
{
    int sum = 0;
    for (int i = 0; i < numbers.Length; i++)
         {
         if (numbers[i]>0) sum += numbers[i];
         }
    return sum;
}

static int Get_Negative_Sum(int[] numbers)
{
    int sum = 0;
    for (int i = 0; i < numbers.Length; i++)
     {
        if (numbers[i]<0) sum += numbers[i];
     }
    return sum;
}

static void change_numbers(int[] numbers)
    for (int i = 0; i < length; i++)
    {
        for (int i = 0; i < numbers.Length; i++)
         {
         numbers[i] *= -1;           
         }
    }

static void chek(int[] numbers)
{
    Console.WriteLine("Введите число");
    int num = int.Parse(Console.ReadLine());
    for (int i = 0; i < numbers.Length; i++)
     {
        if (num == numbers[i]) return true;
     }
     if (flag) Console.WriteLine("Число найдено");
    else Console.WriteLine("Число не найдено");
}

static void task0()
{
    int size = 12;
    int[] numbers = new int[size];
    fillarray(numbers);
    printarray(numbers);
    int sum = Get_Positive_Sum(numbers);
    Console.WriteLine($"Сумма положительных элементов равна {sum}");
    Console.WriteLine($"Сумма отрицательных элементов равна {Get_Negative_Sum(numbers)}");
}

void task1()
{
    int size = 12;
    int[] numbers = new int[size];
    fillarray(numbers);
    printarray(numbers);
    change_numbers(numbers);
    printarray(numbers);
}

void task2()
{
    bool flag = false;
    int size = 12;
    fillarray(numbers);
    printarray(numbers);
    chek(numbers);
}