a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))

if a > b: 
    print(f'{a} больше {b}')
elif a==b:
     print('числа равны')
else:
    print(f'{b} больше {a}')