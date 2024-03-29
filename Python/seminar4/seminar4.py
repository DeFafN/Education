﻿ #Напишите программу, которая принимает на вход
 #строку, и отслеживает, сколько раз каждый символ
 #уже встречался. Количество повторов добавляется к
 #символам с помощью постфикса формата _n.

string = 'a a a b c a a d c d d'.split()
chars = {}
newString = []
for char in string:
    if char in chars:
        count = chars[char]
        chars[char] = count + 1
        newString.append(char + '_' + str(count))
    else:
        chars[char] = 1
        newString.append(char)
print(newString)


#Пользователь вводит текст(строка). Словом считается
#последовательность непробельных символов идущих
#подряд, слова разделены одним или большим числом
#пробелов или символами конца строки.Определите,
#сколько различных слов содержится в этом тексте.

text = """She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.""".split()
count = set(text)
print(len(count))


 #Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
 #Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

listLengthOne = int(input('Введите длинну списка 1: '))
numlistOne = []
for element in range(listLengthOne):
    element = int(input('Введите элемент: '))
    numlistOne.append(element)
listLengthTwo = int(input('Введите длинну списка 2: '))
numlistTwo = []
for element in range(listLengthTwo):
    element = int(input('Введите элемент: '))
    numlistTwo.append(element)
uniquenumlist = set(numlistOne) & set(numlistTwo)
UniqeNumlist = list(uniquenumlist)
print(UniqeNumlist)
for i in range(len(UniqeNumlist)-2):
    for j in range(len(UniqeNumlist)-2):
        if UniqeNumlist[j] > UniqeNumlist[j+1]:
            UniqeNumlist[j] = UniqeNumlist[j+1]

print(f'Уникальные элементы списков {uniquenumlist}') 


 #В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста
 #есть ровно два соседних. Всего на грядке растёт N кустов.
 #Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
 #В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
 #Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
 #Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
 #заданной во входном файле грядки.

import random

bashQantity = int(input('Введите количество кустов на грядке: '))
gardenBeds = []
for bash in range(bashQantity):
    bash = random.randint(0, 50)
    gardenBeds.append(bash)
print(gardenBeds)
maxHarvest = gardenBeds[-1] + gardenBeds[0] + gardenBeds[1]
print(maxHarvest)
for bash in range(len(gardenBeds)-2):
    if gardenBeds[bash] + gardenBeds[bash +1] + gardenBeds[bash + 2] > maxHarvest:
        maxHarvest = gardenBeds[bash] + gardenBeds[bash +1] + gardenBeds[bash + 2]
print(f'Максимальное количество ягод собранных за 1 раз: {maxHarvest}') # Есть ли вариант решить оптимальнее?