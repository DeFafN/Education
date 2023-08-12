# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

element = int(input('Введите первый элемент прогрессии: '))
lenList = int(input('Введите количесвто элементов: '))
step = int(input('Введите разность между элементами: '))
arithmeticProgression = []
arithmeticProgression.append(element)
print(arithmeticProgression)
for i in range(lenList): 
    element = element + step
    arithmeticProgression.append(element)
print(arithmeticProgression)


# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# т.е. не меньше заданного минимума и не больше заданного максимума

numList = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
indexList = []
#for element in numList:
#    if element > 5 and element <15:
#      indexList.append(numList.index(element))
#print(f'Индексы элементов в диапозоне от 5 до 15 {indexList}')

# без накопителя
for element in numList:
    if element > 5 and element <15:
      print(f'Индекс элемента {element} в диапозоне от 5 до 15 равен {numList.index(element)}')
