// Задача 2
Console.Write("Введите первое число ");
int a = int.Parse(Console.ReadLine());
Console.Write("Введите второе число ");
int b = int.Parse(Console.ReadLine());
if(a > b){
    Console.WriteLine($"Максимальное значение {a}");
}
else{
    Console.WriteLine($"Максимальное значение {b}");
}
// Задача 4
Console.Write("Введите первое число ");
int c = int.Parse(Console.ReadLine());
Console.Write("Введите второе число ");
int d = int.Parse(Console.ReadLine());
Console.Write("Введите третье число ");
int e = int.Parse(Console.ReadLine());
if(c > d){
    if(c > e){
    Console.WriteLine($"Максимальное значение {c}");    
    }
    else
    Console.WriteLine($"Максимальное значение {e}");
}
else{
    if(d > e){
    Console.WriteLine($"Максимальное значение {d}");    
    }
    else
    Console.WriteLine($"Максимальное значение {e}");
}
// задача 6
Console.Write("Введите число ");
int f = int.Parse(Console.ReadLine());
if(f % 2 == 0){
    Console.WriteLine("Да");    
}
else{
    Console.WriteLine("Нет");    
}
// задача 8
int count = 1;
Console.Write("Введите число ");
int N = int.Parse(Console.ReadLine());
while(count < N){
    if(count % 2 == 0){
        Console.WriteLine(count);
    }
count++;
}