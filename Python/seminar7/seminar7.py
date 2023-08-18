﻿def func1(x):
    return x
print(func1(5))

func2 = lambda x: x
print(func2(5))


# # У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# # transformation = <???>
# # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# # transormed_values = list(map(transformation, values))
# # Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# # Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# # Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# # values = [1, 23, 42, ‘asdfg’]
# # transformed_values = list(map(trasformation, values)) if values == transformed_values:
# # print(‘ok’) else:
# # print(‘fail’)
# # Вывод:
# # ok

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = list(filter(lambda x: x==x, values))
print(transformation)

# # с помощью лямбда и фильтра составить список из двух значных чисел. ввод "2 10 -32 8 1 78", вывод [10, -32, 78]

values = [2, 10, -32, 8, 1, 78]
newValues = list(filter(lambda x: 9 < abs(x) < 100 , values))
print(newValues)

values2 = '2 10 -32 8 1 78'
newValues = list(filter(lambda x: 9 < abs(x) < 100 , map(int, values2.split())))
print(newValues)

newValues = list(filter(lambda x: len(str(abs(int(x))))==2, values2.split()))
print(newValues)

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, 
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits))
# Вывод: 2.5 10

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def farest_orbit(listOfOrbits):
    multiplication = max(halfaxisA*halfAsisB for halfaxisA,halfAsisB in orbits if halfaxisA!=halfAsisB)
    masxSqare = [(a,b) for a,b in orbits if a*b==multiplication]
    return masxSqare
    
print(farest_orbit(orbits))


# в 2 строки для конкретно этого списка:

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*max(orbits, key = lambda x: (x[0] != x[1]) * x[0]*x[1]))

            
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам    

chant = input('Напиши кричалку: ').split()
def FindRythm(chant):
    vowelList = ['а', 'о', 'я', 'и', 'у', 'е', 'э', 'ю', 'ы' 'ё']
    count = 0
    for i in chant:
        for j in i:
            if j in vowelList:
                count += 1
    if count % len(chant) == 0:
        return print('Парам пам-пам')
    else:
        return print('Пам парам')
FindRythm(chant)


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def print_operation_table(operation, num_rows=6, num_columns=6):
    product = []
    for i in range(1,num_rows):
        row = []
        for j in range(1, num_columns):
            row.append(i*j)
        product.append(row)
    return print("\n".join(map(str,product)))

print_operation_table(lambda x,y: x*y)




















