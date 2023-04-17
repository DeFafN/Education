// хотелось бы уточнить почему этот код работает только до 2-х?
Console.WriteLine("Введите число");
double number = double.Parse(Console.ReadLine());
for (double i = 0; i <= number; i++)
{
    double j = i;
    i = Math.Pow(i,3);
    Console.WriteLine($"куб {j} равен {i}");
}