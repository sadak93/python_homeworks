# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
import math
def f(a,b):
    if b < 1:
        return 1
    # return math.pow(a,b)
    return a*f(a,b-1)

# print(stepen(3,5))

a = 3
b = 5
print(f(a, b))