# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

from unicodedata import digit


speed = int(input('Введите пройденное за день расстояние: '))
distance = int(input('Введите длинну маршрута: '))

print("Количество дней для того чтобы пройти маршрут равно ", distance // speed +(distance % speed != 0))
print("Количество дней для того чтобы пройти маршрут равно ", (-(-distance // speed)))
print("Количество дней для того чтобы пройти маршрут равно ", (abs(-distance // speed)))
print("Количество дней для того чтобы пройти маршрут равно ", (speed+distance-1) // speed)


# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

studentsInFirstClass = int(input('Введите количество учеников в первом классе: '))
studentsInSecondClass = int(input('Введите количество учеников во втором классе: '))
studentsInThirdClass = int(input('Введите количество учеников в третьем классе '))
studentsInDesk = int(input('Введите количество учеников за одной партой '))
print("Количество необходимых парт равно ", ((studentsInFirstClass // studentsInDesk) + (studentsInFirstClass % studentsInDesk != 0)) +abs((-studentsInSecondClass // studentsInDesk)) + ((studentsInThirdClass // studentsInDesk) + (studentsInThirdClass // studentsInDesk == 0)))
print("Количество необходимых парт равно ", ((studentsInFirstClass + studentsInSecondClass + studentsInThirdClass) // studentsInDesk) + ((studentsInFirstClass + studentsInSecondClass + studentsInThirdClass) % studentsInDesk != 0))


# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

vanVasya = int(input('Введите номер вагона в который зашёл Вася: '))
vanNumber = int(input('Введите номер вагона который Вася увидел на вагоне: '))
if vanVasya == vanNumber:
    print('Без дополнительной информации узнать количество вагонов невозможно')
else:
    print('Количество вагонов в поезде: ', vanNumber + vanVasya - 1 )


# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

yearNumber = int(input('Ввведите год: '))
if (yearNumber % 4 == 0 and yearNumber % 100 != 0) or yearNumber % 400 == 0:
    print('Год является високосным')
else:
    print('Год не является високосным')


# Найдите сумму цифр трехзначного числа n.

number = int(input('введите число: '))
digitSum = 0
while number > 0:
    digitSum = digitSum + number % 10
    number = number // 10
print(f'Сумма чисел равна {digitSum}')


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

cranNumbers = int(input('Введите количество сделанных журавликов: '))

if cranNumbers % 6 != 0:
    print('Столько журавликов не могло быть сделано')
else:
    patyaCran = cranNumbers // 6
    sergeyCran = cranNumbers // 6
    katyaCran = (cranNumbers // 6) * 4
    print(patyaCran, katyaCran, sergeyCran)

#for i in range(1, cranNumbers):
#        petyaCran = i
#        katyaCran = 0
#        if katyaCran = ((petyaCran + petyaCran) * 2) == cranNumbers:
#            cranK = katyaCran
#            cranP = petyaCran
#            cranS = petyaCran
#            answer = ('cranP', 'cranK', 'cranS')


# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

ticketNumber = input('Введите номер билета: ')
if len(ticketNumber) != 6:
    print('Введён неверный номер билета')
else:
    numberOne = int(ticketNumber[0:3])
    numberTwo = int(ticketNumber[3:6])
    digitSumOne = 0
    digitSumTwo = 0
    while numberOne > 0 and numberTwo > 0: 
        digitSumOne = digitSumOne + numberOne % 10
        numberOne = numberOne // 10
        digitSumTwo = digitSumTwo + numberTwo % 10
        numberTwo = numberTwo // 10
if digitSumOne == digitSumTwo:
    print('У тебя СЧАСТЛИВЫЙ БИЛЕТ')
else:
    print('Не повезло (')

# Определите, можно ли от шоколадки размером a × b долек отломить c долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

sizeA = int(input('Введите размер первой стороны шоколадки: '))
sizeB = int(input('Введите размер второй стороны шоколадки: '))
clove = int(input('Введите размер дольки: '))
if clove > sizeA * sizeB and (clove % sizeA == 0 or clove % sizeB == 0):
    print('Поделить можно')
else:
    print('что-то пошло не так')