# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X

list_1 = [1, 4, 3, 7, 8, 9, 2]
k = 5
x = 0
for i in range(0,len(list_1)):
    if list_1[i] == k:
        x = list_1[i]
        break
    elif list_1[i] == (k+1) or list_1[i] == (k-1):
        x = list_1[i]
print(x)

# print(list_1)

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)