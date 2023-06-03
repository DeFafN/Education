/*Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии.
N = 5 -> "5, 4, 3, 2, 1"
N = 8 -> "8, 7, 6, 5, 4, 3, 2, 1"
*/
void PrintDigit(int digit)
{
    Console.WriteLine(digit);
    if (digit > 1)
    {
       PrintDigit(digit - 1);
    }
}
PrintDigit(2);
Console.WriteLine();
/*Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
M = 1; N = 15-> 120
M = 4; N = 8. -> 30*/

int SumOfElements(int firstDigit, int secondDigit)
{
    if (firstDigit < secondDigit)
    {
       return firstDigit + SumOfElements(firstDigit + 1, secondDigit);
    }
 return firstDigit;
}
Console.WriteLine(SumOfElements(4, 8));
Console.WriteLine();

/*Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
m = 2, n = 3->A(m, n) = 9
m = 3, n = 2->A(m, n) = 29*/

int Akerman (int numberOne , int numberTwo)
{
    if (numberOne == 0)
        return numberTwo + 1;
    else if (numberTwo == 0)
        return numberOne + 1;
    else 
        return Akerman(numberOne-1, Akerman(numberOne, numberTwo-1)); // а вот здесь вопрос, 2,3 считает нормально, совпадает с таблицей, а 3,2 выдаёт 25, 
}                                                                     // при этом этого значения в таблице из вики нет, если поменять местами аргументы в 41 строке
Console.WriteLine(Akerman(3,2));                                      // то получается stack overflow, а если поменять местами аргументы в 34 строке,
                                                                      // то stack overflow наступает почти сразу что я делаю е так?