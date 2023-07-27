# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n_coins = int (input('Введите кол-во монет: '))
count_0 = 0
count_1 = 0
for i in range(n_coins):
    current_coin = randint (0,1)
    print(current_coin, end=' ')
    if current_coin==0:
        count_0 += 1
    else:
        count_1 += 1
print(f'\nКол-во монет лежащих вверх решкой - {count_0}, вверх гербом - {count_1}')

print ('Перевернем минимальное кол-во монет, чтоб лежали одинаково: ')
for i in range(n_coins):
    if count_0 >= count_1:
        current_coin = 0
        print(current_coin, end=' ')
    else:
        current_coin = 1
        print(current_coin, end=' ')

# import random

# coins = int(input('Введите общее количество монет: '))
# heads = 0
# all_coins = 0

# for i in range(coins):
#     coin = random.randint(0, 1)
#     print(coin, end=' ')
#     heads += coin

# if heads != coins and heads != 0:
#     print(f'\nНужно перевернуть {1 if heads < coins // 2 + 1 else 0}')
# else:
#     print('\nНичего переворачивать не нужно')