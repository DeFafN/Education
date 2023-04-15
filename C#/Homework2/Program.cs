// задача 1
Console.WriteLine("Введите число");
int number = int.Parse(Console.ReadLine());
int first = number / 10;
int second =  first % 10;
Console.WriteLine("Второая цифра: "+ second);

// задача 2
Console.WriteLine("Введите число");
int number2 = int.Parse(Console.ReadLine());
if (number2>999)
{
    string convert_number2 = number2.ToString();
    Console.WriteLine("Третья цифра: " + convert_number2[2]);
}
else
{
    if(number2<100){
        Console.WriteLine("Третьей цифры нет");
    }    
    else {
        int vtoraya = number2 % 10;
        Console.WriteLine("Третья цифра: " + vtoraya);
    }
}

// задача 3
Console.WriteLine("Введите номер дня недели");
int day = int.Parse(Console.ReadLine());
if (day == 6 | day == 7){
    Console.WriteLine("Да");
}
else {
    Console.WriteLine("Нет");
}