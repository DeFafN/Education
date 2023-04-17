Console.WriteLine("Введите пятизначное число");
string number = Console.ReadLine();
string reverse_number = number.Reverse(number);
if (number.Lehgth() != 5)
{
    Console.WriteLine("Количество знаков не равно 5");
}
    else if (number == reverse_number)
    {
        Console.WriteLine("Число является полиндромом");
    }
    else
    {
        Console.WriteLine("Число не является полиндромом");
    }