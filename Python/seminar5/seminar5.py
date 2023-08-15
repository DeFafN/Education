 # найти факториал числа N через рекурсию

def factorial (n):
    if n==0:
        return 1
    return factorial (n-1) * n
n = int(input("Введите число: "))
print(factorial(n))

 # Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
 # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
 # Input: 7 Output: 13

def fib (n):
    if n == 1 or n == 2:
        return 1
    return fib (n-1) + fib(n-2)
n = int(input("Введите число: "))
print(fib(n))

 # Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
 # Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
 # Input: 2 -> 3 4 Output: 4 3

def reverse (n):
    if n == 0:
        return ''
    text = input('введите символ: ')
    return reverse(n-1) + text
print(reverse(5))

 # Напишите программу, которая на вход принимает
 # два числа A и B, и возводит число А в целую степень B с
 # помощью рекурсии.

def degree (a, b):
    if b == 1 or a == 0:
        return 1
    return degree(a, b**2)
print(degree(2,3))

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
def power(a, b):
    if a == 0 or b == 1:
        return a
    if b == 0:
     return 1
    else:
        return a* power(a, b-1)
print(power(a,b))

 # Напишите рекурсивную функцию sum(a, b),
 # возвращающую сумму двух целых неотрицательных чисел. Из
 # всех арифметических операций допускаются только +1 и -1.
 # Также нельзя использовать циклы.

def summ(a,b):
    if b == 0:
        return a
    return 1+ summ(a, b-1)
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(summ(a,b))


 # определить простое число или составное

number = int(input("Введите число: "))
def simple (numberOne, devider = 2):
    if numberOne == 2 or devider * devider > numberOne:
       return print(f"{numberOne} - Простое число")
    elif numberOne % devider == 0:
        return print(f"{numberOne} - Составное число")
    return simple(numberOne, devider + 1)
simple(number)

 # определить является ли слово палиндромом

def polindrome(numberTwo):
    if len(numberTwo) <= 1:
        return print (True)
    elif numberTwo[0] == numberTwo[-1]:
        return polindrome(numberTwo[1:-1])
    else:
        return print(False)
number = input('Введите число: ')
polindrome(number)

 # Два различных натуральных числа n и m называются дружественными,
 # если сумма делителей числа n (включая 1, но исключая само n)
 # равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
 # По данному числу k выведите все пары дружественных чисел,
 # каждое из которых не превосходит k. Программа получает на вход одно
 # натуральное число k, не превосходящее 10 ** 5. Программа должна
 # вывести все пары дружественных чисел, каждое из которых не превосходит k. 
 # Пары необходимо выводить по одной в строке, разделяя пробелами. 
 # Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
 # Ввод: Вывод:
 # 300   220 284

def devidersSum(number):
    sumOne = 0
    for i in range(1, number):
        if number % i == 0:
            sumOne += i
    return sumOne

number = int(input("Введите число: "))
def friend(number):
    if number > 100000:
        return print("Слишком большое число")
    else:
        sumPairs = []
        for i in range(1, number):
            if i not in sumPairs:
                temp = devidersSum(i)
                if i == devidersSum(temp) and i != temp:
                    sumPairs.append(temp)
                    sumPairs.append(i)
        setPairs = set(sumPairs)
    return setPairs
print(friend(number))

 # Даны два массива чисел. Требуется вывести те элементы
 # первого массива (в том порядке, в каком они идут в первом
 # массиве), которых нет во втором массиве. Пользователь вводит
 # число N - количество элементов в первом массиве, затем N
 # чисел - элементы массива. Затем число M - количество
 # элементов во втором массиве. Затем элементы второго массива

listOne = [(lambda i: i*i)(i) for i in range(0,10)]
print(listOne)
listTwo = [i for i in range(0,20)]
print(listTwo)
for i in listOne:
    if i not in listTwo:
        print(i)


 # Дан массив, состоящий из целых чисел. Напишите
 # программу, которая в данном массиве определит
 # количество элементов, у которых два соседних и, при
 # этом, оба соседних элемента меньше данного. Сначала
 # вводится число N — количество элементов в массиве
 # Далее записаны N чисел — элементы массива. Массив
 # состоит из целых чисел.
    
import random
listOne = []
listLength = int(input("Введите количество элементов в списке: "))
for i in range(listLength):
    listOne.append(random.randint(0, 50))
print(listOne)
count = 0
for i in range(1, listOne[-2]):
    if listOne[i] > listOne[i+1] and listOne[i] > listOne[i-1]:
        count += 1
print(f'Количество элементов, у которых два соседних элемента меньше равно {count}')


 # Дан список чисел. Посчитайте, сколько в нем пар
 # элементов, равных друг другу. Считается, что любые
 # два элемента, равные друг другу образуют одну пару,
 # которую необходимо посчитать. Вводится список
 # чисел. Все числа списка находятся на разных строках.

import random
listOne = []
listLength = int(input("Введите количество элементов в списке: "))
for i in range(listLength):
    listOne.append(random.randint(0, 5))
print(listOne)
count = 0
for i in range(1, len(listOne)-2):
    if i == listOne[i-1] or i == listOne[i+1]:
        count +=1
print(count)




