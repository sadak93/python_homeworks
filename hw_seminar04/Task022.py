# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

n_of_list_1 = int(input('Введите кол-во чисел 1 списка: '))
list_1 = [randint(0,50) for _ in range(n_of_list_1)]
n_of_list_2 = int(input('Введите кол-во чисел 2 списка: '))
list_2 = [randint(0,50) for _ in range(n_of_list_2)]
print(f'1ый набор целый чисел: {list_1}')
print(f'2ой набор целый чисел: {list_2}')
list_1 = set(list_1)
list_2 = set (list_2)
#print(list_1)
#print(list_2)

list_3 = list_1.union(list_2)
#print(list_3)
list_3 = list(list_3)
temp = 0
max_elem = list_3[0]
for i in range(len(list_3)-1):
    for j in range(len(list_3)-i-1):
        if list_3[j]>list_3[j+1]:
            list_3[j], list_3[j+1] = list_3[j+1], list_3[j]
print(f'Числа встречающиеся в обоих наборах в порядке возрастания: {list_3}')
