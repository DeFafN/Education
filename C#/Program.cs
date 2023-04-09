// int N = int.Parse(Console.ReadLine());
// if(N<0) N = N*-1;
// for (int i = -N; i <= N; i++)
// {
//     Console.WriteLine(i);
// }
//int M = int.Parse(Console.ReadLine())%10;
//Console.WriteLine(M);
double count = 0;
double distance = 10000;
double firstfriendspeed = 1;
doub
le secondfriendspeed = 2;
double dogspeed = 5;
double friend = 2;
double time = 0;
while(distance > 10)
{
    if(friend == 1)
    {
        time = distance / (firstfriendspeed+dogspeed);
        friend = 2;
    }
    else
    {
        time = distance / (secondfriendspeed+dogspeed);
        friend = 2;
    }
    distance = distance - (firstfriendspeed + secondfriendspeed) * time;
    count = count + 1;
}
Console.Write(count);