## Дан список чисел. Определите, сколько в нем встречается различных чисел.
## Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
## Примечание: Пользователь может вводить значения списка или список задан изначально

#numList = [1, 1, 2, 0, -1, 3, 4, 4]
#print(numList)
#numlist2 = []
#for i in numList:
#    if i not in numlist2:
#        numlist2.append(i)
#print(numlist2)
#print(len(numlist2))
#print(len(set(numList))) # простое решение

## Дана последовательность из N целых чисел и число K.
## Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
## Input: [1, 2, 3, 4, 5] k = 2 Output: [4, 5, 1, 2, 3]

#numListLength = int(input('Введите длинну списка:'))
#numList = []
#for i in range(numListLength):
#    i = int(input('Введите элемент списка:'))
#    numList.append(i)
#k = int(input('Введите число: '))
#k = k % numListLength
#for i in range(k):
#    temporaryValue = numList.pop()
#    numList.insert(0, temporaryValue)
#print(numList)

## Напишите программу для печати всех уникальных значений в словаре.
## Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
## Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
## Примечание: Список словарей задан изначально. Пользователь его не вводит
 
#dictList = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
#uniqueValuses = set()
#for i in dictList:
#    for j in i:
#        uniqueValuses.add(i[j])
#print(f'Уникальные значения словарей: {uniqueValuses}')

## Дан массив, состоящий из целых чисел.
## Напишите программу, которая подсчитает количество элементов массива, больших предыдущего
## (элемента с предыдущим номером) 
## Input: [0, -1, 5, 2, 3]
## Output: 2 (-1 < 5, 2 < 3)

#import random
#listLength = int(input('Введите длинну списка: '))
#numlist = []
#count = 0
#for i in range(listLength):
#    i = random.randint(-1000,1000)
#    numlist.append(i)
#print(numlist)
#for i in range(1,len(numlist)):
#    if numlist[i-1] < numlist[i]:
#        count += 1
#print(f'Количество элементов больше предыдущего {count}')


## Требуется вычислить, сколько раз встречается некоторое
## число X в массиве A[1..N]. Пользователь в первой строке вводит
## натуральное число N – количество элементов в массиве. В последующих
## строках записаны N целых чисел Ai. Последняя строка содержит число X

#import random
#listLength = int(input('Введите длинну списка: '))
#numlist = []
#for i in range(listLength):
#    i = random.randint(0,1)
#    numlist.append(i)
#print(numlist)
#targetValue = int(input('Введите искомое число: '))
#count = 0
#for i in range(len(numlist)):
#    if targetValue == numlist[i]:
#        count+=1
#print(f'Число встречается {count} раз')


## Требуется найти в массиве A[1..N] самый близкий по
## величине элемент к заданному числу X. Пользователь в первой строке
## вводит натуральное число N – количество элементов в массиве. В
## последующих строках записаны N целых чисел Ai.
## Последняя строка содержит число X

#import random
#from typing import Required
#listLength = int(input('Введите длинну списка: '))
#numlist = []
#for i in range(listLength):
#    i = random.randint(0,10)
#    numlist.append(i)
#print(numlist)

#requiredNumber = int(input('Введите искомое число: '))
#module = abs(requiredNumber - numlist[0])
#disiredNumber = numlist[0]

#for i in range(1, len(numlist)):
#    if module > abs(numlist[i] - requiredNumber):
#        module = abs(numlist[i] - requiredNumber)
#        disiredNumber = numlist[i]
#print(f'Ближайшее число {disiredNumber}')


## В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
## ценность. В случае с английским алфавитом очки распределяются так:
##  ● A, E, I, O, U, L, N, S, T, R – 1 очко;
##  ● D, G – 2 очка;
##  ● B, C, M, P – 3 очка;
##  ● F, H, V, W, Y – 4 очка;
##  ● K – 5 очков;
##  ● J, X – 8 очков;
##  ● Q, Z – 10 очков.
##  А русские буквы оцениваются так:
##  ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
##  ● Д, К, Л, М, П, У – 2 очка;
##  ● Б, Г, Ё, Ь, Я – 3 очка;
##  ● Й, Ы – 4 очка;
##  ● Ж, З, Х, Ц, Ч – 5 очков;
##  ● Ш, Э, Ю – 8 очков;
##  ● Ф, Щ, Ъ – 10 очков.
##  Напишите программу, которая вычисляет стоимость введенного пользователем слова.
##  Будем считать, что на вход подается только одно слово, которое содержит либо только
##  английские, либо только русские буквы.

#rusDict = {'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2,
#          'П':2, 'У':2, 'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Й':4, 'Ы':4, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10,
#         'Щ':10, 'Ъ':10}
#enDict = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2, 'B':3, 'C':3,
#         'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}

#word = input('Введите слово: ')
#seachWord = word.upper()
#score = 0
#for letter in seachWord:
#    if letter in rusDict:
#        score = score + rusDict[letter]
#    elif letter in enDict:
#         score = score + enDict[letter]
#    else:
#        print('Нет такой буквы')
#print(f'Количество очков за слово {score}')
