# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета 
# с номером n и выводит на экран yes или no.

# Пример:

# n = 385916 -> yes
# n = 123456 -> no

n = 385916

n1 = (n//100000)+(n//10000)%10+(n//1000)%10
n2 = (n%10)+(n%100)//10+(n%1000)//100
if n1==n2:
    print('yes')
else:
    print('no')