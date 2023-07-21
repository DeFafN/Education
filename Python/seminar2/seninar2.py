##По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N 
##(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

n = int(input('введите число:'))
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i += 1
print(factorial)

##Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
##то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

a = int(input('Введите число: '))
f0 = 0
f1 = 1
f = 0
i = 1
while f < a:
    f = f0 + f1
    f0 = f1
    f1 = f
    i +=1
    print(f)
if f == a:
    print('номер числа ', i)
else:
    print('-1')
    
## На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
## Определите минимальное число монеток, которые нужно перевернуть,
## чтобы все монетки были повернуты вверх одной и той же стороной.
## Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
x = int(input('Введите количество монет: '))
coinsNumber = []
i = 1
for i in range(1,x+1):
    coinsNumber.append(i)
    i+=1
print(coinsNumber)
coinRevers = 0
coinAwers = 0
for i in range(0,len(coinsNumber)):
    coinSide = randint(0,1)
    if coinSide == 0:
        coinAwers += 1
    else:
        coinRevers += 1
    i+=1
print(f'количество монет лежащих орлом равно {coinRevers}, а количество монетлежащих решкой равно {coinAwers}')
if coinAwers < coinRevers:
    print(f'Необходимо перевернуть {coinAwers} монет')
elif coinRevers < coinAwers:
    print(f'Необходимо перевернуть {coinRevers} монет')
else:
    print(f'Количество монет лежащих орлом и решкой одинаково, необходимо перевернуть {coinAwers} монет')

## Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
## Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
## а Катя должна их отгадать. Для этого Петя делает две подсказки.
## Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint
x = randint(0,1000)
print(f'Первое задуманное число {x}') # печать для проверки итога        x+y=s
y = randint(0,100 )                                                    # x*y=p
print(f'Второе задуманное число {y}') # печать для проверки итога        y=s-x
s = x + y                                                              # x*(s-x)=p
print('Сумма чисел равна: ', s)                                        # x*s - x*x = p
p = x * y                                                              # -x*x + s*x - p = 0 умножил на -1
print('Произведение чисел равно: ', p)                                 # x*x-s*x+p=0

discriminant = (s*s - 4*p)

if discriminant >= 0:
    guessedNumberOne = ((s + (discriminant**0.5))/2)
    guessedNumberTwo = s - abs(guessedNumberOne)
    print("Загаданные числа ", guessedNumberOne, guessedNumberTwo, "или наоборот, что не принципиально")

else:
    print('Угадать нельзя')

## Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите число: '))
listOfNumbers = []
for i in range (0,number+1):
    listOfNumbers.append(i)
    i +=1
listOfDegrees = []
for i in listOfNumbers:
    for j in range (0,i):
        if i == 2**(j):
            listOfDegrees.append(i)
        j +=1
    i +=1
print(f'Степени двойки до {number} равны {listOfDegrees}')
