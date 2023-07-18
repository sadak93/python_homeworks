# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.

import math

n = int (input('Введите число: '))
k = 1
while k < n:
    print(k, end=', ')
    k *= 2
print()

k = 0
stepen = 0
while k < n:
    print(round(k), end=', ')
    k = math.pow(2, stepen)
    stepen += 1
    
    