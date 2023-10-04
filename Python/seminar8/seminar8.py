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
            phoneNumber = input('Введите номер: ')
            print(FindByPhoneNumber(phonebook, phoneNumber))
        elif choise == 6:
            userData = input('Новый абонент: ')
            AddUser(phonebook, userData)
            WriteTxt(phonebook)
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
            lst1 = line.strip().split(',')
            for element in range(len(lst1)):
                lst1[element] = lst1[element].strip()
            record=dict(zip(fields,lst1))
            phoneBook.append(record)
    return phoneBook

def WriteTxt(filename):
    with open('phonebook.txt','w') as phb:
        for i in range(len(phb)):
            string = ''
            for value in phb[i].values():
                string += value+','
        phb.write(f'{string[:-1]}\n')

def PrintResult(phonebook):
    for record in phonebook:
        print(', '.join(record.values()))

def FindByLastname(phonebook, lastName):
    shotlist = []
    for record in phonebook:
        if record['Фамилия'] == lastName:
            shotlist.append(', '.join(record.values()))
            return shotlist
        return 'Такой абонент не найден'

def FindByPhoneNumber(phonebook, phoneNumber):
    shotlist = []
    for record in phonebook:
        if record['Телефон'] == phoneNumber:
            shotlist.append(', '.join(record.values()))
            return shotlist
        return 'Такой абонент не найден'

def ChangeNumber(phonebook, lastName, newNumber):
    
    for record in phonebook:
        if record['Фамилия'] == lastName:
            record['Телефон'] = newNumber
            return 'номер изменен'
        else:
            return 'Такой абонент не найден'


def DeleteByLastname(phonebook, lastName):
    for i, record in enumerate(phonebook):
        if record['Фамилия'] == lastName:
            del phonebook[i]
            WriteTxt('phonebook.txt', phonebook)
            return 'Контакт удален'
    return 'Такой абонент не найден'
            
def AddUser(phonebook, user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    phonebook.append(dict(zip(fields, user_data)))

WorkWithPhonebook()