# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input('Введите трезночное число: '))
print('Сумма чисел = ', n % 10 + n % 100 // 10 +  n // 100)