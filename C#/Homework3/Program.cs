Console.WriteLine("Введите пятизначное число");
string number = Console.ReadLine();
int Length = number.Length;
if (number.Length != 5)
{
    Console.WriteLine("Количество знаков не равно 5");
}
    else if (number[0] == number[4] && number[1] == number[3])
    {
        Console.WriteLine("Число является полиндромом");
    }
    else
    {
        Console.WriteLine("Число не является полиндромом");
    }
// Неработающий код, хотелось бы узнать почему
// Console.WriteLine("Введите пятизначное число");
// string number = Console.ReadLine();
// string reverse_number = number.Reverse();
// if (number.Length != 5)
// {
//     Console.WriteLine("Количество знаков не равно 5");
// }
//     else if (number == reverse_number)
//     {
//         Console.WriteLine("Число является полиндромом");
//     }
//     else
//     {
//         Console.WriteLine("Число не является полиндромом");
//     }