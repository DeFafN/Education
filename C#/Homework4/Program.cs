// Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
int Pow (int Base, int index)
{
int result = Base;
if (index == 0)
    {
        return 1;
    }
else
    {
        for (int i = 0; i < index-1; i++)
        {
            Base = Base * result;
        }
    return Base;    
}
}
Console.Write("введите число которое необходимо возвести в степень ");
int Base = int.Parse(Console.ReadLine());
Console.Write("введите степень в которую необходимо возвести ");
int index = int.Parse(Console.ReadLine());
Console.WriteLine("результат операции: " + Pow(Base, index));