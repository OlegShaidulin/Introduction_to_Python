# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

num = int(input('Введите количество монет: '))
count_orel = 0
count_reshka = 0
index = 0
while index <= num:
    count = random.randint(0,1)
    print(count, end=" ")
    if count == 0:
        count_orel += 1
    else:
        count_reshka += 1
    index += 1
result = count_orel if count_orel>count_reshka else count_reshka
print(f'\n результат {result}')  