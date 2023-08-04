# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n_of_list_1 = int(input('Введите кол-во чисел списка: '))
list_1 = [randint(-20,20) for _ in range(n_of_list_1)]
print(list_1)

list_2_start = int(input('Введите начало диапазона: '))
list_2_end = int(input('Введите конец диапазона: '))
list_2 = []
for i in range(list_2_end-list_2_start+1):
    list_2.append(list_2_start+i)
#print(list_2)

list_3 = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_2[j] == list_1 [i]:
            list_3.append(i)
print(list_3)