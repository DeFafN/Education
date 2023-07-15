from os import replace
from pickle import TRUE


print(5,8,6)

n =5 
print(n)
print(type(n))

n = None
print(n)
print(type(n))

n = 1.89
print(n)
print(type(n))

n = "hello"
print(n)
print(type(n))

print('asdasda "dfsdf" ')

a = 5 
b = 85.24
c = 'hello'

print(a, '-', b, '-', c)
print(f'{a} - {b} - {c}')
print('{}-{}-{}'.format(a,b,c)) 

print('Введите первое число')
a = int(input())
print(a)
b = int(input('введите второе число: '))

print(a, '+', b, ' = ', a+b)

a = 1.57632
b = 5.22479
print(round(a * b, 3))

inter = 10
print(inter)
inter += 3
print(inter)
inter -= 4
print(inter)
inter *= 5
print(inter)
inter /= 2
print(inter)
inter //= 2
print(inter)
inter %= 3
print(inter)
inter **= 5
print(inter)

a = 1 > 4
print(a)
a = 1 < 4 and 5 > 2
print(a)
a = 1 == 2
print(a)
a = 1 != 2
print(a)
a = 'qwe'
b = 'qwe'
print(a==b)
a = 'qwe'
b = 'qWe'
print(a==b)
a = 1 < 3 < 5 < 10
print(a)
a = 1 < 3 > 5 < 10
print(a)

username = input('Введите имя: ')
if username == "Маша":
    print("Ура это же МАША!!!!!!")
elif username == "Эльдар":
    print("Эльдар - стронг")
elif username == "Марина":
    print("Я так ждала тебя Марина")
else:
    print(f"Привет {username}")

n = 423
sum = 0
while n > 0:
    sum = n % 10 + sum
    n = n // 10
print(sum)

i = 0
while i < 5:
    if i == 3:
        break
    i += 1
else:
    print('Пожалуй')
    print('Хватит')
print(i)

i = 0
while i < 5:
    i += 1
else:
    print('Пожалуй')
    print('Хватит')
print(i)

n = int(input('введите число:'))
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1

for i in 'qwerty':
    print(i)

a = 'qwerty'
for i in a:
    print(i)


line = ''
for i in range(10):
    line = ''
    for j in range(2):
        line += '*'
    print(line)

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё', 'ЕЩЁ'))
print(text[0])
print(text[1])
print(text[len(text)-1])
print(text[-5])
print(text[:])
print(text[:2])
print(text[len(text)-2:])
print(text[2:9])
print(text[6:-18])
print(text[0:len(text):6])
print(text[::6])
text = text[2:9] + text[-5] + text[2]
print(text)

