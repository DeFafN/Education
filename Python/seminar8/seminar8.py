# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
import os

def WorkWithPhonebook():
    choise = ShowMenu()
    phonebook = ReadTxt('phonebook.txt')
    
    while choise != 7:
        if choise == 1:
            PrintResult(phonebook)
        elif choise == 2:
            lastName = input('Фамилия: ')
            print(FindByLastname(phonebook, lastName))
        elif choise == 3:
            lastName = input('Фамилия: ')
            newNumber = input('Новый номер: ')
            print(ChangeNumber(phonebook, lastName, newNumber))
        elif choise == 4:
            lastName = input('Фамилия: ')
            print(DeleteByLastname(phonebook, lastName))
        elif choise == 5:            
            number = input('Введите номер: ')
            print(FindByLastname(phonebook, number))
        elif choise == 6:
            userData = input('Новый абонент: ')
            AddUser(phonebook, userData)
            WriteTxt(phonebook.txt, phonebook)
        choise = ShowMenu()
def ShowMenu():
    print('1. Распечатать справочник\n'
    '2. Найти телефон по фамилии\n' 
    '3. Изменить номер телефона\n'
    '4. Удалить запись\n'
    '5. Найти абонента по номеру телефона\n'
    '6. Добавить абонента в справочник\n'
    '7. Закончить работу')
    choice = int(input())
    return choice

def ReadTxt(filename):
    phoneBook = []
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('phonebook.txt','r') as phb:
        for line in phb:
            record=dict(zip(fields,line.strip().split(',')))
            phoneBook.append(record)
    return phoneBook

def WriteTxt(filename,phoneBook):
    with open('phonebook.txt','w') as phout:
        for i in range(len(phoneBook)):
            string = ''
        for value in phoneBook[i].values():
            string += value+','
        phout.write(f'{string[:-1]}\n')

def PrintResult(phonebook):
    with open ('phonebook.txt','a') as phout:
        print(phout)

def FindByLastname(phonebook, lastName):
    with open ('phonebook.txt','r') as phf:
        for line in phf:
            if lastName == line[0]:
                return print(line)
            else:
                return print('Такой абонент не найден')
        
def ChangeNumber(phonebook, lastName, newNumber):
    with open ('phonebook.txt','w') as phf:
        for line in phf:
            if lastName == line[0]:
                line[2] = newNumber
                return print('номер изменён')
            else:
                return print('Такой абонент не найден')                
def DeleteByLastname(phonebook, lastName):
    with open ('phonebook.txt', 'r') as phf:
        for line in phf:
            if lastName == line[0]:
                del phonebook[i]['lastName']
                return print('Контакт удален')
            else:
                return print('Такой абонент не найден')
            
def AddUser(phonebook, userData):
    user = {'Фамилия': userData[0], 'Имя':userData[1], 'Телефон':userData[2], 'Описание':userData[3]}
    phonebook.append(user)
    with open('phonebook.txt', 'w') as phout:
        for i in range(len(phonebook)):
            string = ''
        for value in phonebook[i].values():
            string += value+','
        phout.write(f'{string[:-1]}\

WorkWithPhonebook()