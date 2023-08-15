# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).

numList = [1, 2, 3, 5, 8, 15, 23, 38] 
#newNumList = []
#for number in numList:
#    if number % 2 == 0:
#        newNumList.append((number, number**2))
#print(newNumList)

#def select(f, col):
#    return [f(x) for x in col]
#def where(f, col):
#    return [x for x in col if f(x)]

newNumList = map(int, numList) #select заменён на map
newNumList = filter(lambda x: x % 2 == 0, newNumList) # where заменён на filter
newNumList = list(map(lambda x: (x, x**2), newNumList))
print(newNumList)